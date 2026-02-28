# WORKSPACE_INDEX - แผนที่ไฟล์ใน Workspace

ไฟล์นี้เป็น INDEX ว่าไฟล์ไหนอยู่ไหน ใช้ทำอะไร ค้นหาได้เร็ว

---

## 📁 Root Level (อ่านตามลำดับ)

| ไฟล์ | อ่านเมื่อไหร่ | หน้าที่ |
|------|-------------|---------|
| `AGENTS.md` | ทุกครั้ง | กฎการทำงานหลัก |
| `SOUL.md` | ทุกครั้ง | ตัวตนกุ้ง |
| `USER.md` | ทุกครั้ง | ข้อมูล Bank |
| `MEMORY.md` | Main session only | ความจำระยะยาว |
| `TOOLS.md` | ตอนใช้ tools | Local tool notes |
| `HEARTBEAT.md` | ตอน heartbeat | Checklist |

---

## 📁 memory/ - Raw Logs

**รูปแบบ:** `YYYY-MM-DD.md`  
**มีทั้งหมด:** ~25 ไฟล์ (Feb 2026)  
**อ่านเมื่อ:** ต้องการ context วันนั้น

---

## 📁 memory/knowledge/ - ความรู้เฉพาะทาง

| ไฟล์ | หัวข้อ | ใช้เมื่อไหร่ |
|------|--------|-------------|
| `GRAPH.md` | Knowledge graph structure | จัดการความรู้ |
| `openclaw-openrouter-official-models.md` | OpenClaw models | เลือก model |
| `browsing_standard.md` | Web browsing best practices | ตอน scraping |

---

## 📁 memory/projects/ - โปรเจคต่างๆ

| ไฟล์ | โปรเจค | สถานะ |
|------|--------|-------|
| `NightlyBuild.md` | Nightly build system | Active |

---

## 📁 skills/ - Custom Skills

| Skill | หน้าที่ |
|-------|---------|
| `context-budgeting/` | จัดการ context limit |
| `group-chat-etiquette/` | มารยาทกลุ่ม |
| `intel-analyst/` | วิเคราะห์ข่าวกรอง |
| `social-media-scraping/` | ดึงข้อมูล social |

---

## 🔍 Quick Find

**ถามเรื่อง:** | **ไปดูที่:**
---|---
Facebook login | `MEMORY.md` (ส่วน Facebook Login)
Web scraping | `skills/social-media-scraping/SKILL.md`
OpenClaw config | `backups/config/`
Daily logs | `memory/YYYY-MM-DD.md`
Context limit | `skills/context-budgeting/SKILL.md`

---

*Last updated: 2026-02-28*
