"""
Main game engine loop and application entry point.
Supports pluggable backends for rendering and input.
"""

from .map import GameMap
from .player import Player
from .config import EngineConfig
from .interfaces import BaseRenderer, BaseInputHandler
from .renderer import Renderer  # <-- Import your Renderer here
from typing import Callable, List
# Only import additional modules here if you use them in this file


class RaycastingEngine:
    def __init__(self, config: EngineConfig, backend: str = "pygame"):
        self.config = config
        self.map = GameMap(config.map_path)
        self.player = Player(self.map.start_position)

        # Dynamically select backend
        if backend == "pygame":
            from .pygame_backend import PygameRenderer, PygameInputHandler
            self.renderer: BaseRenderer = PygameRenderer(self.map, self.player, config)
            self.input_handler: BaseInputHandler = PygameInputHandler(self.player)
        elif backend == "renderer":
            self.renderer: BaseRenderer = Renderer(self.map, self.player, config)
            self.input_handler: BaseInputHandler = None  # Set this to your input handler if needed
        # Future: add elif blocks for other backends (pyglet, moderngl, etc.)
        else:
            raise ValueError(f"Unknown backend: {backend}")

        self.running = True
        self.framerate = getattr(config, "framerate", 60)

        # Hooks for plugins and custom logic
        self.pre_update_hooks: List[Callable[[], None]] = []
        self.post_update_hooks: List[Callable[[], None]] = []
        self.pre_render_hooks: List[Callable[[], None]] = []
        self.post_render_hooks: List[Callable[[], None]] = []
        self.event_handlers: List[Callable] = []

    def register_pre_update(self, func: Callable[[], None]):
        self.pre_update_hooks.append(func)

    def register_post_update(self, func: Callable[[], None]):
        self.post_update_hooks.append(func)

    def register_pre_render(self, func: Callable[[], None]):
        self.pre_render_hooks.append(func)

    def register_post_render(self, func: Callable[[], None]):
        self.post_render_hooks.append(func)

    def register_event_handler(self, func: Callable):
        self.event_handlers.append(func)

    def run(self):
        """
        Main engine loop: handles input, updates game state, renders frames.
        Supports plugin hooks and custom event handlers.
        """
        try:
            while self.running:
                # Event handling (backend-specific)
                if hasattr(self.input_handler, "process_events"):
                    for event in self.input_handler.process_events():
                        if getattr(event, "type", None) == "QUIT":
                            self.running = False
                        for handler in self.event_handlers:
                            handler(event)

                for hook in self.pre_update_hooks:
                    hook()

                self.input_handler.process_input()
                self.player.update()

                for hook in self.post_update_hooks:
                    hook()

                for hook in self.pre_render_hooks:
                    hook()

                self.renderer.render_frame()

                for hook in self.post_render_hooks:
                    hook()

                self.renderer.flip()
                self.renderer.tick(self.framerate)

        except Exception as e:
            print(f"Engine encountered an error: {e}")
        finally:
            # Backend-specific cleanup if needed
            if hasattr(self.renderer, "cleanup"):
                self.renderer.cleanup()
