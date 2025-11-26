"""
AI-Powered Diagnostic Assistant
Integrates OpenAI ChatGPT for advanced natural language analysis and insights
"""

import os
import json
import logging
import asyncio
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import tkinter as tk
from tkinter import messagebox
from dataclasses import dataclass
try:
    import openai
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    openai = None
    OpenAI = None
import threading


@dataclass
class AIAnalysisRequest:
    """AI analysis request structure"""
    request_id: str
    content: str
    analysis_type: str
    context: Dict[str, Any]
    timestamp: datetime


@dataclass
class AIAnalysisResult:
    """AI analysis result structure"""
    request_id: str
    analysis: str
    confidence: float
    key_findings: List[str]
    recommendations: List[str]
    technical_insights: List[str]
    risk_assessment: str
    next_steps: List[str]
    timestamp: datetime
    tokens_used: int


class AIDiagnosticAssistant:
    """AI-powered diagnostic assistant using OpenAI"""
    
    def __init__(self, model: str = "gpt-4o"):
        self.logger = logging.getLogger(__name__ + '.AIDiagnosticAssistant')
        self.client = None
        self.api_key = None
        # Default to gpt-4o (most capable), with support for gpt-4o-mini and future gpt-5
        self.model = model  
        self.available_models = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-5"]  # gpt-5 when available
        self.max_tokens = 4000  # Increased for more comprehensive analysis
        self.temperature = 0.3  # Lower temperature for more consistent technical analysis
        
        # Check if OpenAI is available
        if not OPENAI_AVAILABLE:
            self.logger.warning("OpenAI package not available. AI features will be disabled.")
            return
        
        # Load API key
        self._load_api_key()
    
    def _load_api_key(self):
        """Load OpenAI API key from environment or config"""
        # Try environment variable first
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        if not self.api_key:
            # Try loading from config file
            try:
                config_path = 'ai_config.json'
                if os.path.exists(config_path):
                    with open(config_path, 'r') as f:
                        config = json.load(f)
                        self.api_key = config.get('openai_api_key')
            except Exception as e:
                self.logger.error(f"Error loading AI config: {e}")
        
        if self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
                self.logger.info("OpenAI client initialized successfully")
            except Exception as e:
                self.logger.error(f"Error initializing OpenAI client: {e}")
                self.client = None
        else:
            self.logger.warning("No OpenAI API key found. AI features will be disabled.")
    
    def is_available(self) -> bool:
        """Check if AI assistant is available"""
        return OPENAI_AVAILABLE and self.client is not None
    
    def set_api_key(self, api_key: str) -> bool:
        """Set OpenAI API key"""
        if not OPENAI_AVAILABLE:
            self.logger.error("OpenAI package not available")
            return False
            
        try:
            self.api_key = api_key
            self.client = OpenAI(api_key=api_key)
            
            # Save to config file
            config = {'openai_api_key': api_key}
            with open('ai_config.json', 'w') as f:
                json.dump(config, f, indent=2)
            
            self.logger.info("OpenAI API key set and client initialized")
            return True
        except Exception as e:
            self.logger.error(f"Error setting API key: {e}")
            return False
    
    def analyze_diagnostic_log(self, log_content: str, context: Dict[str, Any] = None) -> AIAnalysisResult:
        """Analyze diagnostic log using AI"""
        if not self.is_available():
            raise Exception("AI assistant not available. Please configure OpenAI API key.")
        
        request_id = f"ai_req_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        # Prepare context information
        context_info = ""
        if context:
            context_info = f"""
CONTEXT INFORMATION:
- Vehicle: {context.get('vehicle', 'Unknown')}
- VIN: {context.get('vin', 'Unknown')}  
- Module: {context.get('module', 'Unknown')}
- Analysis Type: {context.get('analysis_type', 'diagnostic')}
- Technician: {context.get('technician', 'Unknown')}
"""
        
        # Create comprehensive prompt for diagnostic analysis
        system_prompt = """You are an expert automotive diagnostic technician with decades of experience in Ford vehicle systems, FDRS diagnostic tools, and ECU programming. You specialize in analyzing diagnostic logs and determining root causes of issues.

Your task is to analyze diagnostic logs and provide professional insights including:
1. Clear assessment of success/failure status
2. Technical explanation of what occurred
3. Risk assessment and potential impacts
4. Specific recommendations for next steps
5. Root cause analysis when issues are present

Focus on:
- ECU communication patterns
- Error codes and their meanings
- Programming/update sequences
- System responses and behaviors
- Verification procedures
- Post-update validation

Provide responses in a professional, technical format suitable for service documentation."""

        user_prompt = f"""Please analyze this automotive diagnostic log and provide comprehensive insights:

{context_info}

DIAGNOSTIC LOG CONTENT:
{log_content}

Please provide:
1. OVERALL ASSESSMENT: Clear success/failure determination
2. TECHNICAL ANALYSIS: What happened during this diagnostic session
3. KEY FINDINGS: Important observations and discoveries
4. RISK ASSESSMENT: Potential issues or concerns
5. RECOMMENDATIONS: Specific next steps and actions
6. ROOT CAUSE: If issues exist, what caused them
7. CONFIDENCE LEVEL: Your confidence in this analysis (0-100%)

Format your response professionally for automotive service documentation."""

        try:
            # Make API call to OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # Extract response content
            analysis_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
            # Parse the response to extract structured information
            parsed_result = self._parse_ai_response(analysis_text)
            
            # Create result object
            result = AIAnalysisResult(
                request_id=request_id,
                analysis=analysis_text,
                confidence=parsed_result.get('confidence', 75.0),
                key_findings=parsed_result.get('key_findings', []),
                recommendations=parsed_result.get('recommendations', []),
                technical_insights=parsed_result.get('technical_insights', []),
                risk_assessment=parsed_result.get('risk_assessment', 'Medium'),
                next_steps=parsed_result.get('next_steps', []),
                timestamp=datetime.now(),
                tokens_used=tokens_used
            )
            
            self.logger.info(f"AI analysis completed. Request ID: {request_id}, Tokens used: {tokens_used}")
            return result
            
        except Exception as e:
            self.logger.error(f"AI analysis error: {e}")
            raise
    
    def _parse_ai_response(self, response: str) -> Dict[str, Any]:
        """Parse AI response to extract structured information"""
        parsed = {
            'confidence': 75.0,
            'key_findings': [],
            'recommendations': [],
            'technical_insights': [],
            'risk_assessment': 'Medium',
            'next_steps': []
        }
        
        try:
            lines = response.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                
                # Detect sections
                if 'CONFIDENCE' in line.upper() or 'CONFIDENCE LEVEL' in line.upper():
                    # Extract confidence percentage
                    import re
                    confidence_match = re.search(r'(\d+)%', line)
                    if confidence_match:
                        parsed['confidence'] = float(confidence_match.group(1))
                
                elif 'KEY FINDINGS' in line.upper():
                    current_section = 'key_findings'
                elif 'RECOMMENDATIONS' in line.upper():
                    current_section = 'recommendations'
                elif 'TECHNICAL ANALYSIS' in line.upper() or 'TECHNICAL' in line.upper():
                    current_section = 'technical_insights'
                elif 'RISK ASSESSMENT' in line.upper():
                    current_section = 'risk_assessment'
                elif 'NEXT STEPS' in line.upper():
                    current_section = 'next_steps'
                elif line.startswith('**') or line.startswith('#'):
                    current_section = None
                
                # Extract content based on current section
                elif current_section and line:
                    if line.startswith('-') or line.startswith('•') or line.startswith('*'):
                        # List item
                        item = line.lstrip('-•* ').strip()
                        if item and current_section in ['key_findings', 'recommendations', 'technical_insights', 'next_steps']:
                            parsed[current_section].append(item)
                    elif current_section == 'risk_assessment' and not line.startswith('-'):
                        # Risk assessment text
                        if 'LOW' in line.upper():
                            parsed['risk_assessment'] = 'Low'
                        elif 'HIGH' in line.upper():
                            parsed['risk_assessment'] = 'High'
                        elif 'CRITICAL' in line.upper():
                            parsed['risk_assessment'] = 'Critical'
                        else:
                            parsed['risk_assessment'] = 'Medium'
            
        except Exception as e:
            self.logger.error(f"Error parsing AI response: {e}")
        
        return parsed
    
    def analyze_multi_source_evidence(self, documents: List[Dict[str, Any]], question: str = None) -> AIAnalysisResult:
        """Analyze multiple evidence sources with AI"""
        if not self.is_available():
            raise Exception("AI assistant not available. Please configure OpenAI API key.")
        
        request_id = f"multi_ai_req_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        # Prepare document summaries
        doc_summaries = []
        for i, doc in enumerate(documents, 1):
            summary = f"""
DOCUMENT {i}: {doc.get('filename', 'Unknown')}
Type: {doc.get('doc_type', 'Unknown')}
Size: {doc.get('file_size', 0)} bytes
Key Findings: {', '.join(doc.get('key_findings', []))}

Content Preview:
{doc.get('extracted_text', '')[:1000]}{'...' if len(doc.get('extracted_text', '')) > 1000 else ''}
"""
            doc_summaries.append(summary)
        
        # Create comprehensive multi-source analysis prompt
        system_prompt = """You are an expert automotive diagnostic analyst with advanced training in multi-source evidence correlation. You excel at analyzing multiple types of evidence (system logs, health reports, work orders, screenshots, technical documents) to provide comprehensive diagnostic conclusions.

Your expertise includes:
- Cross-referencing information from multiple sources
- Identifying patterns and correlations
- Detecting contradictions or inconsistencies
- Providing evidence-based conclusions
- Risk assessment and impact analysis
- Technical root cause analysis

Provide professional, detailed analysis suitable for automotive service documentation and expert testimony."""

        analysis_question = question or "Based on all available evidence, what is the comprehensive diagnostic conclusion regarding the update/repair outcome?"
        
        user_prompt = f"""Please analyze these multiple evidence sources and provide a comprehensive diagnostic conclusion:

ANALYSIS QUESTION: {analysis_question}

EVIDENCE SOURCES:
{''.join(doc_summaries)}

Please provide:
1. COMPREHENSIVE CONCLUSION: Overall assessment based on all evidence
2. EVIDENCE CORRELATION: How the different sources support or contradict each other
3. CONFIDENCE ASSESSMENT: Your confidence level and reasoning
4. KEY TECHNICAL FINDINGS: Important technical discoveries
5. RISK ANALYSIS: Potential risks or concerns identified
6. EXPERT RECOMMENDATIONS: Professional recommendations based on findings
7. CONTRADICTIONS: Any conflicting information that needs resolution
8. NEXT STEPS: Specific actions recommended

Consider the reliability and relevance of each evidence source in your analysis."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            analysis_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            parsed_result = self._parse_ai_response(analysis_text)
            
            result = AIAnalysisResult(
                request_id=request_id,
                analysis=analysis_text,
                confidence=parsed_result.get('confidence', 80.0),
                key_findings=parsed_result.get('key_findings', []),
                recommendations=parsed_result.get('recommendations', []),
                technical_insights=parsed_result.get('technical_insights', []),
                risk_assessment=parsed_result.get('risk_assessment', 'Medium'),
                next_steps=parsed_result.get('next_steps', []),
                timestamp=datetime.now(),
                tokens_used=tokens_used
            )
            
            self.logger.info(f"Multi-source AI analysis completed. Request ID: {request_id}, Tokens used: {tokens_used}")
            return result
            
        except Exception as e:
            self.logger.error(f"Multi-source AI analysis error: {e}")
            raise
    
    def ask_diagnostic_question(self, question: str, context: Dict[str, Any] = None) -> str:
        """Ask a specific diagnostic question"""
        if not self.is_available():
            raise Exception("AI assistant not available. Please configure OpenAI API key.")
        
        context_info = ""
        if context:
            context_info = f"Context: {json.dumps(context, indent=2)}"
        
        system_prompt = """You are an expert Ford automotive diagnostic technician and trainer. Answer diagnostic questions with technical accuracy and practical insights. Provide specific, actionable advice based on automotive diagnostic best practices."""
        
        user_prompt = f"""Diagnostic Question: {question}

{context_info}

Please provide a comprehensive answer including technical details, potential causes, diagnostic steps, and recommendations."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=1000,
                temperature=0.4
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Diagnostic Q&A error: {e}")
            raise
    
    def generate_diagnostic_report(self, analysis_data: Dict[str, Any]) -> str:
        """Generate a professional diagnostic report using AI"""
        if not self.is_available():
            raise Exception("AI assistant not available. Please configure OpenAI API key.")
        
        system_prompt = """You are an expert automotive technical writer specializing in diagnostic reports. Create professional, detailed diagnostic reports suitable for service documentation, warranty claims, and technical communication."""
        
        user_prompt = f"""Please generate a professional diagnostic report based on this analysis data:

{json.dumps(analysis_data, indent=2, default=str)}

Format the report professionally with:
- Executive Summary
- Technical Findings
- Diagnostic Procedures Performed
- Evidence Analysis
- Conclusions and Recommendations
- Supporting Documentation References

Use automotive industry standard terminology and formatting."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2000,
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Report generation error: {e}")
            raise
    
    def explain_error_code(self, error_code: str, context: str = "") -> str:
        """Get AI explanation of error codes"""
        if not self.is_available():
            raise Exception("AI assistant not available. Please configure OpenAI API key.")
        
        system_prompt = """You are an expert in automotive diagnostic trouble codes (DTCs) and error codes. Provide detailed explanations including causes, symptoms, diagnostic procedures, and repair recommendations."""
        
        user_prompt = f"""Please explain this automotive error code in detail:

Error Code: {error_code}
Context: {context}

Include:
- Code meaning and description
- Common causes
- Symptoms experienced
- Diagnostic procedures
- Repair recommendations
- Prevention measures"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=1500,
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error code explanation error: {e}")
            raise