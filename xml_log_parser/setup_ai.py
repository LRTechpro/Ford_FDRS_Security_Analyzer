"""
Setup script for AI-enhanced Professional Diagnostic Analyzer
Installs required packages for ChatGPT integration
"""

import subprocess
import sys
import os

def install_package(package):
    """Install package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    print("🚀 Setting up AI-Enhanced Professional Diagnostic Analyzer")
    print("=" * 60)
    
    # Required packages for AI integration
    packages = [
        "openai>=1.0.0",
        "requests>=2.28.0", 
        "python-dateutil>=2.8.2"
    ]
    
    print("Installing AI integration packages...")
    success_count = 0
    
    for package in packages:
        print(f"\n📦 Installing {package}...")
        if install_package(package):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"Installation Summary: {success_count}/{len(packages)} packages installed")
    
    if success_count == len(packages):
        print("🎉 All packages installed successfully!")
        print("\nNext steps:")
        print("1. Get an OpenAI API key from https://platform.openai.com")
        print("2. Launch the Professional Diagnostic Analyzer")
        print("3. Go to the '🤖 AI Assistant' tab")
        print("4. Enter your API key and click 'Set Key'")
        print("5. Click 'Test Connection' to verify setup")
        print("\n🚀 Ready to use AI-powered diagnostic analysis!")
    else:
        print("⚠️  Some packages failed to install.")
        print("Please check the error messages above and try again.")
        print("You may need to run this script as administrator.")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()