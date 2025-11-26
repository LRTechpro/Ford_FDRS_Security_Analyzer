"""
Professional Reporting Engine
Enterprise-grade report generation with multiple formats and templates
"""

import os
import json
import html
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import logging
from dataclasses import dataclass
import base64


@dataclass
class ReportMetadata:
    """Report metadata structure"""
    title: str
    generated_by: str
    generation_time: datetime
    file_analyzed: str
    analysis_mode: str
    total_entries: int
    error_count: int
    warning_count: int
    success_count: int
    version: str = "2.1.0"


class ProfessionalReportGenerator:
    """Enterprise-grade report generation engine"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.template_dir = Path("templates")
        self.output_dir = Path("reports")
        
        # Ensure directories exist
        self.template_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialize templates
        self._initialize_templates()
    
    def _initialize_templates(self):
        """Initialize report templates"""
        self.html_template = self._get_html_template()
        self.css_styles = self._get_css_styles()
        self.executive_template = self._get_executive_template()
        self.technical_template = self._get_technical_template()
    
    def generate_comprehensive_report(self, 
                                    analysis_results: List[Dict],
                                    metadata: ReportMetadata,
                                    report_type: str = "comprehensive",
                                    output_format: str = "html") -> str:
        """Generate comprehensive professional report"""
        
        try:
            self.logger.info(f"Generating {report_type} report in {output_format} format")
            
            # Prepare report data
            report_data = self._prepare_report_data(analysis_results, metadata)
            
            # Generate based on type and format
            if output_format.lower() == "html":
                return self._generate_html_report(report_data, report_type)
            elif output_format.lower() == "json":
                return self._generate_json_report(report_data, report_type)
            elif output_format.lower() == "xml":
                return self._generate_xml_report(report_data, report_type)
            elif output_format.lower() == "csv":
                return self._generate_csv_report(report_data, report_type)
            else:
                raise ValueError(f"Unsupported output format: {output_format}")
                
        except Exception as e:
            self.logger.error(f"Report generation failed: {e}")
            raise
    
    def _prepare_report_data(self, results: List[Dict], metadata: ReportMetadata) -> Dict[str, Any]:
        """Prepare and organize data for reporting"""
        
        # Categorize results
        errors = [r for r in results if self._is_error_entry(r)]
        warnings = [r for r in results if self._is_warning_entry(r)]
        successes = [r for r in results if self._is_success_entry(r)]
        communications = [r for r in results if self._is_communication_entry(r)]
        
        # ECU analysis
        ecu_stats = self._analyze_ecu_distribution(results)
        
        # Timeline analysis
        timeline_data = self._create_timeline_analysis(results)
        
        # Error patterns
        error_patterns = self._analyze_error_patterns(errors)
        
        # Performance metrics
        performance_metrics = self._calculate_performance_metrics(results)
        
        return {
            "metadata": metadata,
            "summary": {
                "total_entries": len(results),
                "error_count": len(errors),
                "warning_count": len(warnings),
                "success_count": len(successes),
                "communication_count": len(communications),
                "unique_ecus": len(ecu_stats),
                "analysis_duration": "N/A",  # Would be calculated in production
                "file_size": "N/A"  # Would be calculated in production
            },
            "categorized_results": {
                "errors": errors[:100],  # Limit for performance
                "warnings": warnings[:100],
                "successes": successes[:50],
                "communications": communications[:50]
            },
            "ecu_analysis": ecu_stats,
            "timeline": timeline_data,
            "error_patterns": error_patterns,
            "performance_metrics": performance_metrics,
            "recommendations": self._generate_recommendations(results, errors)
        }
    
    def _generate_html_report(self, report_data: Dict[str, Any], report_type: str) -> str:
        """Generate professional HTML report"""
        
        metadata = report_data["metadata"]
        summary = report_data["summary"]
        
        # Choose template based on report type
        if report_type == "executive":
            content = self._generate_executive_content(report_data)
        elif report_type == "technical":
            content = self._generate_technical_content(report_data)
        else:  # comprehensive
            content = self._generate_comprehensive_content(report_data)
        
        # Generate HTML
        html_content = self.html_template.format(
            title=metadata.title,
            css_styles=self.css_styles,
            generation_time=metadata.generation_time.strftime("%Y-%m-%d %H:%M:%S"),
            file_analyzed=metadata.file_analyzed,
            analysis_mode=metadata.analysis_mode,
            total_entries=summary["total_entries"],
            error_count=summary["error_count"],
            warning_count=summary["warning_count"],
            success_count=summary["success_count"],
            content=content,
            version=metadata.version
        )
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"diagnostic_report_{report_type}_{timestamp}.html"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        self.logger.info(f"HTML report saved: {filepath}")
        return str(filepath)
    
    def _generate_comprehensive_content(self, report_data: Dict[str, Any]) -> str:
        """Generate comprehensive report content"""
        
        content_sections = []
        
        # Executive Summary
        content_sections.append(self._create_executive_summary_section(report_data))
        
        # ECU Analysis
        content_sections.append(self._create_ecu_analysis_section(report_data))
        
        # Error Analysis
        content_sections.append(self._create_error_analysis_section(report_data))
        
        # Timeline Analysis
        content_sections.append(self._create_timeline_section(report_data))
        
        # Detailed Results
        content_sections.append(self._create_detailed_results_section(report_data))
        
        # Recommendations
        content_sections.append(self._create_recommendations_section(report_data))
        
        # Appendix
        content_sections.append(self._create_appendix_section(report_data))
        
        return "\n".join(content_sections)
    
    def _create_executive_summary_section(self, report_data: Dict[str, Any]) -> str:
        """Create executive summary section"""
        summary = report_data["summary"]
        
        # Calculate health score
        total = summary["total_entries"]
        errors = summary["error_count"]
        health_score = max(0, 100 - (errors / total * 100)) if total > 0 else 100
        
        # Determine status
        if health_score >= 95:
            status = "EXCELLENT"
            status_class = "status-excellent"
        elif health_score >= 85:
            status = "GOOD"
            status_class = "status-good"
        elif health_score >= 70:
            status = "FAIR"
            status_class = "status-fair"
        else:
            status = "NEEDS ATTENTION"
            status_class = "status-poor"
        
        return f"""
        <div class="section">
            <h2>📊 Executive Summary</h2>
            <div class="summary-grid">
                <div class="metric-card">
                    <h3>System Health Score</h3>
                    <div class="health-score {status_class}">
                        <span class="score">{health_score:.1f}%</span>
                        <span class="status">{status}</span>
                    </div>
                </div>
                <div class="metric-card">
                    <h3>Total Communications</h3>
                    <span class="metric-value">{summary['total_entries']:,}</span>
                </div>
                <div class="metric-card error-metric">
                    <h3>Errors Detected</h3>
                    <span class="metric-value">{summary['error_count']:,}</span>
                </div>
                <div class="metric-card">
                    <h3>ECU Modules</h3>
                    <span class="metric-value">{summary.get('unique_ecus', 'N/A')}</span>
                </div>
            </div>
            
            <div class="key-findings">
                <h3>🔍 Key Findings</h3>
                <ul>
                    <li>Analyzed {summary['total_entries']:,} diagnostic communications</li>
                    <li>Identified {summary['error_count']} error conditions requiring attention</li>
                    <li>Found {summary['warning_count']} warnings for review</li>
                    <li>Recorded {summary['success_count']} successful operations</li>
                </ul>
            </div>
        </div>
        """
    
    def _create_ecu_analysis_section(self, report_data: Dict[str, Any]) -> str:
        """Create ECU analysis section"""
        ecu_stats = report_data.get("ecu_analysis", {})
        
        if not ecu_stats:
            return "<div class='section'><h2>🔧 ECU Analysis</h2><p>No ECU data available for analysis.</p></div>"
        
        # Create ECU table
        ecu_rows = []
        for ecu_id, stats in ecu_stats.items():
            error_rate = (stats.get('errors', 0) / max(stats.get('total', 1), 1)) * 100
            status_icon = "🔴" if error_rate > 10 else "🟡" if error_rate > 5 else "🟢"
            
            ecu_rows.append(f"""
                <tr>
                    <td>{status_icon}</td>
                    <td><code>{ecu_id}</code></td>
                    <td>{stats.get('name', 'Unknown')}</td>
                    <td>{stats.get('total', 0):,}</td>
                    <td>{stats.get('errors', 0)}</td>
                    <td>{error_rate:.1f}%</td>
                    <td>{stats.get('last_activity', 'N/A')}</td>
                </tr>
            """)
        
        ecu_table = f"""
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Status</th>
                        <th>ECU ID</th>
                        <th>Module Name</th>
                        <th>Communications</th>
                        <th>Errors</th>
                        <th>Error Rate</th>
                        <th>Last Activity</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(ecu_rows)}
                </tbody>
            </table>
        """
        
        return f"""
        <div class="section">
            <h2>🔧 ECU Analysis</h2>
            <p>Detailed analysis of Electronic Control Unit (ECU) communications and performance.</p>
            {ecu_table}
        </div>
        """
    
    def _create_error_analysis_section(self, report_data: Dict[str, Any]) -> str:
        """Create error analysis section"""
        errors = report_data["categorized_results"]["errors"]
        error_patterns = report_data.get("error_patterns", {})
        
        if not errors:
            return "<div class='section'><h2>⚠️ Error Analysis</h2><p>No errors detected in the analysis.</p></div>"
        
        # Create error summary
        error_summary = f"""
            <div class="alert alert-error">
                <h3>⚠️ {len(errors)} Error(s) Detected</h3>
                <p>The following errors require immediate attention:</p>
            </div>
        """
        
        # Error details table
        error_rows = []
        for i, error in enumerate(errors[:20]):  # Show top 20 errors
            timestamp = error.get('timestamp', 'N/A')
            ecu = error.get('ecu', error.get('source', 'Unknown'))
            description = html.escape(str(error.get('description', error.get('message', 'No description'))))
            severity = error.get('severity', 'Medium')
            
            severity_class = {
                'Critical': 'severity-critical',
                'High': 'severity-high',
                'Medium': 'severity-medium',
                'Low': 'severity-low'
            }.get(severity, 'severity-medium')
            
            error_rows.append(f"""
                <tr>
                    <td>{i+1}</td>
                    <td>{timestamp}</td>
                    <td><span class="severity-badge {severity_class}">{severity}</span></td>
                    <td><code>{ecu}</code></td>
                    <td>{description}</td>
                </tr>
            """)
        
        error_table = f"""
            <table class="data-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Timestamp</th>
                        <th>Severity</th>
                        <th>ECU</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(error_rows)}
                </tbody>
            </table>
        """
        
        return f"""
        <div class="section">
            <h2>⚠️ Error Analysis</h2>
            {error_summary}
            {error_table}
            {f"<p><em>Showing first 20 of {len(errors)} total errors.</em></p>" if len(errors) > 20 else ""}
        </div>
        """
    
    def _create_recommendations_section(self, report_data: Dict[str, Any]) -> str:
        """Create recommendations section"""
        recommendations = report_data.get("recommendations", [])
        
        if not recommendations:
            return "<div class='section'><h2>💡 Recommendations</h2><p>No specific recommendations at this time.</p></div>"
        
        rec_items = []
        for i, rec in enumerate(recommendations):
            priority_class = {
                'High': 'priority-high',
                'Medium': 'priority-medium',
                'Low': 'priority-low'
            }.get(rec.get('priority', 'Medium'), 'priority-medium')
            
            rec_items.append(f"""
                <div class="recommendation-item {priority_class}">
                    <h4>{rec.get('title', f'Recommendation {i+1}')}</h4>
                    <p>{rec.get('description', '')}</p>
                    <div class="rec-actions">
                        <strong>Recommended Actions:</strong>
                        <ul>
                            {''.join(f'<li>{action}</li>' for action in rec.get('actions', []))}
                        </ul>
                    </div>
                </div>
            """)
        
        return f"""
        <div class="section">
            <h2>💡 Recommendations</h2>
            <p>Based on the analysis, here are our recommendations for system optimization:</p>
            {''.join(rec_items)}
        </div>
        """
    
    # Additional helper methods (stubs for brevity)
    def _create_timeline_section(self, report_data: Dict[str, Any]) -> str:
        return "<div class='section'><h2>📈 Timeline Analysis</h2><p>Timeline visualization would be implemented here.</p></div>"
    
    def _create_detailed_results_section(self, report_data: Dict[str, Any]) -> str:
        return "<div class='section'><h2>📋 Detailed Results</h2><p>Detailed results table would be implemented here.</p></div>"
    
    def _create_appendix_section(self, report_data: Dict[str, Any]) -> str:
        return "<div class='section'><h2>📎 Appendix</h2><p>Additional technical details and raw data would be included here.</p></div>"
    
    # Analysis helper methods
    def _is_error_entry(self, entry: Dict) -> bool:
        text = str(entry).lower()
        return any(keyword in text for keyword in ['error', 'failure', 'fail', 'nrc', 'fault'])
    
    def _is_warning_entry(self, entry: Dict) -> bool:
        text = str(entry).lower()
        return 'warning' in text or 'warn' in text
    
    def _is_success_entry(self, entry: Dict) -> bool:
        text = str(entry).lower()
        return any(keyword in text for keyword in ['success', 'pass', 'ok', 'complete'])
    
    def _is_communication_entry(self, entry: Dict) -> bool:
        return True  # All entries are communications in this context
    
    def _analyze_ecu_distribution(self, results: List[Dict]) -> Dict[str, Any]:
        """Analyze ECU distribution in results"""
        # This would implement actual ECU analysis
        return {}
    
    def _create_timeline_analysis(self, results: List[Dict]) -> Dict[str, Any]:
        """Create timeline analysis"""
        # This would implement actual timeline analysis
        return {}
    
    def _analyze_error_patterns(self, errors: List[Dict]) -> Dict[str, Any]:
        """Analyze error patterns"""
        # This would implement actual error pattern analysis
        return {}
    
    def _calculate_performance_metrics(self, results: List[Dict]) -> Dict[str, Any]:
        """Calculate performance metrics"""
        # This would implement actual performance calculations
        return {}
    
    def _generate_recommendations(self, results: List[Dict], errors: List[Dict]) -> List[Dict[str, Any]]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if len(errors) > 10:
            recommendations.append({
                "title": "High Error Rate Detected",
                "description": f"The system shows {len(errors)} errors, which exceeds normal thresholds.",
                "priority": "High",
                "actions": [
                    "Review error patterns for common causes",
                    "Check ECU communication interfaces",
                    "Verify system configuration and parameters",
                    "Consider diagnostic calibration updates"
                ]
            })
        
        # Add more recommendation logic here
        
        return recommendations
    
    # Template methods
    def _get_html_template(self) -> str:
        """Get HTML report template"""
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{css_styles}</style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚗 Professional Automotive Diagnostic Report</h1>
            <div class="report-meta">
                <p><strong>Generated:</strong> {generation_time}</p>
                <p><strong>File Analyzed:</strong> {file_analyzed}</p>
                <p><strong>Analysis Mode:</strong> {analysis_mode}</p>
                <p><strong>Version:</strong> {version}</p>
            </div>
        </header>
        
        <main>
            {content}
        </main>
        
        <footer>
            <p>Report generated by Professional Automotive Diagnostic Analyzer v{version}</p>
            <p>© 2025 - For professional diagnostic use only</p>
        </footer>
    </div>
</body>
</html>"""
    
    def _get_css_styles(self) -> str:
        """Get professional CSS styles"""
        return """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        
        header {
            border-bottom: 3px solid #1f4e79;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        
        header h1 {
            color: #1f4e79;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .report-meta {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #3182ce;
        }
        
        .section {
            margin-bottom: 40px;
            padding: 20px;
            border-radius: 8px;
            background: white;
            border: 1px solid #e2e8f0;
        }
        
        .section h2 {
            color: #2c5282;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e2e8f0;
        }
        
        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .metric-card.error-metric {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        }
        
        .metric-card h3 {
            font-size: 0.9em;
            margin-bottom: 10px;
            opacity: 0.9;
        }
        
        .metric-value {
            font-size: 2.5em;
            font-weight: bold;
        }
        
        .health-score {
            text-align: center;
        }
        
        .health-score .score {
            display: block;
            font-size: 3em;
            font-weight: bold;
        }
        
        .health-score .status {
            display: block;
            font-size: 0.9em;
            margin-top: 5px;
        }
        
        .status-excellent { color: #38a169; }
        .status-good { color: #3182ce; }
        .status-fair { color: #d69e2e; }
        .status-poor { color: #e53e3e; }
        
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9em;
        }
        
        .data-table th,
        .data-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .data-table th {
            background: #2c5282;
            color: white;
            font-weight: bold;
        }
        
        .data-table tr:hover {
            background: #f8f9fa;
        }
        
        .severity-badge {
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: bold;
            text-transform: uppercase;
        }
        
        .severity-critical { background: #fee; color: #c53030; }
        .severity-high { background: #fff5f5; color: #e53e3e; }
        .severity-medium { background: #fffbeb; color: #d69e2e; }
        .severity-low { background: #f0fff4; color: #38a169; }
        
        .alert {
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        
        .alert-error {
            background: #fed7d7;
            border-left: 4px solid #e53e3e;
            color: #742a2a;
        }
        
        .recommendation-item {
            background: #f7fafc;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #3182ce;
        }
        
        .recommendation-item.priority-high {
            border-left-color: #e53e3e;
            background: #fed7d7;
        }
        
        .recommendation-item.priority-medium {
            border-left-color: #d69e2e;
            background: #fffbeb;
        }
        
        .recommendation-item.priority-low {
            border-left-color: #38a169;
            background: #f0fff4;
        }
        
        .key-findings ul {
            list-style: none;
            padding-left: 0;
        }
        
        .key-findings li {
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
        }
        
        .key-findings li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #38a169;
            font-weight: bold;
        }
        
        footer {
            border-top: 2px solid #e2e8f0;
            padding-top: 20px;
            margin-top: 40px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }
        
        code {
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Consolas', monospace;
            font-size: 0.9em;
        }
        
        @media print {
            .container { box-shadow: none; }
            .section { page-break-inside: avoid; }
        }
        """
    
    def _get_executive_template(self) -> str:
        """Get executive summary template"""
        return "Executive template placeholder"
    
    def _get_technical_template(self) -> str:
        """Get technical report template"""
        return "Technical template placeholder"
    
    def _generate_json_report(self, report_data: Dict[str, Any], report_type: str) -> str:
        """Generate JSON report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"diagnostic_report_{report_type}_{timestamp}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        self.logger.info(f"JSON report saved: {filepath}")
        return str(filepath)
    
    def _generate_xml_report(self, report_data: Dict[str, Any], report_type: str) -> str:
        """Generate XML report"""
        # XML generation would be implemented here
        return "XML report placeholder"
    
    def _generate_csv_report(self, report_data: Dict[str, Any], report_type: str) -> str:
        """Generate CSV report"""
        # CSV generation would be implemented here
        return "CSV report placeholder"