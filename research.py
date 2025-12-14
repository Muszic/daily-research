import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

# --- CONFIGURATION ---
# 'cs.CV' = Computer Vision
# 'cs.CL' = Computation and Language (NLP)
# 'cs.LG' = Machine Learning
CATEGORY = 'cs.CV' 
FILENAME = "DAILY_PAPERS.md"
# ---------------------

def fetch_latest_paper():
    # Query ArXiv API for the most recent paper in the category
    print(f"Fetching latest paper for {CATEGORY}...")
    url = f'http://export.arxiv.org/api/query?search_query=cat:{CATEGORY}&start=0&max_results=1&sortBy=submittedDate&sortOrder=descending'
    
    try:
        data = urllib.request.urlopen(url).read()
        root = ET.fromstring(data)
        entry = root.find('{http://www.w3.org/2005/Atom}entry')
        
        if entry is None:
            print("No entry found.")
            return None

        # Extract details (cleaning up newlines in titles/summaries)
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.replace('\n', ' ').strip()
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.replace('\n', ' ').strip()
        link = entry.find('{http://www.w3.org/2005/Atom}id').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text[:10]

        return {
            "title": title,
            "summary": summary,
            "link": link,
            "date": published
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def update_file(paper):
    if not paper:
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Format the new entry (Markdown)
    new_entry = f"""
## [{date_str}] {paper['title']}
**Published:** {paper['date']} | [Read Paper]({paper['link']})

> **Abstract:** {paper['summary'][:400]}...

---
"""
    
    # Read existing content
    try:
        with open(FILENAME, "r") as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = "# Daily ArXiv Research Log\n\n"
        
    # Write new content AT THE TOP (Prepend)
    with open(FILENAME, "w") as f:
        f.write(existing_content + new_entry) # Writes to bottom. Swap to `new_entry + existing_content` if you want newest at top.
        # I recommend appending to bottom for a chronological log, or top for a 'blog' style.
        # Let's stick to appending to the bottom for a history log:
        f.write(entry_to_write) 
    
    # CORRECTED LOGIC for "Newest at Top" (Better for visibility):
    final_content = new_entry + existing_content.replace("# Daily ArXiv Research Log\n\n", "")
    with open(FILENAME, "w") as f:
        f.write("# Daily ArXiv Research Log\n\n" + final_content)
    
    print(f"Successfully added: {paper['title']}")

if __name__ == "__main__":
    paper = fetch_latest_paper()
    update_file(paper)
