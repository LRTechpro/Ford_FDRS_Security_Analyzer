"""
Minimal test to check NRC 7F method availability
"""

def test_method_exists():
    try:
        from gui_app_enhanced import EnhancedLogParserGUI
        import tkinter as tk
        
        # Create a minimal instance
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        app = EnhancedLogParserGUI(root)
        
        # Check if the method exists
        if hasattr(app, '_show_nrc7f_details'):
            print("✅ Method _show_nrc7f_details exists")
        else:
            print("❌ Method _show_nrc7f_details NOT found")
            print("Available methods with 'nrc' in name:")
            methods = [m for m in dir(app) if 'nrc' in m.lower()]
            for method in methods:
                print(f"  - {method}")
        
        if hasattr(app, '_check_nrc7f_issues'):
            print("✅ Method _check_nrc7f_issues exists")
        else:
            print("❌ Method _check_nrc7f_issues NOT found")
        
        root.destroy()
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_method_exists()