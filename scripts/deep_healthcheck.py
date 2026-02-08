import os
import re

# --- CONFIG ---
LOG_DIR = "memory"
OUTPUT_FILE = "memory/logs/context_health_report.md"

# --- LOGIC ---
def analyze_logs():
    print(f"🔍 Analyzing logs in: {LOG_DIR}...")
    
    context_history = []
    incidents = []
    
    # 1. Walk through daily memory files
    for file in sorted(os.listdir(LOG_DIR)):
        if re.match(r"\d{4}-\d{2}-\d{2}\.md", file):
            path = os.path.join(LOG_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
                # Extract Context Usage (This depends on if we logged it manually or via session_status)
                # Looking for patterns like "Context Usage: 217k/1.0m" or "Context: 97k"
                matches = re.findall(r"Context.*?:.*?(\d+)[kK]", content)
                for m in matches:
                    val = int(m)
                    context_history.append({"file": file, "value": val})

                # Extract Errors
                if "402 Payment Required" in content or "Billing Error" in content:
                    incidents.append(f"⚠️ {file}: API Billing Error (402)")
                if "429 Too Many Requests" in content:
                    incidents.append(f"⚠️ {file}: Rate Limit (429)")
                if "Context Reset" in content:
                    incidents.append(f"🔄 {file}: Context Reset Detected")

    # 2. Analyze Context Drops
    drops = []
    if len(context_history) > 1:
        for i in range(1, len(context_history)):
            prev = context_history[i-1]["value"]
            curr = context_history[i]["value"]
            
            # If drop > 20% (Abnormal)
            if curr < prev * 0.8:
                drops.append(f"📉 DROP: {prev}k -> {curr}k (-{prev-curr}k) in {context_history[i]['file']}")

    # 3. Generate Report
    report = ["# 🧠 Deep Context Healthcheck Report", f"**Generated:** {os.popen('date -u').read().strip()}", ""]
    
    report.append("## 🚨 Abnormal Incidents")
    if incidents:
        for inc in incidents: report.append(f"- {inc}")
    else:
        report.append("- ✅ No critical API errors found in logs.")

    report.append("\n## 📉 Context Drops (>20%)")
    if drops:
        for drop in drops: report.append(f"- {drop}")
    else:
        report.append("- ✅ Context usage is stable.")

    report.append("\n## 📊 Usage History (Sampled)")
    if context_history:
        report.append(f"- Start: {context_history[0]['value']}k")
        report.append(f"- Max: {max(c['value'] for c in context_history)}k")
        report.append(f"- Current: {context_history[-1]['value']}k")
    else:
        report.append("- (No context usage data found in logs)")

    # Write Output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    
    print(f"✅ Report generated at: {OUTPUT_FILE}")
    # Print summary to console
    print("\n".join(report))

if __name__ == "__main__":
    analyze_logs()
