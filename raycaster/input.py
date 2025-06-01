"""
InputHandler: processes user input and updates player actions.
"""

import pygame
from .player import Player


class InputHandler:
    def __init__(self, player: Player):
        self.player = player

    def process_input(self):
        """
        Process keyboard and mouse input using pygame.
        """
        keys = pygame.key.get_pressed()

        # Example movement controls (customize as needed)
        if keys[pygame.K_w]:
            self.player.move_forward()
        if keys[pygame.K_s]:
            self.player.move_backward()
        if keys[pygame.K_a]:
            self.player.strafe_left()
        if keys[pygame.K_d]:
            self.player.strafe_right()
        if keys[pygame.K_LEFT]:
            self.player.turn_left()
        if keys[pygame.K_RIGHT]:
            self.player.turn_right()
