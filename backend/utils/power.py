import importlib.util
from typing import Dict, Any, Optional
from utils.config import config

class PowerManager:
    def __init__(self):
        if config.get('power'):
            self._load_custom_methods()
            
    def _load_custom_methods(self) -> None:
        script_path = config.get_nested('power', 'custom_script')
        
        if script_path:
            try:
                spec = importlib.util.spec_from_file_location("custom_power", script_path)
                
                if spec and spec.loader:
                    custom_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(custom_module)
                    
                    # Override methods if they exist
                    if hasattr(custom_module, 'power_on'):
                        self.power_on = custom_module.power_on
                    
                    if hasattr(custom_module, 'power_off'):
                        self.power_off = custom_module.power_off
                        
                    if hasattr(custom_module, 'power_status'):
                        self.power_status = custom_module.power_status
                        
                    print(f"Loaded custom power script: {script_path}")
            
            except Exception as e:
                print(f"Failed to load custom power script: {e}")
                
    # Default implementations
    async def power_on(self) -> Dict[str, Any]:
        return {"status": "on", "method": "default", "message": "No custom power_on configured"}
    
    async def power_off(self) -> Dict[str, Any]:
        return {"status": "off", "method": "default", "message": "No custom power_off configured"}
    
    async def power_status(self) -> Dict[str, Any]:
        return {"status": "unknown", "method": "default", "message": "No custom power_status configured"}

# Singleton
powerManager = PowerManager()