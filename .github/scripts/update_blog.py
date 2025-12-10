import feedparser
from datetime import datetime

FEED_URL = "https://medium.com/feed/@stiflerxd"
README_PATH = "README.md"
START_TAG = "<!-- BLOG-POST-LIST:START -->"
END_TAG = "<!-- BLOG-POST-LIST:END -->"
MAX_POSTS = 3

def fetch_medium_feed():
    feed = feedparser.parse(FEED_URL)
    entries = feed.entries[:MAX_POSTS]
    lines = [START_TAG, ""]
    for entry in entries:
        title = entry.title
        link = entry.link
        pub_date = datetime(*entry.published_parsed[:3]).strftime("%Y-%m-%d")
        lines.append(f"- 🧠 [{title}]({link})  \n  <sub>Published: {pub_date}</sub>\n")
    lines.append("")
    lines.append(END_TAG)
    return "\n".join(lines)

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_blog_block = fetch_medium_feed()
    start_idx = content.find(START_TAG)
    end_idx = content.find(END_TAG) + len(END_TAG)

    if start_idx != -1 and end_idx != -1:
        updated_content = content[:start_idx] + new_blog_block + content[end_idx:]
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated_content)

if __name__ == "__main__":
    update_readme()
