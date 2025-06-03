"""
Player: handles player state and movement.
"""

from typing import Tuple


class Player:
    """
    Represents the player in the game world.
    Handles position, angle, and movement logic.
    """

    def __init__(
        self,
        start_pos: Tuple[float, float],
        move_speed: float = 0.05,
        turn_speed: float = 0.03,
    ):
        self.x, self.y = start_pos
        self.angle = 0.0
        self.move_speed = move_speed
        self.turn_speed = turn_speed
        # Future: self.health = 100, self.inventory = []

    def update(self):
        """
        Update player state.
        Extend this method to implement movement, collision detection, etc.
        """
        pass  # TODO: Implement movement logic
