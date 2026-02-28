#!/bin/bash
# 🦐 EMERGENCY RESTORE - ถ้ากุ้งพังทั้งระบบ
# ใช้เมื่อต้อง restore OpenClaw ใหม่ทั้งหมด

set -e

echo "=================================="
echo "  OpenClaw Emergency Restore"
echo "=================================="
echo ""

# 1. Check prerequisites
if ! command -v git &> /dev/null; then
    echo "❌ git not installed"
    exit 1
fi

if [ -z "$OPENCLAW_WORKSPACE_GIT" ]; then
    echo "⚠️  Set your workspace git URL:"
    echo "   export OPENCLAW_WORKSPACE_GIT='git@github.com:user/repo.git'"
    exit 1
fi

# 2. Stop gateway if running
openclaw gateway stop 2>/dev/null || true

# 3. Backup current (ถ้ามี)
if [ -d "$HOME/.openclaw" ]; then
    BACKUP_TS=$(date +"%Y%m%d_%H%M%S")
    mv "$HOME/.openclaw" "$HOME/.openclaw.broken.$BACKUP_TS"
    echo "📦 Backed up broken install to ~/.openclaw.broken.$BACKUP_TS"
fi

# 4. Reinstall OpenClaw (ถ้าลบทั้งหมด)
# npm install -g openclaw  # ถ้าต้อง reinstall

# 5. Restore workspace from git
echo ""
echo "📥 Restoring workspace from git..."
mkdir -p "$HOME/.openclaw"
git clone "$OPENCLAW_WORKSPACE_GIT" "$HOME/.openclaw/workspace"

# 6. Restore configs from backup (ถ้ามี)
if [ -d "$HOME/.openclaw.backups" ]; then
    echo ""
    echo "🔧 Restoring configs from backup..."
    # ใช้ restore-config.sh ถ้ามี
    if [ -f "$HOME/.openclaw/workspace/scripts/restore-config.sh" ]; then
        bash "$HOME/.openclaw/workspace/scripts/restore-config.sh"
    fi
fi

# 7. Reinstall skills (จาก skills-list)
if [ -f "$HOME/.openclaw/backups/skills-list_"*.txt ]; then
    echo ""
    echo "📦 Reinstalling skills..."
    for skill in $(cat "$HOME/.openclaw/backups/skills-list_"*.txt | head -1); do
        openclaw skills install "$skill" 2>/dev/null || echo "  ⚠️  Failed to install $skill"
    done
fi

# 8. Rebuild memory index
if [ -d "$HOME/.openclaw/workspace/memory" ]; then
    echo ""
    echo "🧠 Rebuilding memory index..."
    export GOOGLE_API_KEY="${GOOGLE_API_KEY:-$(grep -o 'AIza[0-9A-Za-z_-]*' "$HOME/.openclaw/openclaw.json" | head -1)}"
    openclaw memory index --force 2>/dev/null || echo "  ⚠️  Memory index failed (may need API key)"
fi

# 9. Start gateway
echo ""
echo "🚀 Starting gateway..."
openclaw gateway start

echo ""
echo "=================================="
echo "  ✅ Restore Complete!"
echo "=================================="
echo ""
echo "Check status: openclaw status"
echo "Test agent:   openclaw sessions list"
