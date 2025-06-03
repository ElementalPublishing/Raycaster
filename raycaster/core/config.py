"""
EngineConfig: holds all engine configuration parameters.
"""

from typing import Any, Tuple


class EngineConfig:
    def __init__(
        self,
        resolution: Tuple[int, int] = (640, 480),
        fov: float = 60.0,
        map_path: str = "assets/maps/basic_map.json",
        **kwargs: Any,
    ):
        if (
            not isinstance(resolution, tuple)
            or len(resolution) != 2
            or not all(isinstance(x, int) and x > 0 for x in resolution)
        ):
            raise ValueError("resolution must be a tuple of two positive integers")
        if not isinstance(fov, (int, float)) or fov <= 0:
            raise ValueError("fov must be a positive number")
        if not isinstance(map_path, str) or not map_path:
            raise ValueError("map_path must be a non-empty string")

        self.resolution = resolution
        self.fov = fov
        self.map_path = map_path
        # Add more config options as needed
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return (
            f"EngineConfig(resolution={self.resolution}, fov={self.fov}, "
            f"map_path='{self.map_path}', ...)"
        )
