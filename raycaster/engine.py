"""
Main game engine loop and application entry point.
"""
from .renderer import Renderer
from .map import GameMap
from .player import Player
from .input import InputHandler
from .config import EngineConfig
import pygame

class RaycastingEngine:
    def __init__(self, config: EngineConfig):
        self.config = config
        self.map = GameMap(config.map_path)
        self.player = Player(self.map.start_position)
        self.renderer = Renderer(self.map, self.player, config)
        self.input_handler = InputHandler(self.player)
        self.running = True

    def run(self):
        """
        Main engine loop: handles input, updates game state, renders frames.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.input_handler.process_input()
            self.player.update()
            self.renderer.render_frame()

            # Update the display and cap the framerate
            pygame.display.flip()
            self.renderer.clock.tick(60)  # 60 FPS

        pygame.quit()