"""
Main game engine loop and application entry point.
Supports pluggable backends for rendering and input.
"""

from typing import Callable, List, Optional

from .config import EngineConfig
from .interfaces import BaseInputHandler, BaseRenderer
from .map import GameMap
from .player import Player
from .renderer import Renderer


class RaycastingEngine:
    """
    The main engine class. Handles the game loop, plugin hooks, and backend selection.
    """

    def __init__(self, config: EngineConfig, backend: str = "pygame"):
        self.config = config
        self.map = GameMap(config.map_path)
        self.player = Player(self.map.start_position)

        # Dynamically select backend
        if backend == "pygame":
            from .pygame_backend import PygameInputHandler, PygameRenderer

            self.renderer: BaseRenderer = PygameRenderer(
                self.map, self.player, config
            )
            self.input_handler: Optional[BaseInputHandler] = (
                PygameInputHandler(self.player)
            )
        elif backend == "renderer":
            self.renderer: BaseRenderer = Renderer(
                self.map, self.player, config
            )
            self.input_handler: Optional[BaseInputHandler] = (
                None  # Set this to your input handler if needed
            )
        # Future: add elif blocks for other backends (pyglet, moderngl, etc.)
        else:
            raise ValueError(
                f"Unknown backend: {backend}"
            )

        self.running: bool = True
        self.framerate: int = getattr(config, "framerate", 60)

        # Hooks for plugins and custom logic
        self.pre_update_hooks: List[Callable[[], None]] = []
        self.post_update_hooks: List[Callable[[], None]] = []
        self.pre_render_hooks: List[Callable[[], None]] = []
        self.post_render_hooks: List[Callable[[], None]] = []
        self.event_handlers: List[Callable] = []

    def register_pre_update(self, func: Callable[[], None]):
        """Register a function to be called before each update."""
        self.pre_update_hooks.append(func)

    def register_post_update(self, func: Callable[[], None]):
        """Register a function to be called after each update."""
        self.post_update_hooks.append(func)

    def register_pre_render(self, func: Callable[[], None]):
        """Register a function to be called before each render."""
        self.pre_render_hooks.append(func)

    def register_post_render(self, func: Callable[[], None]):
        """Register a function to be called after each render."""
        self.post_render_hooks.append(func)

    def register_event_handler(self, func: Callable):
        """Register a function to handle events."""
        self.event_handlers.append(func)

    def clear_hooks(self):
        """Clear all hooks and event handlers (useful for tests)."""
        self.pre_update_hooks.clear()
        self.post_update_hooks.clear()
        self.pre_render_hooks.clear()
        self.post_render_hooks.clear()
        self.event_handlers.clear()

    def run(self):
        """
        Main engine loop: handles input, updates game state, renders frames.
        Supports plugin hooks and custom event handlers.
        """
        try:
            while self.running:
                # Event handling (backend-specific)
                if self.input_handler and hasattr(
                    self.input_handler, "process_events"
                ):
                    for event in self.input_handler.process_events():
                        if getattr(event, "type", None) == "QUIT":
                            self.running = False
                        for handler in self.event_handlers:
                            try:
                                handler(event)
                            except Exception as e:
                                print(f"[Engine] Event handler error: {e}")

                for hook in self.pre_update_hooks:
                    try:
                        hook()
                    except Exception as e:
                        print(f"[Engine] Pre-update hook error: {e}")

                if self.input_handler and hasattr(
                    self.input_handler, "process_input"
                ):
                    try:
                        self.input_handler.process_input()
                    except Exception as e:
                        print(f"[Engine] Input handler error: {e}")

                try:
                    self.player.update()
                except Exception as e:
                    print(f"[Engine] Player update error: {e}")

                for hook in self.post_update_hooks:
                    try:
                        hook()
                    except Exception as e:
                        print(f"[Engine] Post-update hook error: {e}")

                for hook in self.pre_render_hooks:
                    try:
                        hook()
                    except Exception as e:
                        print(f"[Engine] Pre-render hook error: {e}")

                try:
                    self.renderer.render_frame()
                except Exception as e:
                    print(f"[Engine] Renderer error: {e}")

                for hook in self.post_render_hooks:
                    try:
                        hook()
                    except Exception as e:
                        print(f"[Engine] Post-render hook error: {e}")

                try:
                    self.renderer.flip()
                except Exception as e:
                    print(f"[Engine] Renderer flip error: {e}")

                try:
                    self.renderer.tick(self.framerate)
                except Exception as e:
                    print(f"[Engine] Renderer tick error: {e}")

        except Exception as e:
            print(f"Engine encountered an error: {e}")
        finally:
            # Backend-specific cleanup if needed
            if hasattr(self.renderer, "cleanup"):
                try:
                    self.renderer.cleanup()
                except Exception as e:
                    print(f"[Engine] Renderer cleanup error: {e}")
