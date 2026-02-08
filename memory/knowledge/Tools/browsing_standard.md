# 🌐 Web Browsing Standard Operating Procedure (SOP)

**Effective Date:** 2026-02-08
**Objective:** Prevent infinite loops, excessive token usage, and bot detection during deep browsing tasks.

---

## 🛑 The "Anti-Loop" Protocol (4 Rules)

### 1. The Wait Strategy (Explicit Wait)
- **Problem:** Clicking "Next" too fast on slow-loading sites causes re-clicks.
- **Rule:** ALWAYS wait after interaction.
- **Command:** `process wait 3000` (or `sleep 3`) after every `click` or `scroll`.
- **Reason:** Allow DOM to settle and content to load.

### 2. State Check (Differential Snapshot)
- **Problem:** Clicking a disabled/broken button repeatedly.
- **Rule:** Compare state before and after action.
- **Logic:**
  1. Take Snapshot A.
  2. Perform Action (Click/Scroll).
  3. Take Snapshot B.
  4. **IF (A == B) THEN ABORT.** (Stop immediately, report "Stuck").

### 3. Hard Limit Counter (Quota)
- **Problem:** Infinite scroll is truly infinite.
- **Rule:** Set a strict maximum for pagination/scrolls.
- **Default:** Max **5 pages** or **5 scrolls** per session.
- **Action:** If reached limit, STOP and ask user: "Continue?"

### 4. Smart Error Handling (Retry vs. Abort)
- **Problem:** Element not found or Timeout.
- **Rule:**
  - **1st Error:** Retry once (maybe network glitch).
  - **2nd Error:** **REFRESH PAGE** (`agent-browser open <url>`) or **CLOSE TAB**.
  - **Do NOT** retry endlessly in a loop.

---

## 🛠️ Tool Preference
1. **`agent-browser` (CLI):** Preferred for simple browsing/scraping.
2. **`bird` (CLI):** Preferred for Twitter/X specific tasks (safer).
3. **`browser` (Built-in):** Avoid if possible (often flaky).

## 📝 Pre-Flight Checklist
- [ ] Read this file (`read memory/knowledge/Tools/browsing_standard.md`)
- [ ] Set `max_pages` or `max_scrolls` variable.
- [ ] Verify URL and expected content type.
