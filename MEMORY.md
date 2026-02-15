# MEMORY.md - Long-Term Memory

## 📝 MEMORY PRACTICE

**จดระหว่างทาง ไม่รอ context เยอะ**
- ถ้ามีเรื่องสำคัญ → จดลง `memory/YYYY-MM-DD.md` ทันที
- ไม่รอ session จบ หรือ context 70-80%
- ระบบอาจ crash ตอน 20% ก็ได้ — ข้อมูลก่อนหน้าอาจหายหมด

## ☠️ SKILL TO AVOID: elite-longterm-memory

**Date:** 2026-02-06
**Status:** DO NOT USE

### What Happened:
- Installed skill ที่ใช้ LanceDB + Gemini batch embeddings
- Gemini batch jobs ติดค้างที่ status "UNKNOWN" แล้ววน loop
- Context overflow errors ซ้ำๆ
- Connection refused (LanceDB service ล่ม)
- ระบบ crash ต้อง reinstall OpenClaw ใหม่

### Lesson Learned:
- ❌ อย่าใช้ elite-longterm-memory
- ❌ ระวัง skills ที่ต้องใช้ external DB (LanceDB, etc.)
- ✅ ใช้ memory_search ที่มีอยู่แล้วก็พอ

## 🚨 CRITICAL FACEBOOK RESTRICTIONS

**Date:** 2026-02-01
**Status:** ABSOLUTE RULES - NEVER VIOLATE

### STRICT PROHIBITIONS:
1. **NO POSTING** - ห้าม post ข้อความ/รูป/วิดีโอเด็ดขาด
2. **NO MESSAGING** - ห้ามส่ง message หาใครทั้งสิ้น
3. **NO INTERACTIONS** - ห้ามกด like, comment, share, react
4. **READ-ONLY MODE** - อ่านอย่างเดียวเท่านั้น

### ALLOWED ACTIONS:
- ✅ อ่าน Saved posts
- ✅ Browse timeline เพื่อหาข่าว/โพสต์น่าสนใจ
- ✅ ดึงข้อมูล text จาก posts
- ✅ Summarize เนื้อหา

### CREDENTIALS (Sensitive - do not share):
- Email: dev.d.bos@gmail.com
- Purpose: Facebook login for content reading only
- 2FA: User will approve manually

### Login Process:
1. Attempt login with provided credentials
2. Wait for user to approve 2FA on their device
3. User will message "กดแล้ว" to proceed
4. Save cookies/session for future use

## 🔄 AUTOMATIC ERROR RECOVERY PROTOCOL

**Date:** 2026-02-02
**Applies to:** Facebook scraping sessions

### Kimi Rate Limit Error Handling:
**Error:** `Unknown model: kimi-coding/kim`

**Cause:** Kimi API rate limit → Provider in cooldown

**Automatic Recovery:**
1. ✅ Wait 10-30 seconds (do not ask user)
2. ✅ Retry operation automatically
3. ✅ If retry succeeds → Continue silently
4. ✅ If fails 3 times → Report "Rate limit, cooling down..." briefly
5. ✅ Resume work when ready

**DO NOT:**
- ❌ Ask user "what should I do?"
- ❌ Stop and wait for user input
- ❌ Interrupt workflow unnecessarily

**DO:**
- ✅ Work in batches of 10 posts
- ✅ Self-recover from errors
- ✅ Report only critical issues
- ✅ Keep working until context limit

### Workflow:
- Work in **batches of 10 posts**
- Commit git after each batch
- Update index.md after each batch
- Continue until context ~80% or rate limit persists

## 💾 DATA STORAGE OPTIONS (To Discuss)

Current ideas for storing summarized content:
1. Google Sheets (shared link with edit permissions)
2. Obsidian (local database)
3. Notion (API integration)

Need to evaluate best approach based on:
- Ease of access
- Formatting capabilities
- Automation potential

## 🔧 CONFIG BACKUP SYSTEM

**Date:** 2026-02-07
**Status:** ACTIVE - USE BEFORE RISKY CHANGES

### Backup Script Location:
```
~/.openclaw/scripts/backup-config.sh
```

### What Gets Backed Up:
| ไฟล์ | ความเสี่ยง |
|-----|-----------|
| `openclaw.json` | 🔴 Config หลัก |
| `auth-profiles.json` | 🔴 API keys, OAuth |
| `cron/jobs.json` | 🟡 Scheduled jobs |

### Backup Storage:
```
~/.openclaw/backups/
```

### Usage:
```bash
~/.openclaw/scripts/backup-config.sh [reason]
```

### MANDATORY: Run Before:
- ❗ Installing new skills
- ❗ Changing gateway config
- ❗ Adding new auth providers
- ❗ Any risky operation

### Auto-cleanup:
- Keeps last 50 backups
- ~150KB total storage

---

## 🌐 WEB BROWSING STANDARD (Verified 2026-02-09)

**Date:** 2026-02-09
**Status:** ACTIVE

### Rule:
- **ALWAYS use `agent-browser` (CLI tool)** for web interaction.
- **NEVER** use the built-in `browser` tool (it is unreliable/broken).
- **NEVER** use `web_fetch` for dynamic sites (React/SPA) like Facebook, Moltbook, Twitter.

### CRITICAL: Proper Session Cleanup (Updated 2026-02-09)

**⚠️ ต้อง SAVE STATE ก่อน CLOSE เสมอ — ไม่งั้นเกิด ZOMBIE PROCESSES**

**Correct Sequence:**
```bash
# 1. ทำงานเสร็จ → Save state ก่อน
agent-browser state save facebook-session.json

# 2. ค่อยปิด browser
agent-browser close

# 3. (Optional) ถ้าไม่ต้องการ state อีก → ลบไฟล์
rm facebook-session.json
```

**❌ Wrong (ทำให้เกิด zombie chrome กิน RAM):**
```bash
# เปิด browser → ทำงาน → หยุด/ปิดกลางคัน โดยไม่ close
# ผล: zombie processes ค้างกิน RAM ~500MB+
```

**Cleanup Zombie (เมื่อเกิดแล้ว):**
```bash
killall -9 chrome-headless-shell
```

### Usage:
- **Open:** `agent-browser open <url>`
- **View:** `agent-browser snapshot -i` (captures interactive elements + preview text)
- **Interact:** `agent-browser click @e1`, `agent-browser fill @e2 "text"`
- **Session:** `agent-browser state save/load <file>.json` (Critical for login persistence)

## 🐦 TWITTER / X INTELLIGENCE (Verified 2026-02-08)

**Tool:** `bird` (CLI) - `@steipete/bird`
**Config:** `~/.bashrc` (Env Vars: `AUTH_TOKEN`, `CT0`)

### 🧠 Logic: The "Bookmark Unpacker"
1.  **Detection:** If a Bookmarked Tweet appears **empty** or has **only a link** (e.g., `t.co/...`):
    - **DO NOT IGNORE IT.** It is likely a **Long Article** or **Valuable Thread**.
    - **Context Clues:** High-value author (e.g., `Nozz`, `Dan Koe`), related to Automation/AI.
2.  **Action:** IMMEDIATELY execute `bird read <Tweet_ID>`.
3.  **Result:** This extracts the **Full Text** (even if it's a long-form article) which is often "Gold".

### 💡 PRO TIPS for Moltbook (Infinite Scroll Fix):
1.  **Don't Rely on Scroll:** Infinite scroll often freezes or loops on cached content.
2.  **Force Refresh:** If stuck, `open` the URL again to clear DOM cache.
3.  **Switch Feeds:** Click "New", "Top", or specific Submolts (e.g., `m/general`) to force new content loading.
4.  **Read from List:** `snapshot -i` captures preview text in link titles (often enough for summary). Clicking into detail view may hide text if not interactive.

## 🚨 FILE SAFETY RULE (CRITICAL)

**Date:** 2026-02-07
**Status:** MANDATORY

### The Mistake:
- Overwrote `MEMORY.md` with only partial content (lost previous context).
- Reason: Used `write` blindly without reading the full file first.

### The Rule:
1.  **NEVER use `write` on critical files** (MEMORY.md, AGENTS.md) unless you have read the ENTIRE file content in the same turn.
2.  **PREFER `edit` (String Replace)** for small updates/append.
3.  **ALWAYS Check:** If overwriting, ensure the `content` payload includes EVERYTHING (old + new).

---

## 🌏 TIMEZONE CONFIGURATION

**Date:** 2026-02-12
**Status:** ACTIVE

### Bangkok Timezone (UTC+7) — Default Output

**Rule:** แสดงเวลาทั้งหมดเป็น **Asia/Bangkok (UTC+7)** ในการคุยกับ user

**การใช้งาน:**
- แปลง timestamp UTC → Bangkok time ก่อนแสดงผล
- ระบุชื่อ timezone ชัดเจน (เช่น "07:48 น. (กรุงเทพ)")
- ใช้รูปแบบ 24 ชั่วโมง ตามความนิยมในไทย

**ตัวอย่าง:**
- UTC: `2026-02-12 00:48:00 UTC`
- Bangkok: `2026-02-12 07:48 น. (กรุงเทพ UTC+7)`

**หมายเหตุ:** ภายในระบบยังเก็บข้อมูลเป็น UTC ตามมาตรฐาน แต่แสดงผลให้ user เป็นเวลาไทยเสมอ
