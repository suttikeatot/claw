# HEARTBEAT.md

## 🎯 Purpose
Heartbeat runs every 30 min to check for tasks that need attention. Don't just reply HEARTBEAT_OK — use it productively.

## When to Use Heartbeat vs Cron
- **Heartbeat:** Multiple checks batched together, needs conversational context, timing can drift (~30 min OK)
- **Cron:** Exact timing matters, task needs isolation, one-shot reminders

## Quick Checks (rotate through these)
- **Emails** — Any urgent unread?
- **Calendar** — Events in next 24-48h?
- **GitHub** — Any backup issues?
- **System** — Disk/memory OK?

## Stay Silent When
- Late night (23:00-08:00) unless urgent
- Human clearly busy
- Nothing new since last check
- Just checked <30 min ago
- Everything is normal and quiet (no need to reply)

## Proactive Work
- Read/organize memory files
- Check project status (git)
- Update documentation
- Commit pending changes

## Memory Maintenance
Every few days, review recent `memory/YYYY-MM-DD.md` files and update `MEMORY.md` with distilled learnings.

---
*Keep this checklist small to limit token burn.*
