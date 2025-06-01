"""
GameMap: handles map data, loading, and collision logic.
"""
from typing import Tuple, List

class GameMap:
    def __init__(self, map_path: str):
        self.map_data = self.load_map(map_path)
        self.start_position = (1.5, 1.5)  # Example starting position

    def load_map(self, path: str) -> List[List[int]]:
        """
        Load map data from a file (e.g., JSON, text).
        """
        # TODO: Replace with actual file loading logic
        return [
            [1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,0,1],
            [1,0,1,0,1,0,0,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1],
        ]

    def is_wall(self, x: float, y: float) -> bool:
        """
        Check if position (x, y) is a wall.
        """
        xi, yi = int(x), int(y)
        return self.map_data[yi][xi] > 0