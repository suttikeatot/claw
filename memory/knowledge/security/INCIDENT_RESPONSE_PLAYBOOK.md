# 🛡️ SECURITY RESPONSE PLAYBOOK
**For:** OpenClaw Agent Operations  
**Version:** 1.0  
**Date:** 2026-02-10  
**Classification:** INTERNAL

---

## 🚨 INCIDENT RESPONSE PROCEDURES

### IR-001: Agent Compromise Suspected
**Symptoms:**
- Unexpected tool calls
- Messages ที่ไม่ใช่ style ของ Agent
- Network connections ผิดปกติ
- File modifications โดยไม่มีคำสั่ง

**Immediate Actions (First 5 minutes):**
```bash
1. STOP all cron jobs
   openclaw cron list  # ดูว่ามีอะไรรันอยู่
   # หยุดทั้งหมดถ้าจำเป็น

2. CHECK recent activity
   cd ~/.openclaw/workspace
   git status  # ดูไฟล์ที่เปลี่ยน
   git diff HEAD~5  # ดู 5 commits ล่าสุด

3. ISOLATE session
   # ไม่ต้อง kill ทันที — เก็บ evidence ก่อน
   # แต่หยุดรับคำสั่งใหม่
```

**Investigation (5-30 minutes):**
```bash
# ตรวจสอบ processes
ps aux --sort=-%cpu | head -20
ps aux --sort=-%mem | head -20

# ตรวจสอบ network connections
netstat -tulpn | grep ESTABLISHED

# ตรวจสอบไฟล์ที่ถูกแก้ไขล่าสุด
find ~/.openclaw/workspace -type f -mtime -1 -ls

# ตรวจสอบ logs
tail -100 ~/.openclaw/logs/gateway.log
```

**Recovery (30+ minutes):**
```bash
# 1. Backup evidence
mkdir -p ~/incident-$(date +%Y%m%d)
cp -r ~/.openclaw/logs ~/incident-$(date +%Y%m%d)/
cp -r ~/.openclaw/workspace/memory ~/incident-$(date +%Y%m%d)/

# 2. Restore from last known good state
git log --oneline -10  # หา commit ที่ปลอดภัย
git reset --hard <safe-commit-hash>

# 3. Rotate all credentials
openclaw auth rotate --all

# 4. Restart gateway
openclaw gateway restart
```

---

### IR-002: Context Overflow Attack (DoS)
**Symptoms:**
- Context usage พุ่งไป 80%+ ในเวลาสั้น
- Agent ตอบช้าหรือ error
- "Context truncated" warnings

**Immediate Response:**
```bash
1. CREATE emergency handoff
   # กุ้งจะทำอัตโนมัติเมื่อเห็นสัญญาณ
   cat > memory/HANDOFF_EMERGENCY.md << 'EOF'
   # Emergency Handoff
   # Time: $(date)
   # Trigger: Context Overflow Attack
   # Next Action: [ผู้รับต้องตัดสินใจ]
   EOF

2. COMMIT immediately
   git add -A && git commit -m "EMERGENCY: Context overflow protection"
   git push

3. SWITCH to minimal model
   /openclaw model kimi-coding/k2p5  # ใช้ model ที่เร็วที่สุด
```

**Prevention:**
```bash
# Implement output truncation
# ใน TOOLS.md เพิ่ม:
MAX_EXEC_OUTPUT=10000  # characters
TRUNCATION_MESSAGE="[Output truncated due to size]"
```

---

### IR-003: Malicious Skill Installation
**Symptoms:**
- ติดตั้ง skill ใหม่แล้วมีพฤติกรรมแปลก
- Network calls ที่ไม่คาดคิด
- File system access นอกเหนือ scope

**Response:**
```bash
1. IDENTIFY skill ที่ต้องสงสัย
   ls -la ~/.openclaw/skills/
   # ดูว่าติดตั้งอะไรไปบ้างล่าสุด

2. QUARANTINE
   mv ~/.openclaw/skills/<suspicious-skill> \
      ~/.openclaw/quarantine/

3. AUDIT code (ถ้ายังไม่ลบ)
   cat ~/.openclaw/quarantine/<skill>/SKILL.md
   cat ~/.openclaw/quarantine/<skill>/index.js
   # ดูว่ามี network calls, file access ผิดปกติไหม

4. SCAN for persistence
   grep -r "cron\|systemctl\|launchctl" ~/.openclaw/
   # ตรวจหา persistence mechanisms
```

---

### IR-004: API Key Leakage
**Symptoms:**
- Unexpected API usage charges
- มีคนอื่นใช้ API key ของเรา
- Logs แสดง requests ที่เราไม่ได้สั่ง

**Response:**
```bash
1. REVOKE ทันที (ถ้าเป็นไปได้)
   # Kimi: เข้าไป revoke ที่ console
   # Telegram: BotFather → /revoke
   # Discord: Developer Portal

2. ROTATE
   openclaw auth remove <provider>
   openclaw auth add <provider> --new-key

3. AUDIT usage
   # ตรวจสอบ logs ย้อนหลัง
   # ดูว่ามี requests จาก IP ไหนบ้าง
```

---

## 🔍 FORENSICS CHECKLIST

### Log Analysis
- [ ] Gateway logs (`~/.openclaw/logs/`)
- [ ] Git history (`git log --all --oneline --graph`)
- [ ] System logs (`journalctl -u openclaw`)
- [ ] Shell history (`history | tail -100`)

### File Integrity
- [ ] Check SOUL.md (ถูกแก้ไขหรือไม่?)
- [ ] Check MEMORY.md (มีข้อมูลผิดปกติไหม?)
- [ ] Check AGENTS.md (ถูก tamper หรือไม่?)
- [ ] Verify all skill files

### Network Analysis
- [ ] Active connections (`netstat -an`)
- [ ] Recent connections (`ss -t`)
- [ ] DNS queries (`cat /var/log/syslog | grep DNS`)

---

## 🛠️ HARDENING CHECKLIST

### Daily
- [ ] ตรวจสอบ cron job status
- [ ] Verify last backup success
- [ ] Check context health
- [ ] Monitor disk space

### Weekly
- [ ] Rotate API keys (ถ้าใช้งานหนัก)
- [ ] Review installed skills
- [ ] Audit git commits
- [ ] Check for zombie processes

### Monthly
- [ ] Full system backup test (restore)
- [ ] Review access logs
- [ ] Update threat intelligence
- [ ] Security posture assessment

---

## 📞 ESCALATION CONTACTS

| Issue | Contact | Method |
|-------|---------|--------|
| Critical compromise | เจ้านายแบงค์ | Telegram |
| API issues | Provider support | Email/Console |
| OpenClaw bugs | OpenClaw Discord | GitHub Issues |
| Infrastructure | AWS Support | Console |

---

**Last Updated:** 2026-02-10  
**Next Review:** 2026-03-10  
**Owner:** กุ้ง Security Team
