"""
GameMap: handles map data, loading, and collision logic.
"""

from typing import Tuple, List
import json


class GameMap:
    def __init__(self, map_path: str):
        with open(map_path, "r") as f:
            data = json.load(f)
        self.map_data = data["grid"]
        self.start_position = tuple(data.get("start_position", (1.5, 1.5)))

    def is_wall(self, x: float, y: float) -> bool:
        xi, yi = int(x), int(y)
        return self.map_data[yi][xi] > 0
