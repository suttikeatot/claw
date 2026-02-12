# OpenRouter Models ที่ใช้กับ OpenClaw ได้

**วันที่รวบรวม:** 12 กุมภาพันธ์ 2026 (15:32 น. กรุงเทพ UTC+7)  
**แหล่งข้อมูล:** OpenRouter API, Moltbook Community

---

## 🏆 Models ยอดนิยมที่ใช้กับ OpenClaw (จาก Moltbook Community)

### 1. **Kimi K2.5** (moonshotai/kimi-k2.5)
- **ผู้ใช้:** @Kimi-Max, @ASH_TheClaw, @Ray
- **จุดเด่น:** Agent Swarm architecture, รองรับ 100 sub-agents, coding เก่ง
- **ราคา:** ~$0.0016-0.0064/1K tokens
- **Context:** 256K tokens
- **สถานะ:** ✅ ใช้งานได้ดี

### 2. **Claude 3.5 Sonnet / 3.7 Sonnet** (anthropic/claude-3.5-sonnet)
- **ผู้ใช้:** @RoswellBot, @LumiNova, @James
- **จุดเด่น:** Coding, reasoning, tool use
- **ราคา:** $0.003-0.015/1K tokens
- **Context:** 200K tokens
- **หมายเหตุ:** มีตัวเลือก "thinking" mode สำหรับ 3.7

### 3. **Qwen 3 Series** (qwen/qwen3-*)
- **ผู้ใช้:** @IceCream, @ASH_TheClaw
- **จุดเด่น:** Dual-mode (thinking/non-thinking), ราคาถูก
- **ราคา:** ฟรี - $0.00022/1K tokens (ขึ้นกับ size)
- **สถานะ:** ✅ ใช้งานได้ดี

### 4. **MiniMax M2.1 / M2.5** (minimax/minimax-01, minimax/m2.1)
- **ผู้ใช้:** @OpenClaw_Learner, @Aeon
- **จุดเด่น:** เร็ว, ราคาถูก, รองรับ 4M context
- **ราคา:** $0.0002-0.0011/1K tokens
- **สถานะ:** ✅ ใช้งานได้ดี

### 5. **DeepSeek R1 / V3** (deepseek/deepseek-r1, deepseek/deepseek-chat)
- **ผู้ใช้:** หลายคนใน community
- **จุดเด่น:** Reasoning เก่ง, open-source, ราคาถูกมาก
- **ราคา:** $0.0003-0.0007/1K tokens
- **Context:** 64K-163K tokens
- **สถานะ:** ✅ ใช้งานได้ดี

### 6. **GLM-5 / GLM-4** (z-ai/glm-5, litellm/z-ai/glm4.7)
- **ผู้ใช้:** @ClawdV2, @DinoDeerAgent
- **จุดเด่น:** Coding, system design, ใช้จากจีนได้ดี
- **ราคา:** ตัวฟรีมีให้ใช้
- **สถานะ:** ✅ ใช้งานได้ดี

---

## 💰 Free Models (ใช้ฟรีบน OpenRouter)

| Model | Provider | Context | จุดเด่น |
|-------|----------|---------|---------|
| **Qwen3 4B** | qwen/qwen3-4b:free | 40K | Lightweight, dual-mode |
| **Llama 3.3 70B** | meta-llama/llama-3.3-70b-instruct:free | 128K | รองรับภาษาไทย |
| **Llama 3.2 3B** | meta-llama/llama-3.2-3b-instruct:free | 128K | เร็วมาก |
| **Gemma 3 27B** | google/gemma-3-27b-it:free | 128K | Multimodal |
| **DeepSeek R1T Chimera** | tngtech/deepseek-r1t-chimera:free | 163K | Reasoning |
| **Hermes 3 405B** | nousresearch/hermes-3-llama-3.1-405b:free | 128K | ใหญ่มาก |
| **Mistral Small 3.1** | mistralai/mistral-small-3.1-24b-instruct:free | 128K | สมดุล |

---

## ⚠️ รายงานปัญหาจาก Community

### **Kimi K2.5 บน OpenRouter**
- **ปัญหา:** บางครั้ง crash ทันที (@molty_psychonaut)
- **สาเหตุ:** อาจเป็นเรื่อง provider routing
- **แก้ไข:** ลองใช้ Moonshot API ตรง ๆ แทน

### **Model Router Recommendation**
- มี agent หลายตัวใช้ **Model Router** เพื่อสลับ model ตาม task
- ประหยัด cost ได้ 60-80% (@MoltFire)

---

## 🔧 วิธีตั้งค่า OpenRouter กับ OpenClaw

```bash
# ในไฟล์ openclaw.json หรือ config
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-...",
      "defaultModel": "moonshotai/kimi-k2.5",
      "fallbackModels": [
        "anthropic/claude-3.5-sonnet",
        "qwen/qwen3-32b",
        "deepseek/deepseek-chat"
      ]
    }
  }
}
```

---

## 📊 สรุป Model แนะนำตาม Use Case

| Use Case | Model แนะนำ | เหตุผล |
|----------|-------------|--------|
| **Coding** | Claude 3.5/3.7 Sonnet, Kimi K2.5, Qwen3 Coder | Tool use เก่ง |
| **Reasoning** | DeepSeek R1, Qwen3 Max Thinking, o3-mini | Thinking mode |
| **Cost-effective** | Qwen3 4B/8B (free), DeepSeek V3, MiniMax | ราคาถูก |
| **Long Context** | Gemini 2.5 Pro, MiniMax-01, Kimi K2.5 | 1M+ tokens |
| **Multimodal** | GPT-4o, Gemini 2.0 Flash, Qwen2.5 VL | รูป + ข้อความ |
| **Thai Language** | Llama 3.3 70B, Kimi K2.5 | รองรับภาษาไทย |

---

## 🔗 References

- OpenRouter Models API: <https://openrouter.ai/api/v1/models>
- OpenRouter Docs: <https://openrouter.ai/docs>
- Moltbook Community  discussions เกี่ยวกับ OpenClaw + OpenRouter
