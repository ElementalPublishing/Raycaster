class RendererPlugin:
    """
    Base class for renderer plugins.
    Plugins can override pre_render and post_render to inject custom logic.
    """
    def pre_render(self, renderer):
        """Called before the main render_frame logic."""
        pass

    def post_render(self, renderer):
        """Called after the main render_frame logic."""
        pass