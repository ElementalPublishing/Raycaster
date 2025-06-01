"""
Player: handles player state and movement.
"""

from typing import Tuple


class Player:
    def __init__(self, start_pos: Tuple[float, float]):
        self.x, self.y = start_pos
        self.angle = 0.0
        self.move_speed = 0.05
        self.turn_speed = 0.03

    def update(self):
        """
        Update player state (stub for now).
        """
        # TODO: Implement movement logic, collision detection, etc.
        pass
