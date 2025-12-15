import os
import random
import re
import requests
import io
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from google import genai 
from pypdf import PdfReader

# --- CONFIGURATION ---
CATEGORIES = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL', 'cs.RO']
CATEGORY_NAMES = {
    'cs.CV': 'Computer Vision',
    'cs.AI': 'Artificial Intelligence',
    'cs.LG': 'Machine Learning',
    'cs.CL': 'NLP',
    'cs.RO': 'Robotics'
}

# Configure Gemini Client
API_KEY = os.environ.get("GEMINI_API_KEY")
client = None
if API_KEY:
    client = genai.Client(api_key=API_KEY)

def log_run(message):
    """Updates a log file to ensure we always have a commit for the day."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("run_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def fetch_papers_from_arxiv():
    selected_category = random.choice(CATEGORIES)
    print(f"Selected Category: {selected_category}")
    
    url = f'http://export.arxiv.org/api/query?search_query=cat:{selected_category}&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending'
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
        root = ET.fromstring(data)
        return root.findall('{http://www.w3.org/2005/Atom}entry'), selected_category
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None, None

def get_unique_paper(entries, category):
    """Tries to find a paper that doesn't exist yet."""
    if not entries: return None
    
    # Shuffle entries to pick randomly
    random.shuffle(entries)
    
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ').strip()
        # Create filename to check existence
        safe_title = re.sub(r'[^\w\-_\. ]', '', title).replace(' ', '_')[:40]
        date_str = entry.find('{http://www.w3.org/2005/Atom}published').text[:10]
        filename = f"papers/{date_str}_{safe_title}.md"
        
        if not os.path.exists(filename):
            # Found a new paper!
            pdf_link = entry.find('{http://www.w3.org/2005/Atom}id').text.replace("/abs/", "/pdf/") + ".pdf"
            return {
                "title": title,
                "date": date_str,
                "link": entry.find('{http://www.w3.org/2005/Atom}id').text,
                "pdf_link": pdf_link,
                "category": CATEGORY_NAMES.get(category, category)
            }
    
    return None # All 50 papers already exist (unlikely)

def extract_text_from_pdf(pdf_url):
    print(f"Downloading PDF: {pdf_url}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(pdf_url, headers=headers)
        f = io.BytesIO(response.content)
        reader = PdfReader(f)
        text = ""
        for page in reader.pages[:7]: 
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def generate_ai_summary(text):
    if not client: return "Error: GEMINI_API_KEY not found."
    
    prompt = """
    You are an expert research assistant. Summarize this paper in Markdown:
    ## 🧐 Problem
    ## 🛠️ Method
    ## 📊 Impact
    
    Paper text:
    """ + text[:50000]
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Generation Failed: {e}"

def save_paper_note(paper, ai_summary):
    if not os.path.exists("papers"): os.makedirs("papers")
    
    safe_title = re.sub(r'[^\w\-_\. ]', '', paper['title']).replace(' ', '_')[:40]
    filename = f"papers/{paper['date']}_{safe_title}.md"
    
    content = f"# {paper['title']}\n\n- **Category:** {paper['category']}\n- **Published:** {paper['date']}\n- **Source:** [Original ArXiv Link]({paper['link']})\n\n---\n\n{ai_summary}\n"
    
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {filename}")
    log_run(f"Successfully processed: {paper['title']}")

if __name__ == "__main__":
    entries, category = fetch_papers_from_arxiv()
    if entries:
        paper = get_unique_paper(entries, category)
        if paper:
            pdf_text = extract_text_from_pdf(paper['pdf_link'])
            if pdf_text:
                summary = generate_ai_summary(pdf_text)
                save_paper_note(paper, summary)
            else:
                log_run("PDF download failed.")
        else:
            log_run("No new unique papers found in this batch.")
    else:
        log_run("Failed to fetch from ArXiv.")
