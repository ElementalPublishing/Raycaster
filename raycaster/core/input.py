"""
InputHandler: processes user input and updates player actions.
"""

from typing import Optional, Sequence

import pygame

from .player import Player


class InputHandler:
    """
    Handles keyboard (and optionally mouse) input for the player.
    """

    def __init__(self, player: Player):
        self.player = player

    def process_input(self, keys: Optional[Sequence[bool]] = None):
        """
        Process keyboard
        input using pygame
        or a provided key state (for testing).
        """
        if keys is None:
            keys = pygame.key.get_pressed()

        # Example movement controls (customize as needed)
        if hasattr(self.player, "move_forward") and keys[pygame.K_w]:
            self.player.move_forward()
        if hasattr(self.player, "move_backward") and keys[pygame.K_s]:
            self.player.move_backward()
        if hasattr(self.player, "strafe_left") and keys[pygame.K_a]:
            self.player.strafe_left()
        if hasattr(self.player, "strafe_right") and keys[pygame.K_d]:
            self.player.strafe_right()
        if hasattr(self.player, "turn_left") and keys[pygame.K_LEFT]:
            self.player.turn_left()
        if hasattr(self.player, "turn_right") and keys[pygame.K_RIGHT]:
            self.player.turn_right()
