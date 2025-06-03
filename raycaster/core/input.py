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

        def is_pressed(idx):
            return idx < len(keys) and keys[idx]

        action_taken = False

        # Example movement controls (customize as needed)
        if hasattr(self.player, "move_forward") and is_pressed(pygame.K_w):
            self.player.move_forward()
            action_taken = True
        if hasattr(self.player, "move_backward") and is_pressed(pygame.K_s):
            self.player.move_backward()
            action_taken = True
        if hasattr(self.player, "strafe_left") and is_pressed(pygame.K_a):
            self.player.strafe_left()
            action_taken = True
        if hasattr(self.player, "strafe_right") and is_pressed(pygame.K_d):
            self.player.strafe_right()
            action_taken = True
        if hasattr(self.player, "turn_left") and is_pressed(pygame.K_q):
            self.player.turn_left()
            action_taken = True
        if hasattr(self.player, "turn_right") and is_pressed(pygame.K_e):
            self.player.turn_right()
            action_taken = True

        # If no action was taken, optionally call a no-op or log
        if not action_taken and hasattr(self.player, "no_action"):
            self.player.no_action()
