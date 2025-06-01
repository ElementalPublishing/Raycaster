"""
EngineConfig: holds all engine configuration parameters.
"""
from typing import Any

class EngineConfig:
    def __init__(self,
                 resolution: tuple = (640, 480),
                 fov: float = 60.0,
                 map_path: str = "assets/maps/basic_map.json",
                 **kwargs: Any):
        self.resolution = resolution
        self.fov = fov
        self.map_path = map_path
        # Add more config options as needed
        for k, v in kwargs.items():
            setattr(self, k, v)