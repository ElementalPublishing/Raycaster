"""
Raycasting renderer: handles drawing the scene from the player's perspective.
"""

from .map import GameMap
from .player import Player
from .config import EngineConfig
from .plugin import RendererPlugin


class Renderer:
    def __init__(self, game_map: GameMap, player: Player, config: EngineConfig):
        self.game_map = game_map
        self.player = player
        self.config = config
        self.plugins = []
        # Initialize graphics context (pygame)
        import pygame

        pygame.init()
        self.screen = pygame.display.set_mode(self.config.resolution)
        pygame.display.set_caption("Raycaster Engine")
        self.clock = pygame.time.Clock()

    def register_plugin(self, plugin: RendererPlugin):
        """Register a renderer plugin."""
        self.plugins.append(plugin)

    def render_frame(self):
        """
        Perform raycasting and draw a single frame.
        """
        # Call pre-render hooks
        for plugin in self.plugins:
            plugin.pre_render(self)

        # TODO: Actual raycasting and drawing logic here

        # Call post-render hooks
        for plugin in self.plugins:
            plugin.post_render(self)
