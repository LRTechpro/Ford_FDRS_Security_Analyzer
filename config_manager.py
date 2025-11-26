"""
Configuration Manager for Log Parser
Handles app settings, themes, recent files, and user preferences
"""

import json
import os
from typing import Dict, List, Any
from pathlib import Path


class ConfigManager:
    """Manages application configuration and settings"""
    
    def __init__(self):
        self.config_dir = Path.home() / '.log_parser'
        self.config_file = self.config_dir / 'config.json'
        self.default_config = {
            'theme': 'light',
            'recent_files': [],
            'recent_files_max': 10,
            'window': {
                'width': 1200,
                'height': 800,
                'x': None,
                'y': None
            },
            'display': {
                'font_size': 10,
                'font_family': 'Arial',
                'show_line_numbers': True,
                'word_wrap': True
            },
            'filters': {
                'show_critical_only': False,
                'selected_ecus': [],
                'severity_levels': ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'SUCCESS'],
                'time_range': 'all'
            },
            'export': {
                'default_format': 'txt',
                'include_timestamp': True,
                'include_statistics': True
            },
            'shortcuts': {
                'open_file': 'Ctrl+O',
                'save_export': 'Ctrl+S',
                'find': 'Ctrl+F',
                'refresh': 'F5',
                'toggle_simple_mode': 'Ctrl+M',
                'clear_results': 'Ctrl+L'
            }
        }
        self.config = self._load_config()
    
    def _ensure_config_dir(self):
        """Create config directory if it doesn't exist"""
        self.config_dir.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        self._ensure_config_dir()
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    # Merge with defaults to handle new settings
                    return self._merge_configs(self.default_config, loaded_config)
            except Exception as e:
                print(f"Error loading config: {e}")
                return self.default_config.copy()
        else:
            return self.default_config.copy()
    
    def _merge_configs(self, default: Dict, loaded: Dict) -> Dict:
        """Merge loaded config with defaults for new settings"""
        merged = default.copy()
        for key, value in loaded.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._merge_configs(merged[key], value)
            else:
                merged[key] = value
        return merged
    
    def save_config(self):
        """Save current configuration to file"""
        self._ensure_config_dir()
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default=None) -> Any:
        """Get configuration value by key (supports dot notation)"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value if value is not None else default
    
    def set(self, key: str, value: Any):
        """Set configuration value by key (supports dot notation)"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save_config()
    
    def add_recent_file(self, filepath: str):
        """Add file to recent files list"""
        recent = self.config['recent_files']
        
        # Remove if already exists
        if filepath in recent:
            recent.remove(filepath)
        
        # Add to front
        recent.insert(0, filepath)
        
        # Trim to max size
        max_recent = self.config['recent_files_max']
        self.config['recent_files'] = recent[:max_recent]
        
        self.save_config()
    
    def get_recent_files(self) -> List[str]:
        """Get list of recent files (only existing files)"""
        recent = self.config['recent_files']
        # Filter out non-existent files
        existing = [f for f in recent if os.path.exists(f)]
        if len(existing) != len(recent):
            self.config['recent_files'] = existing
            self.save_config()
        return existing
    
    def clear_recent_files(self):
        """Clear recent files list"""
        self.config['recent_files'] = []
        self.save_config()
    
    def get_theme(self) -> str:
        """Get current theme"""
        return self.config['theme']
    
    def set_theme(self, theme: str):
        """Set theme (light/dark)"""
        if theme in ['light', 'dark']:
            self.config['theme'] = theme
            self.save_config()
    
    def toggle_theme(self) -> str:
        """Toggle between light and dark theme"""
        current = self.config['theme']
        new_theme = 'dark' if current == 'light' else 'light'
        self.set_theme(new_theme)
        return new_theme
    
    def save_window_geometry(self, width: int, height: int, x: int, y: int):
        """Save window size and position"""
        self.config['window'] = {
            'width': width,
            'height': height,
            'x': x,
            'y': y
        }
        self.save_config()
    
    def get_window_geometry(self) -> Dict[str, int]:
        """Get saved window geometry"""
        return self.config['window']
    
    def get_filter_config(self) -> Dict[str, Any]:
        """Get filter configuration"""
        return self.config['filters']
    
    def save_filter_config(self, filters: Dict[str, Any]):
        """Save filter configuration"""
        self.config['filters'].update(filters)
        self.save_config()
    
    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = self.default_config.copy()
        self.save_config()
