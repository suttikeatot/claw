import time
import hashlib
import random

# --- 1. The Mock Website (Simulating Bad Behavior) ---
class MockSite:
    def __init__(self):
        self.current_page = 1
        self.is_stuck = False  # Simulate infinite loop state
        self.error_mode = False # Simulate network error

    def load_page(self):
        """Simulates loading a page content."""
        print(f"🌐 [MockSite] Loading Page {self.current_page}...", end=" ")
        
        # Simulate Network Delay (Rule 1: Wait Strategy)
        time.sleep(0.5) 

        # Simulate Error (Rule 4: Smart Error Handling)
        if self.current_page == 4 and not self.error_mode:
            self.error_mode = True # Trigger error once
            print("❌ 500 Internal Server Error!")
            raise Exception("Timeout / Network Error")
        
        # Simulate Loop (Rule 2: State Check)
        if self.current_page >= 6:
            self.is_stuck = True # Content stops changing after page 6
            print("🔄 (Content Loop - Same as Page 5)")
            return f"<html>Page 5 Content (End of List)</html>"

        print("✅ OK")
        return f"<html>Page {self.current_page} Content: Unique Data {random.randint(1000,9999)}</html>"

    def next_page(self):
        """Simulates clicking 'Next' button."""
        if not self.is_stuck:
            self.current_page += 1

# --- 2. The Agent Logic (Implementing 4 Protocols) ---
class SafeBrowserAgent:
    def __init__(self, site):
        self.site = site
        self.last_snapshot_hash = None
        self.page_count = 0
        self.retry_count = 0
        
        # ⚙️ CONFIG (The Rules)
        self.MAX_PAGES = 8          # Rule 3: Hard Limit
        self.WAIT_TIME = 1.0        # Rule 1: Explicit Wait
        self.MAX_RETRIES = 1        # Rule 4: Retry Limit

    def run(self):
        print("\n🚀 [Agent] Starting Safe Browsing Mission...")
        
        while self.page_count < self.MAX_PAGES:
            self.page_count += 1
            print(f"\n--- Step {self.page_count} ---")

            # Rule 4: Smart Error Handling
            try:
                content = self.site.load_page()
                self.retry_count = 0 # Reset retry on success
            except Exception as e:
                print(f"⚠️ [Agent] Caught Error: {e}")
                if self.retry_count < self.MAX_RETRIES:
                    self.retry_count += 1
                    print(f"🔄 [Agent] Retrying ({self.retry_count}/{self.MAX_RETRIES})...")
                    time.sleep(1) # Backoff wait
                    self.page_count -= 1 # Don't count this step
                    continue
                else:
                    print("🛑 [Agent] ABORT: Too many errors! (Rule 4)")
                    break

            # Rule 2: State Check (Differential Snapshot)
            current_hash = hashlib.md5(content.encode()).hexdigest()
            print(f"📸 [Agent] Snapshot Hash: {current_hash[:8]}")

            if self.last_snapshot_hash == current_hash:
                print("🛑 [Agent] ABORT: Loop Detected! Content didn't change. (Rule 2)")
                break
            
            self.last_snapshot_hash = current_hash

            # Rule 1: The Wait Strategy
            print(f"⏳ [Agent] Waiting {self.WAIT_TIME}s for stability... (Rule 1)")
            time.sleep(self.WAIT_TIME)

            # Proceed to next page
            self.site.next_page()

        # Rule 3: Hard Limit Check
        if self.page_count >= self.MAX_PAGES:
            print("\n🛑 [Agent] STOP: Hard Limit Reached (Max 8 Pages). (Rule 3)")
        
        print("\n🏁 [Agent] Mission Complete.")

# --- 3. Execution ---
if __name__ == "__main__":
    mock_site = MockSite()
    agent = SafeBrowserAgent(mock_site)
    agent.run()
