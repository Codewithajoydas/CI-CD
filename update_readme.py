from datetime import datetime

def update_readme():
    content = f"""# My Awesome Project 🚀

This project is automatically updated using GitHub Actions.

_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_

## Features
- Auto-update README using Python 🐍
- Auto Git push with GitHub Actions 🤖
"""

    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
