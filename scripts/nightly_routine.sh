#!/bin/bash
# 🌙 THE NIGHTLY BUILD (Automated Maintenance Routine)
# Runs daily at 21:00 UTC (04:00 BKK)

LOG_FILE="memory/logs/nightly_build.log"
mkdir -p memory/logs

echo "=== 🌙 Starting Nightly Build: $(date) ===" >> $LOG_FILE

# 1. 🧹 CLEANUP: Remove old logs (>7 days)
echo "🧹 Cleaning old logs..." >> $LOG_FILE
find memory/logs -name "*.log" -mtime +7 -delete
echo "   Done." >> $LOG_FILE

# 2. 🧠 KNOWLEDGE: Refresh Graph
echo "🧠 Refreshing Knowledge Graph..." >> $LOG_FILE
python3 scripts/generate_knowledge_graph.py >> $LOG_FILE 2>&1
echo "   Done." >> $LOG_FILE

# 3. 🛡️ BACKUP: Config Files (Critical)
echo "🛡️ Backing up critical config..." >> $LOG_FILE
mkdir -p backups/config
cp ~/.openclaw/openclaw.json backups/config/openclaw_$(date +%F).json
cp ~/.bashrc backups/config/bashrc_$(date +%F).bak
echo "   Done." >> $LOG_FILE

# 4. 📰 INTEL: Fetch Morning Brief (Placeholder)
# (In future: call 'bird search' or RSS reader here)
echo "📰 Morning Brief: Pending Implementation" >> $LOG_FILE

# 5. ✅ FINISH
echo "=== ✅ Nightly Build Complete: $(date) ===" >> $LOG_FILE
echo "----------------------------------------" >> $LOG_FILE

# Notify OpenClaw (via working.md or session)
# echo "Nightly Build Done" > memory/last_nightly_status.txt
