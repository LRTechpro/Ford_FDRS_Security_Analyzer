"""
Enterprise LLM Provider Support
Supports multiple LLM providers: OpenAI, Azure OpenAI, AWS Bedrock, Ford LLM, etc.
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class LLMProvider(Enum):
    """Supported LLM providers"""
    OPENAI = "openai"
    AZURE_OPENAI = "azure_openai"
    AWS_BEDROCK = "aws_bedrock"
    FORD_LLM = "ford_llm"
    ANTHROPIC = "anthropic"
    CUSTOM = "custom"


@dataclass
class LLMConfig:
    """LLM provider configuration"""
    provider: LLMProvider
    api_key: Optional[str] = None
    endpoint: Optional[str] = None
    model: str = "gpt-4o"
    max_tokens: int = 4000
    temperature: float = 0.3
    deployment_name: Optional[str] = None  # For Azure
    region: Optional[str] = None  # For AWS
    custom_headers: Optional[Dict[str, str]] = None


class EnterpriseLLMProvider:
    """Enterprise LLM provider with support for multiple backends"""
    
    def __init__(self, config: Optional[LLMConfig] = None):
        self.logger = logging.getLogger(__name__)
        self.config = config or self._load_config()
        self.client = None
        self._initialize_provider()
    
    def _load_config(self) -> LLMConfig:
        """Load LLM configuration from file or environment"""
        config_path = 'llm_config.json'
        
        # Try to load from config file
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    data = json.load(f)
                    provider = LLMProvider(data.get('provider', 'openai'))
                    return LLMConfig(
                        provider=provider,
                        api_key=data.get('api_key'),
                        endpoint=data.get('endpoint'),
                        model=data.get('model', 'gpt-4o'),
                        max_tokens=data.get('max_tokens', 4000),
                        temperature=data.get('temperature', 0.3),
                        deployment_name=data.get('deployment_name'),
                        region=data.get('region'),
                        custom_headers=data.get('custom_headers')
                    )
            except Exception as e:
                self.logger.error(f"Error loading LLM config: {e}")
        
        # Default to OpenAI
        return LLMConfig(
            provider=LLMProvider.OPENAI,
            api_key=os.getenv('OPENAI_API_KEY'),
            model='gpt-4o'
        )
    
    def _initialize_provider(self):
        """Initialize the LLM provider client"""
        try:
            if self.config.provider == LLMProvider.OPENAI:
                self._initialize_openai()
            elif self.config.provider == LLMProvider.AZURE_OPENAI:
                self._initialize_azure_openai()
            elif self.config.provider == LLMProvider.AWS_BEDROCK:
                self._initialize_aws_bedrock()
            elif self.config.provider == LLMProvider.FORD_LLM:
                self._initialize_ford_llm()
            elif self.config.provider == LLMProvider.ANTHROPIC:
                self._initialize_anthropic()
            elif self.config.provider == LLMProvider.CUSTOM:
                self._initialize_custom()
        except Exception as e:
            self.logger.error(f"Error initializing LLM provider: {e}")
            self.client = None
    
    def _initialize_openai(self):
        """Initialize OpenAI client"""
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=self.config.api_key)
            self.logger.info("OpenAI client initialized")
        except ImportError:
            self.logger.error("OpenAI package not installed. Run: pip install openai")
        except Exception as e:
            self.logger.error(f"Error initializing OpenAI: {e}")
    
    def _initialize_azure_openai(self):
        """Initialize Azure OpenAI client"""
        try:
            from openai import AzureOpenAI
            self.client = AzureOpenAI(
                api_key=self.config.api_key,
                api_version="2024-02-01",
                azure_endpoint=self.config.endpoint
            )
            self.logger.info("Azure OpenAI client initialized")
        except ImportError:
            self.logger.error("OpenAI package not installed. Run: pip install openai")
        except Exception as e:
            self.logger.error(f"Error initializing Azure OpenAI: {e}")
    
    def _initialize_aws_bedrock(self):
        """Initialize AWS Bedrock client"""
        try:
            import boto3
            self.client = boto3.client(
                'bedrock-runtime',
                region_name=self.config.region or 'us-east-1'
            )
            self.logger.info("AWS Bedrock client initialized")
        except ImportError:
            self.logger.error("boto3 not installed. Run: pip install boto3")
        except Exception as e:
            self.logger.error(f"Error initializing AWS Bedrock: {e}")
    
    def _initialize_ford_llm(self):
        """Initialize Ford LLM client"""
        # Ford may have their own LLM API endpoint
        # This is a placeholder - needs Ford's actual API specifications
        try:
            import requests
            self.client = {
                'endpoint': self.config.endpoint or os.getenv('FORD_LLM_ENDPOINT'),
                'api_key': self.config.api_key or os.getenv('FORD_LLM_API_KEY'),
                'headers': self.config.custom_headers or {
                    'Authorization': f'Bearer {self.config.api_key}',
                    'Content-Type': 'application/json'
                }
            }
            self.logger.info("Ford LLM client initialized")
        except Exception as e:
            self.logger.error(f"Error initializing Ford LLM: {e}")
    
    def _initialize_anthropic(self):
        """Initialize Anthropic (Claude) client"""
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.config.api_key)
            self.logger.info("Anthropic client initialized")
        except ImportError:
            self.logger.error("Anthropic package not installed. Run: pip install anthropic")
        except Exception as e:
            self.logger.error(f"Error initializing Anthropic: {e}")
    
    def _initialize_custom(self):
        """Initialize custom LLM endpoint"""
        # Generic REST API client for custom endpoints
        try:
            import requests
            self.client = {
                'endpoint': self.config.endpoint,
                'headers': self.config.custom_headers or {}
            }
            self.logger.info("Custom LLM client initialized")
        except Exception as e:
            self.logger.error(f"Error initializing custom LLM: {e}")
    
    def generate_completion(self, prompt: str, system_prompt: Optional[str] = None) -> Optional[str]:
        """Generate completion using configured LLM provider"""
        if not self.client:
            self.logger.error("LLM client not initialized")
            return None
        
        try:
            if self.config.provider == LLMProvider.OPENAI:
                return self._generate_openai(prompt, system_prompt)
            elif self.config.provider == LLMProvider.AZURE_OPENAI:
                return self._generate_azure_openai(prompt, system_prompt)
            elif self.config.provider == LLMProvider.AWS_BEDROCK:
                return self._generate_aws_bedrock(prompt, system_prompt)
            elif self.config.provider == LLMProvider.FORD_LLM:
                return self._generate_ford_llm(prompt, system_prompt)
            elif self.config.provider == LLMProvider.ANTHROPIC:
                return self._generate_anthropic(prompt, system_prompt)
            elif self.config.provider == LLMProvider.CUSTOM:
                return self._generate_custom(prompt, system_prompt)
        except Exception as e:
            self.logger.error(f"Error generating completion: {e}")
            return None
    
    def _generate_openai(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using OpenAI"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=messages,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        return response.choices[0].message.content
    
    def _generate_azure_openai(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using Azure OpenAI"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.config.deployment_name or self.config.model,
            messages=messages,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature
        )
        return response.choices[0].message.content
    
    def _generate_aws_bedrock(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using AWS Bedrock"""
        import json
        
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        # Format depends on the model (Claude, Llama, etc.)
        body = json.dumps({
            "prompt": full_prompt,
            "max_tokens_to_sample": self.config.max_tokens,
            "temperature": self.config.temperature
        })
        
        response = self.client.invoke_model(
            modelId=self.config.model,
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        return response_body.get('completion', '')
    
    def _generate_ford_llm(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using Ford LLM"""
        import requests
        
        # This is a placeholder - actual implementation depends on Ford's API
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        payload = {
            "prompt": full_prompt,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
            "model": self.config.model
        }
        
        response = requests.post(
            self.client['endpoint'],
            headers=self.client['headers'],
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        
        data = response.json()
        return data.get('completion', data.get('response', ''))
    
    def _generate_anthropic(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using Anthropic Claude"""
        message = self.client.messages.create(
            model=self.config.model or "claude-3-5-sonnet-20241022",
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=system_prompt or "",
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    
    def _generate_custom(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate completion using custom endpoint"""
        import requests
        
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        payload = {
            "prompt": full_prompt,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature
        }
        
        response = requests.post(
            self.client['endpoint'],
            headers=self.client['headers'],
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        
        return response.json().get('completion', '')
    
    def is_available(self) -> bool:
        """Check if LLM provider is available"""
        return self.client is not None
    
    def save_config(self):
        """Save LLM configuration to file"""
        config_data = {
            'provider': self.config.provider.value,
            'endpoint': self.config.endpoint,
            'model': self.config.model,
            'max_tokens': self.config.max_tokens,
            'temperature': self.config.temperature,
            'deployment_name': self.config.deployment_name,
            'region': self.config.region,
            'custom_headers': self.config.custom_headers
        }
        
        # Don't save API key in file for security
        # API keys should come from environment variables
        
        try:
            with open('llm_config.json', 'w') as f:
                json.dump(config_data, f, indent=2)
            self.logger.info("LLM configuration saved")
        except Exception as e:
            self.logger.error(f"Error saving LLM config: {e}")


# Configuration templates for different providers
PROVIDER_TEMPLATES = {
    'openai': {
        'provider': 'openai',
        'model': 'gpt-4o',
        'env_vars': ['OPENAI_API_KEY']
    },
    'azure_openai': {
        'provider': 'azure_openai',
        'model': 'gpt-4o',
        'endpoint': 'https://YOUR-RESOURCE.openai.azure.com/',
        'deployment_name': 'gpt-4o',
        'env_vars': ['AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_ENDPOINT']
    },
    'aws_bedrock': {
        'provider': 'aws_bedrock',
        'model': 'anthropic.claude-3-5-sonnet-20241022-v2:0',
        'region': 'us-east-1',
        'env_vars': ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']
    },
    'ford_llm': {
        'provider': 'ford_llm',
        'model': 'ford-diagnostic-model',  # Placeholder
        'endpoint': 'https://ford-llm-api.ford.com/v1/completions',  # Placeholder
        'env_vars': ['FORD_LLM_API_KEY', 'FORD_LLM_ENDPOINT']
    },
    'anthropic': {
        'provider': 'anthropic',
        'model': 'claude-3-5-sonnet-20241022',
        'env_vars': ['ANTHROPIC_API_KEY']
    }
}
