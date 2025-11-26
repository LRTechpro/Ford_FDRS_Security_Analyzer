# Ford LLM Integration Guide

## Overview

This diagnostic analyzer now supports **multiple LLM providers**, including:
- ✅ **Ford's Internal LLM** (enterprise solution)
- ✅ **Azure OpenAI** (Microsoft enterprise)
- ✅ **AWS Bedrock** (Amazon enterprise)
- ✅ **OpenAI** (public API)
- ✅ **Anthropic Claude** (Claude 3.5)
- ✅ **Custom endpoints** (any REST API)

---

## 🏢 Why Use Ford's LLM?

### Benefits for Ford:
1. **Data Privacy** - Keep diagnostic data within Ford's network
2. **Compliance** - Meet Ford's data governance requirements
3. **No External Costs** - No per-query charges to OpenAI
4. **Customization** - Model trained on Ford-specific diagnostics
5. **Security** - No data leaves Ford's infrastructure

### Typical Ford Setup:
- **Ford LLM Endpoint**: Internal API hosted on Ford's cloud
- **Authentication**: Ford SSO or API key
- **Data Residency**: All data stays within Ford network
- **Cost**: Free for Ford employees (internal budget)

---

## 🔧 Setup Options for Ford

### **Option 1: Ford Internal LLM** (Recommended for Ford)

If Ford has an internal LLM API (ask your IT/AI team):

#### Step 1: Get Ford LLM Credentials
Contact Ford's AI/ML team to get:
- **Endpoint URL**: `https://ford-llm-api.ford.com/v1/completions` (example)
- **API Key**: Your Ford employee API key
- **Model Name**: The diagnostic model name (e.g., `ford-diagnostic-v1`)

#### Step 2: Create Configuration File
Create `llm_config.json` in your project folder:

```json
{
  "provider": "ford_llm",
  "endpoint": "https://ford-llm-api.ford.com/v1/completions",
  "model": "ford-diagnostic-v1",
  "max_tokens": 4000,
  "temperature": 0.3
}
```

#### Step 3: Set Environment Variable
In PowerShell:
```powershell
# For current session
$env:FORD_LLM_API_KEY = "your-ford-api-key-here"

# Or permanently (recommended)
[Environment]::SetEnvironmentVariable("FORD_LLM_API_KEY", "your-ford-api-key-here", "User")
```

#### Step 4: Run the App
```powershell
python professional_diagnostic_analyzer.py
```

The app will automatically detect Ford LLM configuration!

---

### **Option 2: Azure OpenAI** (Common for Enterprise)

Many enterprises use Azure OpenAI for data privacy.

#### Step 1: Get Azure OpenAI Credentials
From Ford's Azure portal or IT team:
- **Resource Name**: e.g., `ford-openai`
- **Deployment Name**: e.g., `gpt-4o`
- **Endpoint**: `https://ford-openai.openai.azure.com/`
- **API Key**: Your Azure OpenAI key

#### Step 2: Create Configuration
Create `llm_config.json`:

```json
{
  "provider": "azure_openai",
  "endpoint": "https://ford-openai.openai.azure.com/",
  "deployment_name": "gpt-4o",
  "model": "gpt-4o",
  "max_tokens": 4000,
  "temperature": 0.3
}
```

#### Step 3: Set API Key
```powershell
$env:AZURE_OPENAI_API_KEY = "your-azure-key-here"
```

#### Step 4: Install Azure OpenAI
```powershell
pip install openai
```

---

### **Option 3: AWS Bedrock** (Amazon Enterprise)

If Ford uses AWS infrastructure:

#### Step 1: Get AWS Credentials
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Region**: e.g., `us-east-1`
- **Model**: e.g., `anthropic.claude-3-5-sonnet-20241022-v2:0`

#### Step 2: Create Configuration
Create `llm_config.json`:

```json
{
  "provider": "aws_bedrock",
  "model": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "region": "us-east-1",
  "max_tokens": 4000,
  "temperature": 0.3
}
```

#### Step 3: Set AWS Credentials
```powershell
$env:AWS_ACCESS_KEY_ID = "your-access-key"
$env:AWS_SECRET_ACCESS_KEY = "your-secret-key"
```

#### Step 4: Install boto3
```powershell
pip install boto3
```

---

## 📋 Configuration File Reference

### Full `llm_config.json` Example (Ford LLM)

```json
{
  "provider": "ford_llm",
  "endpoint": "https://ford-llm-api.ford.com/v1/completions",
  "model": "ford-diagnostic-v1",
  "max_tokens": 4000,
  "temperature": 0.3,
  "custom_headers": {
    "Authorization": "Bearer YOUR_KEY_HERE",
    "X-Ford-Department": "Diagnostics",
    "X-Ford-Application": "Professional-Analyzer"
  }
}
```

### Configuration Options

| Field | Description | Required | Example |
|-------|-------------|----------|---------|
| `provider` | LLM provider type | Yes | `"ford_llm"`, `"azure_openai"`, `"openai"` |
| `endpoint` | API endpoint URL | For Ford/Azure/Custom | `"https://ford-llm.ford.com/v1"` |
| `model` | Model name | Yes | `"ford-diagnostic-v1"`, `"gpt-4o"` |
| `max_tokens` | Max response length | No (default: 4000) | `4000` |
| `temperature` | Creativity (0-1) | No (default: 0.3) | `0.3` |
| `deployment_name` | Azure deployment | For Azure only | `"gpt-4o"` |
| `region` | AWS region | For AWS only | `"us-east-1"` |
| `custom_headers` | Extra HTTP headers | No | `{"X-Custom": "value"}` |

---

## 🔐 Security Best Practices

### DO NOT Store API Keys in Config File!

❌ **Bad** - Storing key in `llm_config.json`:
```json
{
  "provider": "ford_llm",
  "api_key": "secret-key-123"  // DO NOT DO THIS!
}
```

✅ **Good** - Using environment variables:
```powershell
$env:FORD_LLM_API_KEY = "secret-key-123"
```

### Environment Variables by Provider

| Provider | Environment Variable |
|----------|---------------------|
| Ford LLM | `FORD_LLM_API_KEY` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` |
| AWS Bedrock | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` |
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |

---

## 🧪 Testing Your Ford LLM Setup

### Step 1: Create Test Script
Save as `test_ford_llm.py`:

```python
from enterprise_llm_provider import EnterpriseLLMProvider, LLMConfig, LLMProvider

# Test Ford LLM
config = LLMConfig(
    provider=LLMProvider.FORD_LLM,
    endpoint="https://your-ford-endpoint",
    model="ford-diagnostic-v1"
)

provider = EnterpriseLLMProvider(config)

if provider.is_available():
    print("✅ Ford LLM connected!")
    
    # Test completion
    response = provider.generate_completion(
        prompt="Explain NRC 0x31 error code",
        system_prompt="You are a Ford diagnostic expert."
    )
    
    print("\n" + "="*60)
    print("FORD LLM RESPONSE:")
    print("="*60)
    print(response)
else:
    print("❌ Ford LLM not available. Check your configuration.")
```

### Step 2: Run Test
```powershell
python test_ford_llm.py
```

---

## 🏗️ How to Find Ford's LLM Endpoint

### Ask These Teams:
1. **Ford IT AI/ML Team** - Primary contact
2. **Ford Cloud Platform Team** - Infrastructure details
3. **Ford DevOps** - Deployment/endpoint info
4. **Your Manager** - Approval for access

### Common Ford Endpoint Patterns:
- Internal: `https://llm-api.ford.com/v1/completions`
- Azure: `https://ford-ai.openai.azure.com/`
- AWS: Ford's AWS account with Bedrock enabled

### Questions to Ask:
1. "Does Ford have an internal LLM API for diagnostic tools?"
2. "What authentication method do we use? (API key, SSO, OAuth)"
3. "What's the endpoint URL and model name?"
4. "Are there usage limits or quotas?"
5. "Who do I contact for access/credentials?"

---

## 💰 Cost Comparison

| Provider | Cost per 1000 Analyses | Data Privacy | Setup Difficulty |
|----------|----------------------|--------------|------------------|
| **Ford LLM** | **$0** (internal) | ✅ Excellent | Medium |
| **Azure OpenAI** | ~$10-20 | ✅ Good (Ford tenant) | Medium |
| **AWS Bedrock** | ~$15-25 | ✅ Good (Ford VPC) | Hard |
| **OpenAI Public** | ~$10-20 | ⚠️ Limited | Easy |

**Recommendation for Ford:** Use Ford LLM if available, fallback to Azure OpenAI.

---

## 🔄 Switching Providers

### Change at Runtime (GUI)
Future enhancement will add provider selector in Settings tab.

### Change via Config File
Edit `llm_config.json` and change the `provider` field:

```json
{
  "provider": "ford_llm"  // or "azure_openai", "openai", etc.
}
```

Restart the app to apply changes.

---

## 📞 Getting Help

### Ford Internal Resources:
- **Ford AI/ML Portal**: Search for "LLM API" on Ford's intranet
- **Ford DevHub**: Developer documentation
- **Ford IT Support**: Ticket for API access
- **Ford Slack**: #ai-ml or #developer-tools channels

### Technical Issues:
1. Check `llm_config.json` syntax (valid JSON)
2. Verify environment variables are set
3. Test endpoint with `curl` or Postman first
4. Check Ford's VPN/network access
5. Review logs for specific errors

---

## 🚀 Quick Start for Ford Employees

**If you already have Ford LLM credentials:**

1. Create `llm_config.json`:
```json
{
  "provider": "ford_llm",
  "endpoint": "YOUR_FORD_ENDPOINT",
  "model": "YOUR_MODEL_NAME"
}
```

2. Set API key:
```powershell
$env:FORD_LLM_API_KEY = "YOUR_API_KEY"
```

3. Run:
```powershell
python professional_diagnostic_analyzer.py
```

**Done!** The app will use Ford's LLM instead of OpenAI.

---

## 📊 Feature Comparison

All features work with ANY provider:

✅ Diagnostic analysis
✅ Root cause detection
✅ Part number interpretation
✅ ML pattern learning
✅ Error code explanations
✅ Recommendations

The provider is **transparent** - you get the same features whether using Ford LLM, Azure, or OpenAI!

---

## Next Steps

1. **Contact Ford's AI team** to get LLM access
2. **Create `llm_config.json`** with your credentials
3. **Test the connection** with test script
4. **Use the GUI** - everything works automatically!

**Questions?** Contact your Ford IT support or AI/ML team for LLM access credentials.
