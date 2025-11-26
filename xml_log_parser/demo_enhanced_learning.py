"""
Demo script for Enhanced Learning Mode
Shows the educational features with real log data
"""

from xml_log_parser import XMLLogParser
from enhanced_simple_mode import EnhancedSimpleReportGenerator

def demo_enhanced_learning_mode():
    """Demonstrate the enhanced learning mode with real log data"""
    print("🎓 Enhanced Learning Mode Demo")
    print("=" * 60)
    
    # Parse the sample log
    parser = XMLLogParser()
    results = parser.parse_file('sample_log.xml')
    
    print(f"📊 Parsed sample_log.xml: Found {len(results)} items")
    print()
    
    # Generate educational report
    generator = EnhancedSimpleReportGenerator()
    educational_report = generator.generate_educational_report(results, 'xml')
    
    # Save the report to a file for easy reading
    with open('demo_educational_report.txt', 'w', encoding='utf-8') as f:
        f.write(educational_report)
    
    print("📝 Generated educational report and saved to 'demo_educational_report.txt'")
    print()
    print("🔍 Quick preview of the learning content:")
    print("-" * 60)
    
    # Show first few sections as preview
    lines = educational_report.split('\n')
    preview_lines = []
    section_count = 0
    
    for line in lines:
        preview_lines.append(line)
        
        # Stop after showing a few sections
        if line.startswith('='*80) and section_count > 0:
            section_count += 1
            if section_count >= 3:  # Show 3 sections
                preview_lines.append("...")
                preview_lines.append("(Full report saved to demo_educational_report.txt)")
                break
        elif line.startswith('='*80):
            section_count += 1
    
    # Print preview
    for line in preview_lines:
        print(line)
    
    print()
    print("✨ Key Features Demonstrated:")
    print("• 📚 Educational hex/ASCII tutorials")
    print("• 🔍 Real examples from your log file")
    print("• 🚗 Automotive diagnostics explanations")
    print("• 💡 Step-by-step learning approach")
    print()
    print("🎯 To see the full educational experience:")
    print("1. Run the GUI: python gui_app.py")
    print("2. Enable 'Learning Mode (Teaches Hex/ASCII)'")
    print("3. Parse sample_log.xml or your own log file")

if __name__ == "__main__":
    demo_enhanced_learning_mode()