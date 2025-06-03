import pytest

from raycaster.core.renderer import Renderer


class DummyMap:
    pass


class DummyPlayer:
    pass


class DummyConfig:
    resolution = (32, 32)
    map_path = "dummy.json"
    num_workers = 1


class DummyPlugin:
    def __init__(self):
        self.pre_render_called = False
        self.post_render_called = False
        self.override_called = False

    def pre_render(self, renderer):
        self.pre_render_called = True

    def post_render(self, renderer):
        self.post_render_called = True

    def render_override(self, renderer):
        self.override_called = True
        return True  # Prevent default rendering


def test_renderer_init_headless():
    renderer = Renderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    assert renderer.screen.get_width() == 32
    assert renderer.screen.get_height() == 32
    assert isinstance(renderer.plugins, list)


def test_plugin_hooks(monkeypatch):
    renderer = Renderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    plugin = DummyPlugin()
    renderer.register_plugin(plugin)

    # Simulate render_frame calling plugin hooks
    renderer.render_frame()
    assert (
        plugin.pre_render_called or plugin.override_called
    )  # override may short-circuit pre_render
    assert plugin.override_called


def test_plugin_post_render(monkeypatch):
    renderer = Renderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    plugin = DummyPlugin()
    # Only implement post_render for this test
    plugin.render_override = lambda renderer: False
    renderer.register_plugin(plugin)

    renderer.render_frame()
    assert plugin.pre_render_called
    assert plugin.post_render_called
