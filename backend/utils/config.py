# config.py (alternative approach)
import yaml
from typing import Dict, Any, Optional
from pathlib import Path

class _Config:
    def __init__(self, config_path: str = "config.yaml"):
        self._config: Dict[str, Any] = {}
        self._load_config(config_path)
    
    def _load_config(self, config_path: str) -> None:
        if Path(config_path).exists():
            with open(config_path) as f:
                self._config = yaml.safe_load(f) or {}
        else:
            raise FileNotFoundError(f"Config file not found: {config_path}")
    
    def get(self, key: Optional[str] = None, default: Any = None) -> Any:
        if key is None:
            return self._config
        
        return self._config.get(key, default)
    
    def get_nested(self, *keys: str, default: Any = None) -> Any:
        value = self._config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
            
        return value
    
    def reload(self, config_path: str = "config.yaml") -> None:
        self._load_config(config_path)

# Create the singleton instance at module level
config = _Config("config.yaml")

# Export it for easy importing
__all__ = ['config']