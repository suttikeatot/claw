# 🌙 Project: Nightly Build

**Status:** ✅ Active
**Schedule:** Daily at 03:00 BKK (20:00 UTC)
**Script:** `~/.openclaw/scripts/nightly-build.sh`

## 🎯 Objective
To perform autonomous maintenance and reporting while the user sleeps, ensuring the system is healthy and data is backed up.

## 🛠️ Components

### 1. Safety (Kill Switch)
- Checks for `~/.openclaw/stop.flag`
- If exists: **ABORT IMMEDIATELY**
- Prevents runaway scripts or crash loops.

### 2. Backup Config
- Calls `backup-config.sh`
- Targets: `openclaw.json`, `auth-profiles.json`, `jobs.json`
- Storage: `~/.openclaw/backups/`

### 3. System Health
- Checks Disk Usage (%)
- Checks Memory Usage (%)
- Logs warning if Disk > 90%

### 4. Cybersecurity Watchdog
- Calls `cyber-watchdog.sh`
- Scans Hacker News + Reddit Netsec
- Keywords: exploit, vulnerability, cve, zero-day
- Saves report to `memory/knowledge/security/`

### 5. Reporting
- Generates `morning_brief.md`
- Cron job at 08:00 BKK sends this briefing to the user via Telegram.

## 📜 History
- **2026-02-07:** Project initialized. Added Kill Switch and Watchdog.
