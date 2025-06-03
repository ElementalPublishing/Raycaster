"""
GameMap: handles map data, loading, and collision logic.
"""

import json
import os
from typing import Optional  # Removed unused Any, List, Tuple


class GameMap:
    def __init__(
        self,
        map_path: Optional[str] = None,
        data: Optional[dict] = None,
    ):
        """
        Initialize GameMap from a file path or directly from data (for testing).
        """
        if data is not None:
            self._load_from_data(data)
        elif map_path is not None:
            self._load_from_file(
                map_path
            )
        else:
            raise ValueError("Must provide either map_path or data.")

    def _load_from_file(self, map_path: str):
        if not os.path.exists(map_path):
            raise FileNotFoundError(f"Map file not found: {map_path}")
        with open(map_path, "r") as f:
            data = json.load(f)
        self._load_from_data(data)

    def _load_from_data(self, data: dict):
        if "grid" not in data:
            raise ValueError("Map data missing 'grid' key.")
        self.map_data = data["grid"]
        self.start_position = tuple(data.get("start_position", (1.5, 1.5)))

    def is_wall(self, x: float, y: float) -> bool:
        """
        Returns True if the given (x, y) position is a wall.
        Handles out-of-bounds gracefully (returns True for out-of-bounds).
        """
        xi, yi = int(x), int(y)
        if (
            yi < 0
            or yi >= len(self.map_data)
            or xi < 0
            or xi >= len(self.map_data[0])
        ):
            return True  # Treat out-of-bounds as wall
        return self.map_data[yi][xi] > 0
