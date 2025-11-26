"""
LLM Provider Configuration Wizard
Helps users set up Ford LLM, Azure OpenAI, or other providers
"""

import json
import os
from typing import Dict, Optional


def create_llm_config():
    """Interactive wizard to create LLM configuration"""
    
    print("=" * 70)
    print("LLM PROVIDER CONFIGURATION WIZARD")
    print("=" * 70)
    print()
    print("This wizard will help you configure your LLM provider.")
    print()
    
    # Step 1: Choose provider
    print("Available LLM Providers:")
    print()
    print("  1. Ford Internal LLM (recommended for Ford employees)")
    print("  2. Azure OpenAI (enterprise, data stays in your Azure tenant)")
    print("  3. AWS Bedrock (enterprise, uses AWS infrastructure)")
    print("  4. OpenAI (public API, easiest setup)")
    print("  5. Anthropic Claude (public API)")
    print("  6. Custom endpoint (your own LLM API)")
    print()
    
    choice = input("Select provider (1-6): ").strip()
    
    providers = {
        '1': 'ford_llm',
        '2': 'azure_openai',
        '3': 'aws_bedrock',
        '4': 'openai',
        '5': 'anthropic',
        '6': 'custom'
    }
    
    if choice not in providers:
        print("❌ Invalid choice. Exiting.")
        return
    
    provider = providers[choice]
    config = {'provider': provider}
    
    print()
    print(f"✅ Selected: {provider}")
    print()
    
    # Step 2: Provider-specific configuration
    if provider == 'ford_llm':
        configure_ford_llm(config)
    elif provider == 'azure_openai':
        configure_azure_openai(config)
    elif provider == 'aws_bedrock':
        configure_aws_bedrock(config)
    elif provider == 'openai':
        configure_openai(config)
    elif provider == 'anthropic':
        configure_anthropic(config)
    elif provider == 'custom':
        configure_custom(config)
    
    # Step 3: Common settings
    print()
    print("Common Settings:")
    print()
    
    max_tokens = input("Max tokens (default: 4000): ").strip()
    config['max_tokens'] = int(max_tokens) if max_tokens else 4000
    
    temperature = input("Temperature 0-1 (default: 0.3 for technical): ").strip()
    config['temperature'] = float(temperature) if temperature else 0.3
    
    # Step 4: Save configuration
    print()
    print("=" * 70)
    print("CONFIGURATION SUMMARY")
    print("=" * 70)
    print(json.dumps(config, indent=2))
    print()
    
    save = input("Save this configuration? (y/n): ").strip().lower()
    if save == 'y':
        with open('llm_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        print()
        print("✅ Configuration saved to llm_config.json")
        print()
        
        # Show environment variable instructions
        print_env_instructions(provider)
    else:
        print("❌ Configuration not saved.")


def configure_ford_llm(config: Dict):
    """Configure Ford LLM"""
    print("Ford LLM Configuration")
    print("-" * 70)
    print()
    print("Contact Ford's AI/ML team to get:")
    print("  - Endpoint URL")
    print("  - API key")
    print("  - Model name")
    print()
    
    endpoint = input("Ford LLM Endpoint URL: ").strip()
    if not endpoint:
        print("⚠️  Using placeholder. Update llm_config.json with real endpoint.")
        endpoint = "https://ford-llm-api.ford.com/v1/completions"
    
    model = input("Model name (e.g., ford-diagnostic-v1): ").strip()
    if not model:
        model = "ford-diagnostic-v1"
    
    config['endpoint'] = endpoint
    config['model'] = model
    
    print()
    print("Note: Your API key should be set as environment variable FORD_LLM_API_KEY")


def configure_azure_openai(config: Dict):
    """Configure Azure OpenAI"""
    print("Azure OpenAI Configuration")
    print("-" * 70)
    print()
    print("Get these from Azure Portal > Azure OpenAI resource:")
    print()
    
    endpoint = input("Azure OpenAI Endpoint (e.g., https://ford-ai.openai.azure.com/): ").strip()
    deployment = input("Deployment name (e.g., gpt-4o): ").strip()
    model = input("Model name (same as deployment, usually): ").strip() or deployment
    
    config['endpoint'] = endpoint
    config['deployment_name'] = deployment
    config['model'] = model
    
    print()
    print("Note: Your API key should be set as environment variable AZURE_OPENAI_API_KEY")


def configure_aws_bedrock(config: Dict):
    """Configure AWS Bedrock"""
    print("AWS Bedrock Configuration")
    print("-" * 70)
    print()
    print("Available models:")
    print("  - anthropic.claude-3-5-sonnet-20241022-v2:0")
    print("  - anthropic.claude-3-haiku-20240307-v1:0")
    print("  - amazon.titan-text-express-v1")
    print()
    
    region = input("AWS Region (default: us-east-1): ").strip() or "us-east-1"
    model = input("Model ID (default: Claude 3.5 Sonnet): ").strip()
    if not model:
        model = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    
    config['region'] = region
    config['model'] = model
    
    print()
    print("Note: Set AWS credentials as environment variables:")
    print("  - AWS_ACCESS_KEY_ID")
    print("  - AWS_SECRET_ACCESS_KEY")


def configure_openai(config: Dict):
    """Configure OpenAI"""
    print("OpenAI Configuration")
    print("-" * 70)
    print()
    print("Available models:")
    print("  - gpt-4o (recommended)")
    print("  - gpt-4o-mini (faster, cheaper)")
    print("  - gpt-4-turbo")
    print()
    
    model = input("Model (default: gpt-4o): ").strip() or "gpt-4o"
    config['model'] = model
    
    print()
    print("Note: Get API key from https://platform.openai.com/api-keys")
    print("Set as environment variable: OPENAI_API_KEY")


def configure_anthropic(config: Dict):
    """Configure Anthropic"""
    print("Anthropic Configuration")
    print("-" * 70)
    print()
    print("Available models:")
    print("  - claude-3-5-sonnet-20241022 (recommended)")
    print("  - claude-3-opus-20240229")
    print("  - claude-3-haiku-20240307")
    print()
    
    model = input("Model (default: claude-3-5-sonnet-20241022): ").strip()
    if not model:
        model = "claude-3-5-sonnet-20241022"
    
    config['model'] = model
    
    print()
    print("Note: Get API key from https://console.anthropic.com/")
    print("Set as environment variable: ANTHROPIC_API_KEY")


def configure_custom(config: Dict):
    """Configure custom endpoint"""
    print("Custom Endpoint Configuration")
    print("-" * 70)
    print()
    
    endpoint = input("API Endpoint URL: ").strip()
    model = input("Model name: ").strip()
    
    config['endpoint'] = endpoint
    config['model'] = model
    
    print()
    print("Custom headers (optional):")
    print("Example: Authorization: Bearer YOUR_TOKEN")
    print()
    
    add_headers = input("Add custom headers? (y/n): ").strip().lower()
    if add_headers == 'y':
        headers = {}
        while True:
            key = input("Header name (or press Enter to finish): ").strip()
            if not key:
                break
            value = input(f"{key}: ").strip()
            headers[key] = value
        
        if headers:
            config['custom_headers'] = headers


def print_env_instructions(provider: str):
    """Print environment variable setup instructions"""
    print("=" * 70)
    print("NEXT STEP: SET YOUR API KEY")
    print("=" * 70)
    print()
    
    instructions = {
        'ford_llm': {
            'var': 'FORD_LLM_API_KEY',
            'description': 'Your Ford LLM API key from Ford IT'
        },
        'azure_openai': {
            'var': 'AZURE_OPENAI_API_KEY',
            'description': 'Your Azure OpenAI key from Azure Portal'
        },
        'aws_bedrock': {
            'var': 'AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY',
            'description': 'Your AWS credentials from AWS Console'
        },
        'openai': {
            'var': 'OPENAI_API_KEY',
            'description': 'Your OpenAI API key from platform.openai.com'
        },
        'anthropic': {
            'var': 'ANTHROPIC_API_KEY',
            'description': 'Your Anthropic API key from console.anthropic.com'
        },
        'custom': {
            'var': 'YOUR_API_KEY',
            'description': 'Your custom endpoint API key'
        }
    }
    
    info = instructions.get(provider, instructions['custom'])
    
    print(f"Environment Variable: {info['var']}")
    print(f"Description: {info['description']}")
    print()
    print("To set in PowerShell:")
    print()
    
    if provider == 'aws_bedrock':
        print('  $env:AWS_ACCESS_KEY_ID = "your-access-key"')
        print('  $env:AWS_SECRET_ACCESS_KEY = "your-secret-key"')
    else:
        print(f'  $env:{info["var"]} = "your-api-key-here"')
    
    print()
    print("Or permanently:")
    print()
    
    if provider == 'aws_bedrock':
        print('  [Environment]::SetEnvironmentVariable("AWS_ACCESS_KEY_ID", "your-key", "User")')
        print('  [Environment]::SetEnvironmentVariable("AWS_SECRET_ACCESS_KEY", "your-key", "User")')
    else:
        print(f'  [Environment]::SetEnvironmentVariable("{info["var"]}", "your-key", "User")')
    
    print()
    print("Then restart PowerShell and run:")
    print("  python professional_diagnostic_analyzer.py")
    print()


if __name__ == "__main__":
    create_llm_config()
