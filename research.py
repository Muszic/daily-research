import urllib.request
import xml.etree.ElementTree as ET
import os
import random
from datetime import datetime

# --- CONFIGURATION ---
# List of interesting Computer Science categories to pick from
CATEGORIES = [
    'cs.CV', # Computer Vision
    'cs.AI', # Artificial Intelligence
    'cs.LG', # Machine Learning
    'cs.CL', # Computation and Language (NLP)
    'cs.CR', # Cryptography and Security
    'cs.RO', # Robotics
    'cs.SE', # Software Engineering
    'cs.DC', # Distributed, Parallel, and Cluster Computing
]

FILENAME = "DAILY_PAPERS.md"
# ---------------------

def fetch_random_paper():
    # 1. Pick a random category
    selected_category = random.choice(CATEGORIES)
    print(f"Selected Category: {selected_category}")
    
    # 2. Fetch the top 50 recent papers from that category
    # We fetch 50 so we have a good 'pool' to pick a random one from
    url = f'http://export.arxiv.org/api/query?search_query=cat:{selected_category}&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending'
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            
        root = ET.fromstring(data)
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        
        if not entries:
            print("No entries found.")
            return None

        # 3. Pick ONE random paper from the 50 fetched
        random_entry = random.choice(entries)

        # Extract details
        title = random_entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ').strip()
        summary = random_entry.find('{http://www.w3.org/2005/Atom}summary').text.replace('\n', ' ').strip()
        link = random_entry.find('{http://www.w3.org/2005/Atom}id').text
        published = random_entry.find('{http://www.w3.org/2005/Atom}published').text[:10]

        return {
            "title": title,
            "summary": summary,
            "link": link,
            "date": published,
            "category": selected_category
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def update_file(paper):
    if not paper:
        return

    # Read existing content to check for duplicates
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            existing_content = f.read()
    else:
        existing_content = ""

    # DUPLICATE CHECK: If we accidentally picked a paper we already have, stop.
    if paper['title'] in existing_content:
        print(f"Skipping: Paper '{paper['title']}' is already in the log.")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Create the new entry with the Category tag
    new_entry = f"""
## [{date_str}] {paper['title']}
**Category:** {paper['category']} | **Published:** {paper['date']} | [Read Paper]({paper['link']})

> **Abstract:** {paper['summary']}

---
"""
    
    # Write new entry at the top
    header = "# Daily ArXiv Research Log\n\n"
    content_without_header = existing_content.replace(header, "")
    final_content = header + new_entry + content_without_header
    
    with open(FILENAME, "w") as f:
        f.write(final_content)
    
    print(f"Successfully added: {paper['title']}")

if __name__ == "__main__":
    paper = fetch_random_paper()
    update_file(paper)
