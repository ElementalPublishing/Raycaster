"""
Raycasting renderer: handles drawing the scene from the player's perspective.
"""

import os
import pygame
from concurrent.futures import ProcessPoolExecutor
from .map import GameMap
from .player import Player
from .config import EngineConfig
from .plugin import RendererPlugin


def raycast_column(args):
    """
    Standalone function for raycasting a single vertical column.
    Must be at module level for ProcessPoolExecutor.
    Replace this logic with your actual raycasting.
    """
    x, width = args
    # Example: return a color based on x (replace with real raycasting)
    color = (x % 255, 100, 255 - (x % 255))
    return x, color


class Renderer:
    def __init__(self, game_map: GameMap, player: Player, config: EngineConfig):
        self.game_map = game_map
        self.player = player
        self.config = config
        self.plugins = []
        pygame.init()
        self.screen = pygame.display.set_mode(self.config.resolution)
        pygame.display.set_caption("Raycaster Engine")
        self.clock = pygame.time.Clock()
        self.num_workers = getattr(config, "num_workers", os.cpu_count() or 1)

    def register_plugin(self, plugin: RendererPlugin):
        """Register a renderer plugin."""
        self.plugins.append(plugin)

    def render_frame(self):
        """
        Perform raycasting and draw a single frame using multi-core support.
        Allows plugins to override the entire rendering process.
        """
        # Check if any plugin wants to override rendering
        for plugin in self.plugins:
            if hasattr(plugin, "render_override") and callable(plugin.render_override):
                if plugin.render_override(self):
                    # If plugin returns True, skip default rendering
                    return

        # Call pre-render hooks
        for plugin in self.plugins:
            plugin.pre_render(self)

        width, height = self.config.resolution
        columns = [(x, width) for x in range(width)]

        # Parallel raycasting using ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            results = list(executor.map(raycast_column, columns))

        # Draw the results
        for x, color in results:
            pygame.draw.line(self.screen, color, (x, 0), (x, height - 1))

        # Call post-render hooks
        for plugin in self.plugins:
            plugin.post_render(self)
