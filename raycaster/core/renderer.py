"""
Raycasting renderer: handles drawing the scene from the player's perspective.
"""

import os
from concurrent.futures import ProcessPoolExecutor

import pygame

from .config import EngineConfig
from .map import GameMap
from .player import Player
from .plugin import RendererPlugin
from .baserenderer import BaseRenderer


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


class Renderer(BaseRenderer):
    """Default renderer implementation (inherits from BaseRenderer)."""

    def __init__(
        self,
        game_map: GameMap,
        player: Player,
        config: EngineConfig,
        headless: bool = False,
    ):
        super().__init__(game_map, player, config, headless)

    def render_frame(self):
        """
        Perform raycasting and draw a single frame using multi-core support.
        Allows plugins to override the entire rendering process.
        """
        # Check if any plugin wants to override rendering
        for plugin in self.plugins:
            try:
                if hasattr(plugin, "render_override") and callable(
                    plugin.render_override
                ):
                    if plugin.render_override(self):
                        # If plugin returns True, skip default rendering
                        return
            except Exception as e:
                print(f"[Renderer] Plugin render_override error: {e}")

        # Call pre-render hooks
        for plugin in self.plugins:
            try:
                if hasattr(plugin, "pre_render"):
                    plugin.pre_render(self)
            except Exception as e:
                print(f"[Renderer] Plugin pre_render error: {e}")

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
            try:
                if hasattr(plugin, "post_render"):
                    plugin.post_render(self)
            except Exception as e:
                print(f"[Renderer] Plugin post_render error: {e}")

