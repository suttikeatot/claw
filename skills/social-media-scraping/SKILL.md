# SKILL.md - Social Media Scraping

## Description
Best practices for scraping content from social media platforms with infinite scroll.
Use when task involves browsing Facebook, Twitter/X, Instagram, Reddit, TikTok, or Moltbook.

## When to Load
- Task involves "scrape", "browse", "collect" from social media
- Platforms: Facebook, Twitter/X, Instagram, Reddit, TikTok, Moltbook
- URL contains: facebook.com, twitter.com, x.com, instagram.com, reddit.com, tiktok.com

## Universal Rules for Infinite Scroll

### The Pattern
1. **Scroll small amounts** — 800-1500 pixels at a time
2. **WAIT for delay** — 3-6 seconds between scrolls for lazy loading
3. **Scroll continuously** — Repeat until no new content loads
4. **Area to scroll:** Main content area (feed/timeline) — NOT sidebar

### Why This Works
- Social media uses JavaScript lazy loading
- Content loads only when user scrolls near bottom
- Rushing scrolls without delay = JS doesn't trigger = no new content
- Patience is key: Scroll → Wait → Check → Repeat

### Example Pattern
```bash
agent-browser scroll down 1000
agent-browser wait 5000
# Check for new content
# Repeat until count stops increasing
```

## Platform-Specific Tips

### Facebook
- Initial load: ~9 posts
- After proper scrolling: 18, 30, 40, 50, 60+ posts
- Scroll area: "ทั้งหมด" (main content), not sidebar

### Moltbook
- **Don't Rely on Scroll:** Infinite scroll often freezes or loops on cached content
- **Force Refresh:** If stuck, `open` the URL again to clear DOM cache
- **Switch Feeds:** Click "New", "Top", or specific Submolts (e.g., `m/general`) to force new content loading
- **Read from List:** `snapshot -i` captures preview text in link titles (often enough for summary). Clicking into detail view may hide text if not interactive

### Twitter/X
- Use `bird` CLI tool for bookmarks (@steipete/bird)
- Config in `~/.bashrc`: `AUTH_TOKEN`, `CT0`
- **Bookmark Unpacker:** If bookmarked tweet appears empty or has only a link (`t.co/...`), it's likely a Long Article or Valuable Thread — execute `bird read <Tweet_ID>` immediately

## Pro Tips

### Infinite Scroll Fix (All Platforms)
1. Don't rely on scroll alone
2. Force refresh if stuck
3. Switch feeds to load new content
4. Read from list view before clicking into detail

## ⚠️ CRITICAL: Facebook Restrictions

**Date:** 2026-02-01
**Status:** ABSOLUTE RULES - NEVER VIOLATE

### STRICT PROHIBITIONS:
1. **NO POSTING** — ห้าม post ข้อความ/รูป/วิดีโอเด็ดขาด
2. **NO MESSAGING** — ห้ามส่ง message หาใครทั้งสิ้น
3. **NO INTERACTIONS** — ห้ามกด like, comment, share, react
4. **READ-ONLY MODE** — อ่านอย่างเดียวเท่านั้น

### ALLOWED ACTIONS:
- ✅ อ่าน Saved posts
- ✅ Browse timeline เพื่อหาข่าว/โพสต์น่าสนใจ
- ✅ ดึงข้อมูล text จาก posts
- ✅ Summarize เนื้อหา

## Workflow
- Work in **batches of 10 posts**
- Commit git after each batch
- Update index.md after each batch
- Continue until context ~80% or rate limit persists
