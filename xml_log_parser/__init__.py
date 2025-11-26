"""
Ford FDRS XML Log Parser Package
Professional automotive diagnostic log analysis
"""

# Import main classes for convenient access
try:
    from .xml_log_parser import XMLLogParser, NRCCodeExplainer, HexExplainer
except ImportError:
    pass

try:
    from .text_log_parser import TextLogParser
except ImportError:
    pass

try:
    from .intelligent_diagnostic_engine import IntelligentDiagnosticEngine, DocumentReference, AnalysisConclusion
except ImportError:
    pass

try:
    from .ai_diagnostic_assistant import AIDiagnosticAssistant, AIAnalysisResult
except ImportError:
    pass

try:
    from .critical_diagnostic_view import CriticalDiagnosticView, format_critical_diagnostics_report
except ImportError:
    pass

__version__ = "2.1.0"
__author__ = "Ford FDRS Analyzer Team"
