# AI Configuration Guide

## Enabling AI-Powered Features

Your Ford FDRS Security Analyzer includes advanced AI capabilities powered by OpenAI's GPT models. This guide explains how to set up and use these features.

## Features

### 🤖 AI Diagnostic Assistant
- Natural language analysis of diagnostic logs
- Intelligent root cause identification
- Repair recommendations
- Pattern recognition and learning
- Context-aware explanations

### 🧠 Intelligent Diagnostic Engine
- Multi-source evidence analysis
- Document correlation and cross-referencing
- Evidence-based conclusions
- Professional diagnostic reports
- Risk assessment and recommendations

## Setup Instructions

### 1. Get an OpenAI API Key

1. Visit: https://platform.openai.com/account/api-keys
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy the API key (save it somewhere safe - you'll only see it once!)

### 2. Add API Key to the Application

**Option A: Using the GUI**
1. Launch the Ford FDRS Security Analyzer
2. Go to **Tools** menu → **Configure LLM**
3. Enter your OpenAI API key
4. Click "Save"

**Option B: Environment Variable**
```bash
set OPENAI_API_KEY=sk-your-api-key-here
python professional_diagnostic_analyzer.py
```

**Option C: Configuration File**
Create a `config.local.json` file in the project root:
```json
{
  "openai_api_key": "sk-your-api-key-here",
  "ai_model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 2000
}
```

### 3. Verify AI is Working

1. Load a diagnostic log file
2. Go to the **"AI Assistant"** or **"Intelligent Analysis"** tab
3. You should see AI features are now enabled
4. The status bar should show "✅ AI Available"

## OpenAI API Costs

⚠️ **Important**: Using the OpenAI API may incur charges based on your usage.

**Pricing (as of 2025)**:
- GPT-4: ~$0.03-0.06 per 1K tokens
- GPT-3.5-turbo: ~$0.0005-0.0015 per 1K tokens

**Typical diagnostic analysis costs**: $0.01 - $0.10 per log

**Tips to minimize costs**:
- Use GPT-3.5-turbo for faster/cheaper analysis
- Analyze one log at a time
- Set up usage limits on your OpenAI account
- Monitor your usage at: https://platform.openai.com/account/usage/overview

## Troubleshooting

### "No API Key Found"
- Ensure your API key is correctly set
- Restart the application after setting the key
- Check that the key starts with `sk-`

### "API Key Invalid"
- Verify the key is correct (copy from OpenAI website again)
- Check that you haven't exceeded your usage quota
- Ensure your OpenAI account is in good standing

### "Rate Limited"
- OpenAI has rate limits - wait a few minutes before trying again
- Consider upgrading your OpenAI account for higher limits

### "Timeout Error"
- The AI analysis took too long
- Try analyzing a smaller log file first
- Check your internet connection

## Security Notes

🔐 **Never commit your API key to GitHub**
- Your `.gitignore` file already excludes `config.local.json`
- Never paste your API key in issues or pull requests
- Keep your API key confidential - treat it like a password

## Features by AI Model

### GPT-4 (Recommended for Production)
- More accurate diagnostics
- Better reasoning for complex issues
- Supports longer context
- Higher cost (~$0.03 per 1K tokens)

### GPT-3.5-turbo (Good for Testing)
- Faster responses
- Lower cost (~$0.0005 per 1K tokens)
- Good for basic analysis
- Suitable for high-volume scanning

## Advanced Configuration

### Custom Temperature Settings
Temperature controls randomness (0.0 = deterministic, 1.0 = creative):

```json
{
  "temperature": 0.3  // More accurate/conservative
}
```

### Max Tokens
Control response length (more tokens = longer responses = more cost):

```json
{
  "max_tokens": 1000  // Shorter responses
}
```

## Usage Examples

### Example 1: Analyze Diagnostic Errors
1. Load a Ford diagnostic log
2. Go to "AI Assistant" tab
3. The AI will:
   - Identify error codes
   - Explain what they mean
   - Suggest root causes
   - Recommend repair procedures

### Example 2: Compare Multiple Reports
1. Load primary log + correlation reports
2. Use "Intelligent Analysis" tab
3. AI will:
   - Find patterns across reports
   - Identify common issues
   - Suggest diagnostic path
   - Provide professional conclusions

## Privacy

Your diagnostic logs are sent to OpenAI for analysis. 

⚠️ **Important Considerations**:
- Do not analyze logs containing sensitive customer data
- Do not use for vehicles with active recalls/investigations
- Your logs will be processed by OpenAI's servers
- OpenAI may use diagnostic patterns for model improvement (can be disabled)
- Review OpenAI's privacy policy: https://openai.com/privacy

## Support

For issues with:
- **OpenAI API**: https://help.openai.com
- **This application**: Create an issue on GitHub
- **AI responses**: Check your API key and model selection

## Next Steps

After enabling AI:
1. Run sample analysis to verify functionality
2. Test with real diagnostic logs
3. Fine-tune temperature/token settings for your needs
4. Set usage alerts on your OpenAI account
5. Monitor costs and optimize as needed

---

**Happy diagnosing!** 🚗🔧
