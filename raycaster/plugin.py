from typing import Any


class RendererPlugin:
    """
    Base class for renderer plugins.
    Plugins can override pre_render, post_render, and render_override to inject custom logic.
    """

    def pre_render(self, renderer: Any) -> None:
        """Called before the main render_frame logic."""
        pass

    def post_render(self, renderer: Any) -> None:
        """Called after the main render_frame logic."""
        pass

    def render_override(self, renderer: Any) -> bool:
        """
        Called before rendering. If returns True, skips default rendering.
        Override in your plugin if you want to take over rendering.
        """
        return False
