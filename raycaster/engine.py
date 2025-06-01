"""
Main game engine loop and application entry point.
"""
from .renderer import Renderer
from .map import GameMap
from .player import Player
from .input import InputHandler
from .config import EngineConfig

class RaycastingEngine:
    def __init__(self, config: EngineConfig):
        self.config = config
        self.map = GameMap(config.map_path)
        self.player = Player(self.map.start_position)
        self.renderer = Renderer(self.map, self.player, config)
        self.input_handler = InputHandler(self.player)

    def run(self):
        """
        Main engine loop: handles input, updates game state, renders frames.
        """
        running = True
        while running:
            self.input_handler.process_input()
            self.player.update()
            self.renderer.render_frame()
            # TODO: Add frame timing, event handling, exit condition.