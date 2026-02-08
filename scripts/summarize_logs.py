import os
import re
from datetime import datetime

LOG_DIR = os.path.expanduser("~/.openclaw/logs")
OUTPUT_FILE = os.path.expanduser("~/.openclaw/workspace/memory/knowledge/tools/log_summary.md")

def summarize_logs():
    summary = []
    summary.append(f"# Log Summary: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if not os.path.exists(LOG_DIR):
        summary.append("❌ Log directory not found.")
        return "\n".join(summary)

    for filename in os.listdir(LOG_DIR):
        if filename.endswith(".log"):
            filepath = os.path.join(LOG_DIR, filename)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    error_count = len(re.findall(r'ERROR|FAIL|EXCEPTION', content, re.IGNORECASE))
                    warn_count = len(re.findall(r'WARN|WARNING', content, re.IGNORECASE))
                    summary.append(f"- **{filename}**: {error_count} Errors, {warn_count} Warnings")
            except Exception as e:
                summary.append(f"- ⚠️ Error reading {filename}: {str(e)}")

    return "\n".join(summary)

if __name__ == "__main__":
    report = summarize_logs()
    print(report)
    with open(OUTPUT_FILE, "w") as f:
        f.write(report)
