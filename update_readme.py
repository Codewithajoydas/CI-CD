from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

def update_readme():
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    content = f"""# My Awesome Project 🚀

This project is automatically updated using GitHub Actions.

_Last updated: {ist_time.strftime('%Y-%m-%d %H:%M:%S')} IST_

## Features
- Auto-update README using Python 🐍
- Auto Git push with GitHub Actions 🤖
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
