# 🔒 OPENCLAW SECURITY HARDENING GUIDE
**Target:** Maximum Security Posture for Agent Operations  
**Level:** Advanced  
**Last Updated:** 2026-02-10

---

## 🎯 SECURITY TIERS

### Tier 1: Basic (Minimum Viable Security)
สำหรับ: Personal use, non-sensitive data
- ✅ Hourly backups
- ✅ Config backups before changes
- ✅ Read-only mode สำหรับ social media

### Tier 2: Standard (Recommended)
สำหรับ: Professional use, sensitive data
- ✅ ทั้งหมดจาก Tier 1 +
- ✅ Skill whitelist only
- ✅ API key rotation monthly
- ✅ Browser sandboxing

### Tier 3: Maximum (Paranoid Mode)
สำหรับ: Enterprise, critical infrastructure
- ✅ ทั้งหมดจาก Tier 2 +
- ✅ Network isolation (no outbound)
- ✅ Local models only (no cloud API)
- ✅ Manual approval ทุก tool call

---

## 🔧 IMPLEMENTATION GUIDE

### 1. BACKUP STRATEGY (3-2-1 Rule)

**3 Copies:**
1. Local workspace
2. GitHub (primary remote)
3. Secondary remote (GitLab/S3)

**2 Different Media:**
- Git repository
- Archive files (encrypted)

**1 Offsite:**
- GitHub (already offsite)
- Optional: AWS S3 Glacier

**Automation:**
```bash
# cron job ที่มีอยู่แล้วทำงานดี
# เพิ่ม secondary backup:
0 */6 * * * ~/.openclaw/scripts/backup-to-s3.sh
```

---

### 2. SKILL SANDBOXING

**Current Problem:**
- Skills มี full system access
- No isolation between skills
- Malicious skill = full compromise

**Solution Approaches:**

#### Option A: Docker Sandbox (Recommended)
```dockerfile
# Dockerfile.skill-runner
FROM node:20-alpine
RUN adduser -D -s /bin/sh agent
USER agent
WORKDIR /workspace
COPY skill/ ./
CMD ["node", "index.js"]
```

```bash
# Run skill in container
docker run --rm \
  --read-only \
  --tmpfs /tmp:noexec,nosuid,size=100m \
  --network none \
  -v ~/.openclaw/workspace:/workspace:ro \
  skill-runner
```

#### Option B: Firejail (Linux)
```bash
# Sandbox skill execution
firejail --noprofile --private --net=none \
  node ~/.openclaw/skills/<skill>/index.js
```

#### Option C: Deno Permissions (JavaScript/TypeScript)
```javascript
# ใช้ Deno แทน Node.js
# Explicit permissions only
deno run --allow-read=/workspace \
         --allow-write=/workspace/output \
         --allow-net=none \
         skill.ts
```

---

### 3. NETWORK ISOLATION

**Current:** Agent มี internet access เต็มรูปแบบ

**Hardening Levels:**

#### Level 1: Outbound Filtering
```bash
# iptables rules
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT  # HTTPS only
iptables -A OUTPUT -p tcp --dport 80 -j DROP     # Block HTTP
iptables -A OUTPUT -p tcp --dport 22 -j DROP     # Block SSH outbound
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT  # DNS only to specific
```

#### Level 2: Proxy Required
```bash
# บังคับผ่าน proxy ที่ log ทุก request
export HTTP_PROXY=http://localhost:8080
export HTTPS_PROXY=http://localhost:8080

# Proxy ทำหน้าที่ filter + log
```

#### Level 3: Air Gap (Maximum)
```bash
# ตัด internet ออกจากเครื่องที่รัน Agent
# ใช้ sneakernet สำหรับ data transfer
```

---

### 4. SECRETS MANAGEMENT

**Current Issues:**
- Some credentials in plaintext (MEMORY.md)
- No rotation schedule
- No audit trail

**Solution:**

#### Step 1: Consolidate
```bash
# ย้ายทุกอย่างไป auth-profiles.json
openclaw auth add facebook --mode=oauth
openclaw auth add twitter --mode=api_key
# etc.
```

#### Step 2: Environment Variables (Better)
```bash
# ~/.openclaw/.env
KIMI_API_KEY=sk-xxx
TELEGRAM_BOT_TOKEN=xxx
DISCORD_TOKEN=xxx

# Load ทุกครั้งที่ start
export $(cat ~/.openclaw/.env | xargs)
```

#### Step 3: External Vault (Best)
```bash
# HashiCorp Vault
vault kv get secret/openclaw/kimi

# AWS Secrets Manager
aws secretsmanager get-secret-value \
  --secret-id openclaw/credentials
```

**Rotation Schedule:**
| Secret Type | Rotation Frequency |
|-------------|-------------------|
| API Keys | Monthly |
| OAuth Tokens | Every 3 months |
| Bot Tokens | Every 6 months |
| Passwords | Immediately if suspected |

---

### 5. MONITORING & ALERTING

**Current State:** Manual checking

**Target State:** Automated monitoring

#### Health Check Script
```bash
#!/bin/bash
# ~/.openclaw/scripts/health-check.sh

ALERTS=""

# Check disk space
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
if [ $DISK_USAGE -gt 80 ]; then
  ALERTS+="⚠️ Disk usage: ${DISK_USAGE}%\n"
fi

# Check memory
MEM_USAGE=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
if [ $MEM_USAGE -gt 90 ]; then
  ALERTS+="⚠️ Memory usage: ${MEM_USAGE}%\n"
fi

# Check zombie processes
ZOMBIES=$(ps aux | grep 'chrome-headless' | grep -v grep | wc -l)
if [ $ZOMBIES -gt 5 ]; then
  ALERTS+="⚠️ Zombie processes: ${ZOMBIES}\n"
fi

# Check cron jobs
FAILED_JOBS=$(openclaw cron list | grep -c 'error')
if [ $FAILED_JOBS -gt 0 ]; then
  ALERTS+="⚠️ Failed cron jobs: ${FAILED_JOBS}\n"
fi

# Send alert if any issues
if [ -n "$ALERTS" ]; then
  echo -e "$ALERTS" | telegram-send --stdin
fi
```

#### Prometheus/Grafana (Advanced)
```yaml
# docker-compose.yml
version: '3'
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

**Metrics to Track:**
- Context usage over time
- API call latency
- Error rates by tool
- Disk/Memory usage
- Cron job success rates

---

### 6. MODEL SECURITY

**Current Risk:** Dependency on external APIs

**Mitigations:**

#### Fallback Chain
```json
{
  "primary": "kimi-coding/k2p5",
  "fallbacks": [
    "google-antigravity/claude-opus-4-5-thinking",
    "google-antigravity/gemini-3-pro-high",
    "local/ollama-llama2"  // Local model
  ]
}
```

#### Local Model Option
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull model
ollama pull llama2:13b

# Configure OpenClaw
openclaw config set models.local="ollama/llama2:13b"
```

**Trade-offs:**
| Approach | Latency | Quality | Privacy | Cost |
|----------|---------|---------|---------|------|
| Cloud API | Low | High | Low | $$$
| Local GPU | Low | Medium | High | $ (hardware) |
| Local CPU | High | Medium | High | Free |

---

## 📊 SECURITY SCORING

**Current System Score: 7.5/10**

| Category | Score | Notes |
|----------|-------|-------|
| Backup | 9/10 | Hourly + config backups |
| Access Control | 6/10 | Some plaintext creds |
| Monitoring | 5/10 | No automated alerting |
| Incident Response | 8/10 | Good protocols in place |
| Network Security | 6/10 | No isolation |
| Secrets Management | 7/10 | Mostly good, some gaps |

**Target Score: 9.0/10**

---

## 🎓 SECURITY TRAINING CHECKLIST

สำหรับ Agent ทุกตัวที่รันในระบบ:

### Must Know
- [ ] How to identify suspicious skill code
- [ ] When to create HANDOFF.md
- [ ] How to verify backup integrity
- [ ] Emergency shutdown procedures

### Should Know
- [ ] Basic log analysis
- [ ] Network connection monitoring
- [ ] File integrity checking
- [ ] Secret rotation procedures

### Nice to Know
- [ ] Forensics basics
- [ ] Malware analysis fundamentals
- [ ] Cryptography basics
- [ ] Social engineering awareness

---

## 🚀 IMPLEMENTATION ROADMAP

### Week 1: Quick Wins
- [ ] Move all credentials to auth-profiles.json
- [ ] Set up health check cron job
- [ ] Document all current skills (audit)

### Week 2: Monitoring
- [ ] Set up Prometheus + Grafana
- [ ] Configure alerts
- [ ] Create dashboards

### Week 3: Sandboxing
- [ ] Test Docker sandbox for skills
- [ ] Migrate safe skills
- [ ] Document sandbox procedures

### Week 4: Hardening
- [ ] Implement network filtering
- [ ] Set up local model fallback
- [ ] Full security audit

---

**Next Review:** 2026-03-10  
**Owner:** กุ้ง Security Team  
**Questions:** Telegram @gung_security
