import os
import random
import re
import requests
import io
import urllib.request
import xml.etree.ElementTree as ET
import subprocess
import time
from datetime import datetime
from google import genai 
from pypdf import PdfReader

# --- CONFIGURATION ---
CATEGORIES = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL', 'cs.RO', 'cs.CR', 'cs.SE']
CATEGORY_NAMES = {
    'cs.CV': 'Computer Vision', 'cs.AI': 'Artificial Intelligence',
    'cs.LG': 'Machine Learning', 'cs.CL': 'NLP', 'cs.RO': 'Robotics',
    'cs.CR': 'Cryptography', 'cs.SE': 'Software Engineering'
}

# --- DECISION ENGINE ---
# This controls how "human" the bot acts
def decision_engine():
    """
    Decides how many papers to process today based on random probability.
    Returns: Integer (number of commits to make)
    """
    # 1. Check if we already worked today (to avoid accidental 4x/day runs from cron)
    # We check the log file for today's date
    today = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists("run_log.txt"):
        with open("run_log.txt", "r") as f:
            if today in f.read() and random.random() > 0.1: 
                # If we already worked today, 90% chance to stop (unless we are in a 'crunch' frenzy)
                print("Already worked today. Taking a break.")
                return 0

    # 2. Roll the Dice (0.0 to 1.0)
    roll = random.random()
    
    if roll < 0.25:
        # 25% chance to be "Lazy" (Skip day)
        print("Dice Roll: Lazy Day. Skipping.")
        return 0
    elif roll < 0.85:
        # 60% chance to be "Consistent" (1 commit)
        print("Dice Roll: Normal Work Day.")
        return 1
    else:
        # 15% chance to be "Productive" (2-4 commits)
        # Randomly choose between 2, 3, or 4
        burst = random.randint(2, 4)
        print(f"Dice Roll: CRUNCH MODE! Doing {burst} commits.")
        return burst

# --- CORE FUNCTIONS ---

API_KEY = os.environ.get("GEMINI_API_KEY")
client = None
if API_KEY:
    client = genai.Client(api_key=API_KEY)

def git_commit_and_push(paper_title):
    """
    Executes git commands directly from Python to create a commit history.
    """
    try:
        # Stage all changes (new papers + log)
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit with a meaningful message
        commit_message = f"Added notes for: {paper_title[:30]}..."
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push immediately
        subprocess.run(["git", "push"], check=True)
        print("Git push successful.")
        
    except subprocess.CalledProcessError as e:
        print(f"Git Error: {e}")

def log_run(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("run_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def fetch_paper_data():
    category = random.choice(CATEGORIES)
    url = f'http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending'
    
    try:
        with urllib.request.urlopen(url) as response:
            root = ET.fromstring(response.read())
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        return entries, category
    except Exception as e:
        print(f"ArXiv Error: {e}")
        return None, None

def process_one_paper():
    entries, category = fetch_paper_data()
    if not entries: return False

    # Try to find a unique paper
    random.shuffle(entries)
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ').strip()
        date = entry.find('{http://www.w3.org/2005/Atom}published').text[:10]
        safe_title = re.sub(r'[^\w\-_\. ]', '', title).replace(' ', '_')[:40]
        filename = f"papers/{date}_{safe_title}.md"
        
        if not os.path.exists(filename):
            # Found unique paper, process it
            pdf_link = entry.find('{http://www.w3.org/2005/Atom}id').text.replace("/abs/", "/pdf/") + ".pdf"
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            
            # Extract PDF
            text = ""
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                resp = requests.get(pdf_link, headers=headers)
                reader = PdfReader(io.BytesIO(resp.content))
                for p in reader.pages[:6]: text += p.extract_text()
            except:
                text = "PDF Extraction failed."

            # Generate AI Summary
            summary = "AI Summary Unavailable."
            if client and len(text) > 500:
                try:
                    prompt = "Summarize this research paper in Markdown (Problem, Method, Impact):\n" + text[:40000]
                    resp = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    summary = resp.text
                except Exception as e:
                    summary = f"Gemini Error: {e}"
            
            # Save File
            if not os.path.exists("papers"): os.makedirs("papers")
            content = f"# {title}\n\n- **Category:** {CATEGORY_NAMES.get(category, category)}\n- **Date:** {date}\n- **Link:** {link}\n\n---\n{summary}"
            with open(filename, "w", encoding='utf-8') as f: f.write(content)
            
            log_run(f"Processed: {title}")
            
            # COMMIT THIS INDIVIDUAL PAPER
            git_commit_and_push(title)
            return True
            
    return False

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    commits_today = decision_engine()
    
    if commits_today > 0:
        print(f"Starting work... Target: {commits_today} papers.")
        for i in range(commits_today):
            success = process_one_paper()
            if success:
                print(f"Commit {i+1}/{commits_today} done.")
                # Sleep between bursts so timestamps aren't identical (looks more human)
                if i < commits_today - 1:
                    wait_time = random.randint(30, 120)
                    print(f"Taking a coffee break for {wait_time} seconds...")
                    time.sleep(wait_time)
            else:
                print("Could not find new paper or error occurred.")
    else:
        log_run("Skipped run (Decision Engine).")
