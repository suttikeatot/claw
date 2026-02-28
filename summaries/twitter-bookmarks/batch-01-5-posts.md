# Twitter Bookmarks Summary - Batch 1 (5 Posts)
**Date:** 2026-02-28  
**Source:** @Hartdrawss, @cpkcpk3, @0xairdropfarmer, @mkbijaksana, @GithubProjects

---

## 001 - Vibe Coding 2.0: 18 Rules to be the Top 1% builder
**Author:** @Hartdrawss (Harshil Tomar)  
**Date:** Tue Feb 24, 2026  
**Tags:** #vibe-coding #mvp #productivity #startup

### 📌 HEADLINE REWRITE
> 18 กฎสำหรับการสร้าง MVP แบบมือโปร: อย่าสร้างเอง ให้ใช้ ecosystem ที่มีอยู่

### 🧠 CORE THESIS
Founders ใช้เวลา 3 เดือนทำสิ่งที่ควรใช้ 3 สัปดาห์ เพราะเลือกสร้างทุกอย่างเองแทนที่จะใช้ tools สำเร็จรูป กฎทองคือ "รู้ว่าอะไรไม่ควรสร้าง"

### 🔍 KEY INTELLIGENCE POINTS
- **[DO #1-3]** — Auth ใช้ Clerk/Supabase, UI ใช้ Tailwind+shadcn, State ใช้ Zustand
- **[DO #4-6]** — API ใช้ tRPC/Server Actions, Deploy ใช้ Vercel, DB ใช้ Prisma+Managed Postgres
- **[DO #8-9]** — Payment ใช้ Stripe (ไม่มีทางสร้างเอง), Error tracking ใช้ Sentry ตั้งแต่วันแรก
- **[DON'T #1]** — อย่าสร้าง Auth เอง = #1 time killer
- **[DON'T #5]** — อย่า deploy มือ (human error + ไม่ scale)

### 💭 ANALYSIS & THINKING
- **What's NOT said:** ไม่มี discussion เรื่อง cost ของ tools พวกนี้ (Clerk, Stripe มีค่าใช้จ่าย)
- **Assumption:** ผู้อ่านใช้ React/Node ecosystem เป็นหลัก (ไม่ครอบคลุม Python/Go/Rust)
- **Who benefits:** Indie hackers, solo founders, agency ที่ต้อง ship fast
- **Underlying trend:** "Buy vs Build" กลับมาเป็นที่นิยม หลังจากปี 2020-2022 ที่ dev ชอบ reinvent wheel

### 💡 NON-OBVIOUS INSIGHTS
- **Second-order effect:** ถ้าทุกคนใช้ tech stack เหมือนกัน → differentiation อยู่ที่ product/UX ไม่ใช่ tech
- **Contrarian angle:** การ "ไม่สร้าง" ต้องใช้ประสบการณ์สูงกว่าการสร้างเอง (รู้ว่าอะไร reliable)

### ⚡ BOTTOM LINE
> Ship fast ด้วยการใช้ ecosystem ที่มีอยู่ อย่าสร้างเองทุกอย่าง → time saved ไปลงที่ feature ที่ user จริงๆ ต้องการ

---

## 002 - Claude Code Project Management Technique
**Author:** @cpkcpk3 (chompk.eth)  
**Date:** Fri Feb 27, 2026  
**Tags:** #claude-code #ai-coding #project-management #workflow

### 📌 HEADLINE REWRITE
> ระบบจัดการโปรเจคขนาดใหญ่ด้วย Claude Code: แยก subagent เป็น Project Manager

### 🧠 CORE THESIS
งานใหญ่ต้องแตกเป็น task ย่อยละเอียด โดยใช้ Claude Code เป็น Project Manager ผ่านการสร้าง structure: `.prompts/init.md` + `.breakdown/` + `CLAUDE.md`

### 🔍 KEY INTELLIGENCE POINTS
- **[Step 1]** — เขียน design requirement, schema, architecture ใน `.prompts/init.md`
- **[Step 2]** — สร้าง `.breakdown/` เป็น kanban board แบ่ง epic/task
- **[Step 3]** — ใช้ CLAUDE.md template กำหนด role ให้ claude
- **[Step 4]** — ให้ claude แตก task ก่อน (ยังไม่ code) พร้อม planning
- **[Step 5]** — ทำทีละ task, claude จะ update status เป็น [IN PROGRESS] → [DONE]
- **[Critical]** — ให้ claude เขียน unittest ทุก card

### 💭 ANALYSIS & THINKING
- **What's NOT said:** ไม่ได้บอกว่า technique นี้ใช้เวลา setup นานแค่ไหน
- **Assumption:** โปรเจคมีขนาดใหญ่พอที่จะต้อง breakdown (ไม่เหมาะกับ script ง่ายๆ)
- **Comparison:** คล้ายกับ TDD (Test-Driven Development) แต่ใช้ AI ช่วย plan

### 💡 NON-OBVIOUS INSIGHTS
- **Pattern:** ใช้ ".md files as API" สื่อสารกับ AI (prompts, breakdown, status)
- **Second-order:** ถ้า claude code มี memory/persistence ดีขึ้น → technique นี้อาจล้าสมัย

### ⚡ BOTTOM LINE
> แยกโปรเจคเป็น epic/task ใน markdown files แล้วให้ claude code เป็น PM คอย track → ตรวจสอบงานได้ง่ายขึ้น

---

## 003 - Second Brain for Crypto with Obsidian
**Author:** @0xairdropfarmer (👩🌾0xAirdropFarmer)  
**Date:** Thu Feb 26, 2026  
**Tags:** #second-brain #obsidian #crypto #knowledge-management #para-method

### 📌 HEADLINE REWRITE
> ระบบจัดการความรู้ Crypto ด้วย Obsidian + PARA Method: ไม่ลืม research อีกต่อไป

### 🧠 CORE THESIS
ข้อมูล crypto เยอะมาก (protocol ใหม่, airdrop criteria, trading pattern) ถ้าไม่มีระบบ = พลาดโอกาส Second Brain ด้วย Obsidian + PARA Method ช่วยจัดระเบียบ

### 🔍 KEY INTELLIGENCE POINTS
- **[Why Obsidian?]** — Local files (ไม่กลัว cloud ล่ม), Markdown, Backlinks, Graph View, Free
- **[PARA Method]** — Projects (มี deadline), Areas (ดูแลต่อเนื่อง), Resources (ความรู้), Archive (เสร็จแล้ว), Inbox (ไอเดีย)
- **[Crypto Adaptation]** — แยกเป็น Projects/Airdrop-Campaign, Areas/Trading, Resources/Protocols
- **[Backlinks]] — เชื่อมโน้ตเป็น web เช่น [[Arbitrum]] → [[L2 Scaling]]

### 💭 ANALYSIS & THINKING
- **What's NOT said:** ไม่ได้เปรียบเทียบกับ Notion/Affine/Logseq ว่าทำไม Obsidian ดีกว่า
- **Assumption:** ผู้ใช้ comfortable กับ Markdown + local-first
- **Underlying trend:** "Personal Knowledge Management" (PKM) กลับมาฮิต หลัง AI ทำให้ information overload หนักขึ้น

### 💡 NON-OBVIOUS INSIGHTS
- **Second-order:** ถ้า AI มี memory/retrieval ดีขึ้น → ทำไมต้องจดเอง? (แต่ตอนนี้ยังต้อง)
- **Pattern:** PARA Method เป็น framework ที่ใช้ได้ข้าม domain (ไม่ใช่แค่ crypto)

### ⚡ BOTTOM LINE
> ใช้ Obsidian + PARA Method จัดข้อมูล crypto เป็นระบบ → ไม่ลืม research, หาข้อมูลเก่าเจอ, สร้าง web ความรู้เชื่อมโยง

---

## 004 - AI Agents Beginner Roadmap
**Author:** @mkbijaksana (Kurnia Bijaksana)  
**Date:** Tue Feb 24, 2026  
**Tags:** #ai-agents #roadmap #beginner #2026

### 📌 HEADLINE REWRITE
> AI Agents 101: Roadmap สำหรับมือใหม่ที่อยากเริ่มต้นปี 2026

### 🧠 CORE THESIS
AI Agents เป็น trend ที่จะ dominate ปี 2026 ผู้ที่เข้าใจ early จะได้ competitive advantage (ทั้ง career และ wealth)

### 🔍 KEY INTELLIGENCE POINTS
- **[Claim]** — "AI Agents can make you rich" (ไม่มีรายละเอียดว่ายังไง)
- **[Content]** — QT ไป roadmap ละเอียด (ไม่ได้แสดงใน bookmark)
- **[Engagement]** — 1,884 likes, 255 retweets (high interest)

### 💭 ANALYSIS & THINKING
- **What's NOT said:** ไม่มี detail ใน tweet นี้ (เป็น teaser ให้ click QT)
- **Assumption:** "Rich" หมายถึงอะไร? (career, investment, build product?)
- **Hype cycle:** เป็น typical "AI will make you rich" content ที่มาก่อน bubble

### 💡 NON-OBVIOUS INSIGHTS
- **Pattern:** การใช้ "Study this" + high engagement = content ที่ได้รับความสนใจ แต่อาจเป็น shallow signal

### ⚡ BOTTOM LINE
> AI Agents เป็น trend สำคัญปี 2026 แต่ tweet นี้เป็น teaser มากกว่า substance (ต้อง follow QT ถ้าอยากได้ roadmap)

---

## 005 - OpenClaw Use Cases Collection
**Author:** @GithubProjects (GitHub Projects Community)  
**Date:** Thu Feb 26, 2026  
**Tags:** #openclaw #automation #use-cases #github

### 📌 HEADLINE REWRITE
> รวม use cases ของ OpenClaw สำหรับ automation ชีวิตประจำวัน

### 🧠 CORE THESIS
GitHub Projects Community สร้าง collection ของ OpenClaw use cases เพื่อช่วยให้ชีวิตง่ายขึ้น

### 🔍 KEY INTELLIGENCE POINTS
- **[Source]** — GitHub Projects Community (official GitHub account?)
- **[Format]** — Image/infographic (ไม่มี text detail ใน tweet)
- **[Topic]** — OpenClaw use cases for daily automation

### 💭 ANALYSIS & THINKING
- **What's NOT said:** ไม่มี detail ว่า use cases อะไรบ้าง (ต้องดูรูป)
- **Significance:** OpenClaw เริ่มมี community สร้าง content รอบตัว → validation ว่า tool กำลังได้รับความสนใจ

### ⚡ BOTTOM LINE
> OpenClaw มี community สร้าง use case collections → สัญญาณว่า tool กำลังได้รับ adoption

---

*End of Batch 1 (5/10 posts)*
