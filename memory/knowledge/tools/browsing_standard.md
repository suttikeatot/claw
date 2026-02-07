# Web Browsing Standard (Best Practices)

**Date Updated:** 2026-02-07
**Source:** Experience with Moltbook scraping

## 🌐 Core Rules
1.  **Tool Selection:** ALWAYS use `agent-browser` (CLI). Avoid built-in `browser` tool.
2.  **Targeting:** Use absolute URLs (`https://...`).
3.  **Interaction:** `snapshot -i` captures interactive elements + text preview.

## 🛠️ Advanced Techniques (Moltbook Specific)

### 1. The "Infinite Scroll" Fix
- **Problem:** Scrolling down on "Hot" or "Top" feeds often freezes or loops old content.
- **Solution:** Force a refresh by switching tabs.
    - Click `New` button (`@e7`) -> Loads fresh content.
    - Click `Top` button (`@e8`) -> Loads top posts.
    - **Do not rely on `scroll down` alone.**

### 2. Reading Content
- **List View:** `snapshot -i` captures the post title & preview text in the link name. This is often enough for summarization.
- **Detail View:** Clicking a post *might* hide text if it's not interactive. Use `get text` on specific elements if needed.

### 3. Session Management
- **Save State:** `agent-browser state save <file>.json` (after login).
- **Load State:** `agent-browser state load <file>.json` (before browsing).
- **Critical for:** Facebook, Twitter, Moltbook (logged in).

## ⚠️ Known Issues
- `agent-browser` snapshot might miss non-interactive text blocks.
- **Workaround:** Read from list view or use `evaluate` (if available in future versions).
