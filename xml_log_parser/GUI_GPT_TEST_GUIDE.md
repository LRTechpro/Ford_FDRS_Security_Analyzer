# 🚀 Quick Guide: Testing GPT in the GUI

## Your GUI is Now Running! 

The Professional Diagnostic Analyzer is now open on your screen.

---

## 📍 STEP-BY-STEP GUIDE TO TEST GPT

### **STEP 1: Navigate to Settings** ⚙️

Look at the **tab bar at the top** of the window. You should see these tabs:
- 📋 Analysis Results
- 🔧 ECU Analysis  
- ⚠️ Error Analysis
- 📈 Timeline
- 📊 Statistics
- 🧠 Intelligent Analysis
- **🤖 AI Assistant** ← Click this tab!

---

### **STEP 2: Configure Your API Key** 🔑

Once you're in the **🤖 AI Assistant** tab, you'll see:

#### Top Section: "OpenAI API Configuration"
```
┌─────────────────────────────────────────────┐
│ OpenAI API Configuration                    │
├─────────────────────────────────────────────┤
│ API Key: [●●●●●●●●●●●●●●●●●●] [Set Key]    │
│                                             │
│ Status: ⚠️ Not configured                   │
└─────────────────────────────────────────────┘
```

**To configure:**
1. **Get your API key** from: https://platform.openai.com/api-keys
   - Sign in/create account
   - Click "Create new secret key"
   - Copy the key (starts with `sk-...`)

2. **Paste the key** into the text field (it will show as ●●● for security)

3. **Click "Set Key" button**

4. **You should see:**
   - ✅ Success message popup
   - Status changes to: ✅ "Configured"

---

### **STEP 3: Test GPT Analysis** 🧪

Now that your API key is configured, let's test it!

#### Option A: Quick Test with AI Assistant Tab

In the **🤖 AI Assistant** tab, you'll see:

```
┌─────────────────────────────────────────────┐
│ 🔬 AI Analysis Tools                        │
├─────────────────────────────────────────────┤
│ [🚀 Quick Analysis]                         │
│ [📊 Multi-Source Analysis]                  │
│ [🔍 Root Cause Analysis]                    │
│ [📝 Generate Report]                        │
└─────────────────────────────────────────────┘
```

**Click "🚀 Quick Analysis"** button

This will:
- Run a test analysis using current loaded data
- Send data to GPT-4o
- Display results below

#### Option B: Full Analysis with Real Log

1. **Go to "📋 Analysis Results" tab** (first tab)

2. **Load test2.txt:**
   - File menu → Open
   - Or use the file browser
   - Select: `test2.txt`

3. **Click "Analyze" button**

4. **Wait for analysis** (~10-30 seconds)

5. **Check results:**
   - Primary ECU: 7D0
   - Part Numbers: NU5T-14H214-BAA, etc.
   - FDRS Version: 45.5.8

6. **Go to "🧠 Intelligent Analysis" tab**
   - This shows AI-powered insights
   - GPT will analyze patterns
   - Provides diagnostic recommendations

---

### **STEP 4: View GPT Results** 📊

After analysis completes, you'll see in the **AI Analysis Results** section:

```
═══════════════════════════════════════════
🎯 AI ANALYSIS RESULTS
═══════════════════════════════════════════

[AI ANALYSIS]

Primary ECU Analysis:
• ECU 7D0 detected with 80 occurrences
• This is the Body Control Module (BCM)
• High confidence in identification

Error Pattern Analysis:
• NRC 0x31 (Request Out of Range) - 183 occurrences
• This indicates attempted access to DIDs outside
  the valid range for this module
• Common when using wrong calibration version

Calibration Analysis:
• DID 8061: NU5T-14H214-BAA (detected)
• DID 8060: NU5T-14H212-UB (detected)
• FDRS Version: 45.5.8
• Calibrations appear to be Ford-specific format

Recommendations:
1. Verify calibration version compatibility
2. Check if DID access permissions are correct
3. Review FDRS version for module compatibility
4. Consider updating module firmware if mismatch

Root Cause (Likely):
The high NRC 0x31 count suggests a version mismatch
between the diagnostic tool (FDRS 45.5.8) and the
module's expected calibration format.

═══════════════════════════════════════════
```

---

### **STEP 5: Verify GPT is Working** ✅

**Signs GPT is working correctly:**

✅ **No API key warnings** in the results
✅ **Detailed analysis text** appears (not just raw data)
✅ **Recommendations section** with actionable steps
✅ **Root cause analysis** with explanations
✅ **Technical terms explained** (e.g., "NRC 0x31 means...")

**Signs GPT is NOT working:**

❌ Message: "(No API key/configured, skipping real AI analysis)"
❌ Message: "AI features will be disabled"
❌ Only raw data shown, no analysis
❌ Error messages about authentication

---

## 🎯 What to Look For

### In the GUI Console (terminal where you launched):

**Good signs:**
```
✅ AI assistant initialized
✅ Using model: gpt-4o
✅ Max tokens: 4000
```

**Bad signs:**
```
⚠️ No OpenAI API key found
⚠️ AI features will be disabled
❌ Authentication failed
```

---

## 💡 Advanced Testing

### Test Different Models

Currently using: **gpt-4o** (default)

Available models:
- `gpt-4o` ← Current (best quality, slower)
- `gpt-4o-mini` (faster, cheaper)
- `gpt-4-turbo` (good balance)
- `gpt-5` (when available)

**To change models** (requires code edit):
1. Open `ai_diagnostic_assistant.py`
2. Find line: `self.model = model if model else "gpt-4o"`
3. Change default to: `"gpt-4o-mini"` for faster testing
4. Restart the app

### Test with Complex Data

Load **test2.txt** for comprehensive testing:
- 181 DIDs
- 183 NRC errors
- Multiple part numbers
- Real-world diagnostic scenario

This will give GPT more data to analyze and provide better insights.

---

## 💰 Cost Tracking

**After each analysis**, check your OpenAI usage:
- Dashboard: https://platform.openai.com/usage
- Typical cost: $0.01-0.02 per analysis
- 100 analyses ≈ $1-2 total

**Tips to reduce costs:**
- Use `gpt-4o-mini` for routine analysis (5x cheaper)
- Use `gpt-4o` only for complex diagnostics
- Limit max_tokens if you want shorter responses

---

## 🔧 Troubleshooting

### Problem: API key won't save

**Solution:**
1. Close the app
2. Check if `ai_config.json` exists in the folder
3. Open it and verify: `{"openai_api_key": "sk-..."}`
4. If missing, manually create it:
```json
{
  "openai_api_key": "sk-your-actual-key-here"
}
```

### Problem: "Rate limit exceeded"

**Solution:**
- You've hit OpenAI's rate limit
- Wait 60 seconds
- Try again
- Consider upgrading to paid tier for higher limits

### Problem: Analysis takes forever

**Possible causes:**
- GPT-4o can take 20-30 seconds for complex analysis (normal)
- Network connection slow
- OpenAI API experiencing issues

**Solution:**
- Wait up to 60 seconds
- Check OpenAI status: https://status.openai.com
- Try `gpt-4o-mini` for faster responses

---

## ✅ Success Checklist

- [ ] GUI launched successfully
- [ ] Navigated to 🤖 AI Assistant tab
- [ ] API key entered and saved
- [ ] Status shows: ✅ Configured
- [ ] Loaded test2.txt file
- [ ] Analysis completed
- [ ] GPT analysis appeared in results
- [ ] Recommendations displayed
- [ ] No error messages about API key

---

## 🎉 Next Steps After Success

Once GPT is working, you can:

1. **Enable ML Pattern Learning** (coming soon)
   - Learns normal vs abnormal patterns for ECU 7D0
   - Provides anomaly scores
   - Improves recommendations over time

2. **Add Model Selector** (future enhancement)
   - GUI dropdown to switch between models
   - Real-time cost estimates
   - Quality vs speed trade-off

3. **Generate PDF Reports** (future enhancement)
   - Combine: Part numbers + Errors + ML insights + GPT analysis
   - Professional diagnostic reports
   - Share with team or customers

---

## 📞 Need Help?

**Your app is currently running!** 

Look at the GUI window and follow the steps above.

**If you encounter any issues:**
1. Check the terminal output for error messages
2. Verify your API key is correct (starts with `sk-`)
3. Make sure you have internet connection
4. Check OpenAI status page

**Want to see more debug info?**
- Check the terminal where you launched the app
- Look for log messages about AI initialization
