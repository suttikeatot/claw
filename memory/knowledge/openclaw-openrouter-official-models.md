# OpenClaw Models บน OpenRouter (Official)

**วันที่รวบรวม:** 12 กุมภาพันธ์ 2026 (15:57 น. กรุงเทพ UTC+7)  
**แหล่งข้อมูล:** https://openrouter.ai/apps?url=https%3A%2F%2Fopenclaw.ai%2F

---

## 📋 Models ทั้งหมดที่ OpenClaw ใช้ผ่าน OpenRouter

รายชื่อ model ที่ OpenClaw.ai (official) เรียกใช้งานผ่าน OpenRouter:

| # | Model Name | Provider | หมายเหตุ |
|---|------------|----------|----------|
| 1 | **Kimi K2.5** | moonshotai | 🌟 ยอดนิยมมาก, Agent Swarm |
| 2 | **Trinity Large Preview (free)** | arcee-ai | 🆓 Free tier |
| 3 | **Gemini 3 Flash Preview** | google | Fast, multimodal |
| 4 | **Step 3.5 Flash** | stepfun | Chinese model, fast |
| 5 | **Claude Sonnet 4.5** | anthropic | Coding, reasoning |
| 6 | **Claude Opus 4.6** | anthropic | Advanced reasoning |
| 7 | **DeepSeek V3.2** | deepseek | 🆓 ราคาถูก, reasoning |
| 8 | **Claude Opus 4.5** | anthropic | High-end |
| 9 | **Grok 4.1 Fast** | x-ai | Fast, xAI |
| 10 | **MiniMax M2.1** | minimax | 🆓 Long context |
| 11 | **Pony Alpha** | openrouter | OpenRouter native |
| 12 | **Gemini 2.5 Flash Lite** | google | Fast, cheap |
| 13 | **Gemini 2.5 Flash** | google | Standard |
| 14 | **GLM 4.5 Air** | z-ai | Chinese, efficient |
| 15 | **Claude Haiku 4.5** | anthropic | Fast, cheap |
| 16 | **Gemini 3 Pro Preview** | google | High quality |
| 17 | **Claude Sonnet 4** | anthropic | Previous version |
| 18 | **GPT-5.2** | openai | OpenAI latest |
| 19 | **GLM 4.7** | z-ai | Chinese, powerful |
| 20 | **GLM 4.7 Flash** | z-ai | Fast version |

---

## 🏆 สรุปตาม Provider

### Moonshot AI (Kimi)
- **Kimi K2.5** - ตัวหลักที่นิยมมากใน OpenClaw community
- รองรับ 256K context, Agent Swarm architecture
- ใช้งานโดย: OpenClaw, Kilo Code, Roo Code, Cline, liteLLM

### Anthropic (Claude)
- **Claude Sonnet 4.5** - Coding และ reasoning
- **Claude Opus 4.6/4.5** - High-end tasks
- **Claude Haiku 4.5** - Fast, cost-effective
- **Claude Sonnet 4** - Previous generation

### Google (Gemini)
- **Gemini 3 Pro Preview** - คุณภาพสูงสุด
- **Gemini 3 Flash Preview** - เร็ว, multimodal
- **Gemini 2.5 Flash/Flash Lite** - ประหยัด

### DeepSeek
- **DeepSeek V3.2** - ราคาถูก, reasoning ดี
- Open-source, ใช้กันมากใน community

### MiniMax
- **MiniMax M2.1** - Context ยาว (4M tokens)
- เร็ว, ราคาถูก

### Z.AI (GLM)
- **GLM 4.7 / 4.7 Flash** - Chinese model ที่ดี
- **GLM 4.5 Air** - Efficient

### อื่น ๆ
- **Grok 4.1 Fast** (xAI) - จาก X/Twitter
- **Step 3.5 Flash** (StepFun) - Chinese
- **Trinity Large Preview** (Arcee AI) - Free
- **Pony Alpha** (OpenRouter) - Native
- **GPT-5.2** (OpenAI) - Latest

---

## 💰 Free / Low-Cost Models

| Model | Provider | ราคา |
|-------|----------|------|
| Trinity Large Preview | arcee-ai | 🆓 Free |
| MiniMax M2.1 | minimax | 🆓 Free / ถูก |
| DeepSeek V3.2 | deepseek | ถูกมาก |
| GLM 4.5 Air | z-ai | ถูก |
| Claude Haiku 4.5 | anthropic | ถูก |

---

## 🔧 การตั้งค่าใน OpenClaw

OpenClaw สามารถกำหนด model ที่จะใช้ผ่าน OpenRouter ได้ในการตั้งค่า:

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-...",
      "defaultModel": "moonshotai/kimi-k2.5",
      "models": [
        "moonshotai/kimi-k2.5",
        "anthropic/claude-sonnet-4.5",
        "google/gemini-3-flash-preview",
        "deepseek/deepseek-v3.2"
      ]
    }
  }
}
```

---

## 📊 Insights

1. **Kimi K2.5 เป็นที่นิยมมาก** - มีหลาย apps ใช้ (OpenClaw, Kilo Code, Roo Code, Cline, liteLLM)
2. **มีตัวเลือก Free** - Trinity Large Preview, MiniMax M2.1
3. **ครอบคลุมหลาย Provider** - ไม่ได้ผูกขาดกับเจ้าใดเจ้าหนึ่ง
4. **รองรับ Multimodal** - Gemini series รองรับรูปภาพ
5. **มีตัวเลือก Chinese Models** - MiniMax, StepFun, GLM

---

## 🔗 Related Links

- OpenRouter OpenClaw Apps: https://openrouter.ai/apps?url=https%3A%2F%2Fopenclaw.ai%2F
- OpenRouter Models: https://openrouter.ai/models
- OpenClaw Official: https://openclaw.ai/
