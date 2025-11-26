"""
Intelligent Multi-Source Diagnostic Analyzer
Advanced system that correlates multiple data sources to provide clear pass/fail conclusions
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import hashlib
import base64
from dataclasses import dataclass, asdict
import re


@dataclass
class DocumentReference:
    """Document reference with metadata"""
    doc_id: str
    filename: str
    filepath: str
    doc_type: str  # 'system_log', 'health_report', 'work_order', 'screenshot', 'technical_doc'
    upload_time: datetime
    file_size: int
    checksum: str
    description: str = ""
    extracted_text: str = ""
    key_findings: List[str] = None
    
    def __post_init__(self):
        if self.key_findings is None:
            self.key_findings = []


@dataclass
class AnalysisConclusion:
    """Analysis conclusion with evidence"""
    conclusion: str  # "PASSED", "FAILED", "INCONCLUSIVE"
    confidence_score: float  # 0-100
    primary_evidence: List[str]
    supporting_evidence: List[str]
    contradictory_evidence: List[str]
    reasoning: str
    recommendations: List[str]
    sources_referenced: List[str]
    timestamp: datetime


class IntelligentDiagnosticEngine:
    """Advanced diagnostic engine with multi-source analysis"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.documents: Dict[str, DocumentReference] = {}
        self.knowledge_base = self._initialize_knowledge_base()
        self.analysis_patterns = self._initialize_analysis_patterns()
        
        # Document storage
        self.doc_storage_dir = Path("document_storage")
        self.doc_storage_dir.mkdir(exist_ok=True)
        
        # Load existing documents
        self._load_existing_documents()
    
    def _initialize_knowledge_base(self) -> Dict[str, Any]:
        """Initialize diagnostic knowledge base"""
        return {
            "update_success_indicators": [
                "update completed successfully",
                "programming successful",
                "flash complete",
                "calibration updated",
                "software version updated",
                "update verified",
                "positive response",
                "operation complete"
            ],
            "update_failure_indicators": [
                "update failed",
                "programming error",
                "flash failed",
                "timeout during update",
                "negative response code",
                "communication lost",
                "verification failed",
                "checksum error",
                "nrc",
                "abort",
                "error code"
            ],
            "critical_error_codes": [
                "NRC 31", "NRC 33", "NRC 35", "NRC 36", "NRC 37",
                "P0601", "P0602", "P0603", "P0604", "P0605",
                "U0001", "U0100", "U0101", "U0102", "U0103"
            ],
            "ecu_modules": {
                "PCM": "Powertrain Control Module",
                "ABS": "Anti-lock Braking System",
                "BCM": "Body Control Module",
                "TCM": "Transmission Control Module",
                "RCM": "Restraint Control Module",
                "IPC": "Instrument Panel Cluster",
                "HVAC": "Climate Control Module",
                "PAM": "Parking Aid Module"
            }
        }
    
    def _initialize_analysis_patterns(self) -> Dict[str, Any]:
        """Initialize analysis patterns for different scenarios"""
        return {
            "software_update": {
                "required_evidence": ["update_start", "update_progress", "update_completion"],
                "success_threshold": 0.8,
                "critical_failures": ["communication_lost", "flash_error", "verification_failed"]
            },
            "calibration_update": {
                "required_evidence": ["calibration_start", "data_transfer", "verification"],
                "success_threshold": 0.75,
                "critical_failures": ["checksum_error", "data_corruption", "timeout"]
            },
            "diagnostic_test": {
                "required_evidence": ["test_start", "test_execution", "test_results"],
                "success_threshold": 0.85,
                "critical_failures": ["test_abort", "communication_error", "invalid_response"]
            }
        }
    
    def add_document(self, filepath: str, doc_type: str, description: str = "") -> str:
        """Add a document to the analysis system"""
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Document not found: {filepath}")
            
            # Generate document ID
            doc_id = self._generate_doc_id(filepath)
            
            # Calculate file checksum
            checksum = self._calculate_checksum(filepath)
            
            # Copy document to storage
            filename = os.path.basename(filepath)
            storage_path = self.doc_storage_dir / f"{doc_id}_{filename}"
            
            # Copy file to storage
            import shutil
            shutil.copy2(filepath, storage_path)
            
            # Extract text content
            extracted_text = self._extract_text_content(filepath, doc_type)
            
            # Extract key findings
            key_findings = self._extract_key_findings(extracted_text, doc_type)
            
            # Create document reference
            doc_ref = DocumentReference(
                doc_id=doc_id,
                filename=filename,
                filepath=str(storage_path),
                doc_type=doc_type,
                upload_time=datetime.now(),
                file_size=os.path.getsize(filepath),
                checksum=checksum,
                description=description,
                extracted_text=extracted_text,
                key_findings=key_findings
            )
            
            # Store document
            self.documents[doc_id] = doc_ref
            
            # Save document index
            self._save_document_index()
            
            self.logger.info(f"Added document: {filename} ({doc_type})")
            return doc_id
            
        except Exception as e:
            self.logger.error(f"Error adding document: {e}")
            raise
    
    def _generate_doc_id(self, filepath: str) -> str:
        """Generate unique document ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_hash = hashlib.md5(filepath.encode()).hexdigest()[:8]
        return f"doc_{timestamp}_{file_hash}"
    
    def _calculate_checksum(self, filepath: str) -> str:
        """Calculate file checksum"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _extract_text_content(self, filepath: str, doc_type: str) -> str:
        """Extract text content from various file types"""
        try:
            file_ext = os.path.splitext(filepath)[1].lower()
            
            if file_ext in ['.txt', '.log', '.xml']:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()
            
            elif file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
                # For screenshots, we'll extract any embedded text or return metadata
                return f"Screenshot file: {os.path.basename(filepath)}\nType: Image\nSize: {os.path.getsize(filepath)} bytes"
            
            elif file_ext == '.pdf':
                # Would implement PDF text extraction here
                return f"PDF document: {os.path.basename(filepath)}\nRequires PDF processing"
            
            elif file_ext in ['.doc', '.docx']:
                # Would implement Word document processing here
                return f"Word document: {os.path.basename(filepath)}\nRequires document processing"
            
            else:
                return f"Binary file: {os.path.basename(filepath)}\nType: {doc_type}"
                
        except Exception as e:
            self.logger.error(f"Error extracting text from {filepath}: {e}")
            return f"Error reading file: {str(e)}"
    
    def _extract_key_findings(self, text: str, doc_type: str) -> List[str]:
        """Extract key findings from document text"""
        findings = []
        text_lower = text.lower()
        
        # Common patterns based on document type
        if doc_type == 'system_log':
            # Look for update-related findings
            if any(indicator in text_lower for indicator in self.knowledge_base["update_success_indicators"]):
                findings.append("Update success indicators found")
            
            if any(indicator in text_lower for indicator in self.knowledge_base["update_failure_indicators"]):
                findings.append("Update failure indicators detected")
            
            # Look for error codes
            for error_code in self.knowledge_base["critical_error_codes"]:
                if error_code.lower() in text_lower:
                    findings.append(f"Critical error code detected: {error_code}")
        
        elif doc_type == 'health_report':
            # Look for system health indicators
            if "fault" in text_lower or "error" in text_lower:
                findings.append("System faults or errors reported")
            if "normal" in text_lower or "pass" in text_lower:
                findings.append("Normal system operation indicators")
        
        elif doc_type == 'work_order':
            # Look for work performed
            if "replaced" in text_lower or "repaired" in text_lower:
                findings.append("Component replacement or repair performed")
            if "updated" in text_lower or "programmed" in text_lower:
                findings.append("Software update or programming performed")
        
        return findings
    
    def analyze_update_outcome(self, analysis_type: str = "software_update") -> AnalysisConclusion:
        """Analyze all documents to determine update outcome"""
        try:
            self.logger.info(f"Starting intelligent analysis for {analysis_type}")
            
            # Collect evidence from all documents
            primary_evidence = []
            supporting_evidence = []
            contradictory_evidence = []
            sources_referenced = []
            
            # Analyze each document
            for doc_id, doc_ref in self.documents.items():
                evidence, source_info = self._analyze_document_for_evidence(doc_ref, analysis_type)
                
                for item in evidence["primary"]:
                    primary_evidence.append(f"{item} (Source: {doc_ref.filename})")
                
                for item in evidence["supporting"]:
                    supporting_evidence.append(f"{item} (Source: {doc_ref.filename})")
                
                for item in evidence["contradictory"]:
                    contradictory_evidence.append(f"{item} (Source: {doc_ref.filename})")
                
                if evidence["primary"] or evidence["supporting"] or evidence["contradictory"]:
                    sources_referenced.append(f"{doc_ref.filename} ({doc_ref.doc_type})")
            
            # Make conclusion based on evidence
            conclusion, confidence, reasoning = self._make_conclusion(
                primary_evidence, supporting_evidence, contradictory_evidence, analysis_type
            )
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                conclusion, primary_evidence, contradictory_evidence
            )
            
            # Create analysis conclusion
            analysis_result = AnalysisConclusion(
                conclusion=conclusion,
                confidence_score=confidence,
                primary_evidence=primary_evidence,
                supporting_evidence=supporting_evidence,
                contradictory_evidence=contradictory_evidence,
                reasoning=reasoning,
                recommendations=recommendations,
                sources_referenced=sources_referenced,
                timestamp=datetime.now()
            )
            
            self.logger.info(f"Analysis complete: {conclusion} (Confidence: {confidence:.1f}%)")
            return analysis_result
            
        except Exception as e:
            self.logger.error(f"Error during analysis: {e}")
            raise
    
    def _analyze_document_for_evidence(self, doc_ref: DocumentReference, analysis_type: str) -> Tuple[Dict[str, List[str]], str]:
        """Analyze individual document for evidence"""
        evidence = {"primary": [], "supporting": [], "contradictory": []}
        text = doc_ref.extracted_text.lower()
        
        if analysis_type == "software_update":
            # Primary evidence (strong indicators)
            if any(indicator in text for indicator in self.knowledge_base["update_success_indicators"]):
                evidence["primary"].append("Update success confirmation found")
            
            if any(indicator in text for indicator in self.knowledge_base["update_failure_indicators"]):
                evidence["primary"].append("Update failure indication detected")
            
            # Supporting evidence
            if "programming" in text and "complete" in text:
                evidence["supporting"].append("Programming completion referenced")
            
            if "verification" in text and ("pass" in text or "success" in text):
                evidence["supporting"].append("Verification passed")
            
            # Contradictory evidence
            if "success" in text and "error" in text:
                evidence["contradictory"].append("Mixed success/error indicators")
            
            # Check for critical error codes
            for error_code in self.knowledge_base["critical_error_codes"]:
                if error_code.lower() in text:
                    evidence["primary"].append(f"Critical error code found: {error_code}")
        
        return evidence, f"{doc_ref.filename} ({doc_ref.doc_type})"
    
    def _make_conclusion(self, primary_evidence: List[str], supporting_evidence: List[str], 
                       contradictory_evidence: List[str], analysis_type: str) -> Tuple[str, float, str]:
        """Make final conclusion based on evidence"""
        
        # Count evidence types
        success_indicators = len([e for e in primary_evidence if "success" in e.lower() or "pass" in e.lower()])
        failure_indicators = len([e for e in primary_evidence if "fail" in e.lower() or "error" in e.lower()])
        contradictory_count = len(contradictory_evidence)
        
        # Calculate confidence based on evidence strength
        total_evidence = len(primary_evidence) + len(supporting_evidence)
        base_confidence = min(95, total_evidence * 15)  # Base confidence from evidence volume
        
        # Adjust for contradictory evidence
        confidence_penalty = contradictory_count * 10
        confidence = max(30, base_confidence - confidence_penalty)
        
        # Make conclusion
        if failure_indicators > success_indicators:
            conclusion = "FAILED"
            reasoning = f"Analysis indicates update failure based on {failure_indicators} failure indicators vs {success_indicators} success indicators"
        elif success_indicators > failure_indicators:
            conclusion = "PASSED"
            reasoning = f"Analysis indicates update success based on {success_indicators} success indicators vs {failure_indicators} failure indicators"
        else:
            conclusion = "INCONCLUSIVE"
            reasoning = f"Mixed or insufficient evidence: {success_indicators} success vs {failure_indicators} failure indicators"
            confidence = min(confidence, 60)  # Cap confidence for inconclusive results
        
        # Account for contradictory evidence in reasoning
        if contradictory_count > 0:
            reasoning += f". However, {contradictory_count} contradictory indicators require investigation"
        
        return conclusion, confidence, reasoning
    
    def _generate_recommendations(self, conclusion: str, primary_evidence: List[str], 
                                contradictory_evidence: List[str]) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if conclusion == "FAILED":
            recommendations.append("Immediate action required - update has failed")
            recommendations.append("Review system logs for specific error codes and root cause")
            recommendations.append("Verify ECU communication before retry")
            recommendations.append("Check for any TSBs or known issues for this update")
        
        elif conclusion == "PASSED":
            recommendations.append("Update appears successful - verify functionality")
            recommendations.append("Perform post-update validation tests")
            recommendations.append("Document successful update in service records")
        
        elif conclusion == "INCONCLUSIVE":
            recommendations.append("Additional verification required")
            recommendations.append("Gather more diagnostic evidence")
            recommendations.append("Consider re-running update process with enhanced logging")
        
        if contradictory_evidence:
            recommendations.append("Investigate contradictory evidence before final conclusion")
        
        return recommendations
    
    def _save_document_index(self):
        """Save document index to file"""
        try:
            index_file = self.doc_storage_dir / "document_index.json"
            index_data = {
                doc_id: asdict(doc_ref) for doc_id, doc_ref in self.documents.items()
            }
            
            with open(index_file, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, default=str)
                
        except Exception as e:
            self.logger.error(f"Error saving document index: {e}")
    
    def _load_existing_documents(self):
        """Load existing documents from index"""
        try:
            index_file = self.doc_storage_dir / "document_index.json"
            if index_file.exists():
                with open(index_file, 'r', encoding='utf-8') as f:
                    index_data = json.load(f)
                
                for doc_id, doc_data in index_data.items():
                    # Convert datetime strings back to datetime objects
                    doc_data['upload_time'] = datetime.fromisoformat(doc_data['upload_time'])
                    self.documents[doc_id] = DocumentReference(**doc_data)
                
                self.logger.info(f"Loaded {len(self.documents)} existing documents")
                
        except Exception as e:
            self.logger.error(f"Error loading existing documents: {e}")
    
    def get_document_summary(self) -> Dict[str, Any]:
        """Get summary of all documents"""
        summary = {
            "total_documents": len(self.documents),
            "by_type": {},
            "total_size": 0,
            "documents": []
        }
        
        for doc_ref in self.documents.values():
            # Count by type
            if doc_ref.doc_type not in summary["by_type"]:
                summary["by_type"][doc_ref.doc_type] = 0
            summary["by_type"][doc_ref.doc_type] += 1
            
            # Add to total size
            summary["total_size"] += doc_ref.file_size
            
            # Add document info
            summary["documents"].append({
                "filename": doc_ref.filename,
                "type": doc_ref.doc_type,
                "size": doc_ref.file_size,
                "upload_time": doc_ref.upload_time.strftime("%Y-%m-%d %H:%M:%S"),
                "key_findings_count": len(doc_ref.key_findings)
            })
        
        return summary
    
    def remove_document(self, doc_id: str) -> bool:
        """Remove document from system"""
        try:
            if doc_id in self.documents:
                doc_ref = self.documents[doc_id]
                
                # Remove file
                if os.path.exists(doc_ref.filepath):
                    os.remove(doc_ref.filepath)
                
                # Remove from memory
                del self.documents[doc_id]
                
                # Save updated index
                self._save_document_index()
                
                self.logger.info(f"Removed document: {doc_ref.filename}")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error removing document: {e}")
            return False