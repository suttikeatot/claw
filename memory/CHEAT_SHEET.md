# 📜 SYSTEM CHEAT SHEET - OpenClaw Agent Skills
*(Last Updated: 2026-02-08 16:20 UTC)*

## 1. 🕵️‍♂️ Intel Analyst (นักวิเคราะห์ข่าวกรอง)
- **Trigger:** "Analyze", "Decode", "Intel", "สรุปข่าว"
- **Action:** เปลี่ยนโหมดจาก Developer เป็น Analyst เพื่อเจาะลึกบทความ
- **Input:** URL, Text, หรือ Tweet ID
- **Output:** Headline Rewrite, Core Thesis, Key Intel, Insight, Bottom Line (TH/EN)
- **File:** `skills/intel-analyst/SKILL.md`

## 2. 🌐 Safe Browsing (ท่องเว็บปลอดภัย)
- **Trigger:** "Browse <url>", "Scroll", "Pagination"
- **Protocol:** **READ** `memory/knowledge/Tools/browsing_standard.md` FIRST!
- **Rules:**
  1. Wait 3s after click
  2. Check Snapshot Diff (Loop Detection)
  3. Max 5 Pages (Hard Limit)
  4. Retry on Error (Once)
- **Command:** `agent-browser open <url>` (Do not use built-in `browser`)

## 3. 🌙 Nightly Build (งานกะดึก)
- **Trigger:** **AUTO** (Daily 21:00 UTC / 04:00 BKK)
- **Action:**
  1. Backup Config (`openclaw.json`, `.bashrc`)
  2. Clean Logs (>7 days)
  3. Refresh Knowledge Graph (`GRAPH.md`)
- **Manual Trigger:** "Run Nightly Build"
- **Script:** `scripts/nightly_routine.sh`

## 4. 🐦 Twitter Intelligence (สายสืบ X)
- **Trigger:**
  - "Check Bookmarks" -> Top 20 Latest
  - "Bird Read <ID>" -> Deep Dive Tweet/Thread
  - "Bird Search <Keyword>" -> Find News
- **Tool:** `bird` CLI (Config via `.bashrc`)
- **Limit:** Pagination unavailable (Top 20 only)

## 5. 🪵 Log Summarizer (สรุป Log)
- **Trigger:** "Summarize Logs", "Check Health"
- **Action:** Runs `python3 scripts/summarize_logs.py`
- **Output:** `memory/knowledge/tools/log_summary.md` (Markdown Report)
- **Use Case:** เมื่อเจ้านายอยากรู้ว่า "เมื่อวานกุ้งทำอะไรไปบ้าง?"

## 6. 🕸️ Knowledge Graph (แผนผังสมอง)
- **Trigger:** "Update Graph", "Visualize Memory"
- **Action:** Runs `python3 scripts/generate_knowledge_graph.py`
- **Output:** `memory/knowledge/GRAPH.md` (Mermaid Diagram)
- **Use Case:** ดูความเชื่อมโยงของความรู้ (AI <-> Crypto <-> Security)

## 7. 📦 ClawHub (Skill Manager)
- **Trigger:** "Install Skill <name>", "Search Skill <keyword>"
- **Command:** `openclaw skill search <keyword>` / `install <name>`
- **Condition:** Must verify skill safety (check `0xHuge List` first!)

## 8. 🏥 System Healthcheck (ตรวจสุขภาพ)
- **Trigger:** "Check System", "Audit Security"
- **Command:** `openclaw healthcheck run`
- **Output:** Security Report (Firewall, SSH, Ports)

---
**💡 Pro Tip:**
- **"PAUSE"** -> Update `WORKING.md` (Stop Task)
- **"RESUME"** -> Continue from `WORKING.md`
- **"/status"** -> Check Progress without stopping
