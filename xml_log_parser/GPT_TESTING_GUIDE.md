# GPT Testing Guide - GUI Method

## Quick Start: Test GPT in the Professional Diagnostic Analyzer GUI

### Step 1: Launch the Application
```powershell
python professional_diagnostic_analyzer.py
```

### Step 2: Configure Your API Key

1. **Go to the "Settings" tab** (top of the window)
2. **Find the "OpenAI API Configuration" section**
3. **Enter your API key** in the password field
4. **Click "Set Key"** button
5. You should see: ✅ "OpenAI API key configured successfully"

### Step 3: Test GPT Analysis

You have **TWO ways** to test GPT:

---

## METHOD A: Test with Existing Log File

1. **Go to "Analysis" tab**
2. **Load a log file** (e.g., test2.txt)
3. **Click "Analyze" button**
4. **Check the results display** - look for:
   - Primary ECU detection
   - DID counts
   - Part numbers (new feature!)
   - Error mappings

5. **Go to "Intelligent AI" tab** (if available)
   - This tab uses GPT to provide advanced analysis
   - You'll see AI-powered insights about your diagnostic session

---

## METHOD B: Quick API Key Verification

After setting the API key in Settings:

1. **Look for the status indicator** in the Settings tab
2. It should show: ✅ "API Key Status: Configured"
3. **Check the console/terminal** where you launched the app
   - Look for: "AI assistant initialized" or similar messages
   - If you see warnings about API key, it's not configured correctly

---

## What GPT Features Do

### 1. **Intelligent Diagnostic Analysis** (Intelligent AI Tab)
- Analyzes error patterns
- Identifies root causes
- Suggests diagnostic steps
- Explains technical codes (NRCs, DIDs)

### 2. **Root Cause Analysis**
- Correlates errors with part numbers
- Identifies module-specific issues
- Suggests calibration problems

### 3. **Advanced Pattern Recognition**
- Uses GPT-4o (4000 token limit)
- Can understand complex diagnostic scenarios
- Provides technician-friendly explanations

---

## Testing Checklist

- [ ] API key entered in Settings tab
- [ ] "Set Key" button clicked
- [ ] Success message appeared
- [ ] Log file loaded (test2.txt)
- [ ] Analysis completed
- [ ] Results show primary ECU: 7D0
- [ ] Part numbers displayed (DID 8061, 8060)
- [ ] Check Intelligent AI tab for GPT analysis

---

## Troubleshooting

### ❌ "No API key configured" error
**Fix:** Go to Settings tab, enter API key, click "Set Key"

### ❌ API key doesn't save after restart
**Fix:** The app saves to `ai_config.json` - make sure the folder is writable

### ❌ GPT analysis is slow
**Normal:** GPT-4o can take 10-30 seconds for complex analysis

### ❌ "Rate limit" error
**Fix:** You've hit OpenAI's rate limit. Wait 1 minute and try again.

### ❌ "Authentication failed" error
**Fix:** Your API key is incorrect. Get a new one from: https://platform.openai.com/api-keys

---

## Current GPT Configuration

- **Default Model:** gpt-4o (upgraded from gpt-4o-mini)
- **Max Tokens:** 4000 (increased for comprehensive analysis)
- **Available Models:**
  - gpt-4o (recommended)
  - gpt-4o-mini (faster, cheaper)
  - gpt-4-turbo
  - gpt-5 (when available)

---

## Cost Estimate

**GPT-4o Pricing (October 2025):**
- Input: ~$2.50 per 1M tokens
- Output: ~$10.00 per 1M tokens

**Typical diagnostic analysis:**
- Input: ~2000 tokens (diagnostic data)
- Output: ~1000 tokens (analysis)
- Cost per analysis: ~$0.01-0.02

**For 100 analyses:** ~$1-2 total cost

---

## Next Steps After Testing

Once GPT is working, you can:

1. **Enable ML Pattern Learning** (coming soon in GUI)
   - Learns normal vs abnormal patterns
   - Provides anomaly scores
   - Improves over time

2. **Add Model Selector** (future enhancement)
   - Switch between GPT models
   - Choose based on speed vs quality

3. **Root Cause Reports** (future enhancement)
   - Combine part numbers + errors + ML + GPT
   - Generate comprehensive diagnostic reports

---

## Get Your API Key

**OpenAI Platform:** https://platform.openai.com/api-keys

1. Sign in or create account
2. Click "Create new secret key"
3. Name it (e.g., "Diagnostic Analyzer")
4. Copy the key (starts with `sk-...`)
5. Paste into the GUI Settings tab

**Important:** Keep your API key secret! Don't share it or commit it to version control.
