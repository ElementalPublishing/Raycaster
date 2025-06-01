"""
InputHandler: processes user input and updates player actions.
"""
from .player import Player

class InputHandler:
    def __init__(self, player: Player):
        self.player = player

    def process_input(self):
        """
        Process keyboard and mouse input.
        """
        # TODO: Hook into input library (pygame, etc.)
        pass