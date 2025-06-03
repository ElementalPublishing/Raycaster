from raycaster.plugin import RendererPlugin

class DummyRenderer:
    pass

def test_pre_render_called():
    class MyPlugin(RendererPlugin):
        def __init__(self):
            self.called = False
        def pre_render(self, renderer):
            self.called = True

    plugin = MyPlugin()
    renderer = DummyRenderer()
    plugin.pre_render(renderer)
    assert plugin.called

def test_post_render_called():
    class MyPlugin(RendererPlugin):
        def __init__(self):
            self.called = False
        def post_render(self, renderer):
            self.called = True

    plugin = MyPlugin()
    renderer = DummyRenderer()
    plugin.post_render(renderer)
    assert plugin.called

def test_render_override_default_false():
    plugin = RendererPlugin()
    renderer = DummyRenderer()
    assert plugin.render_override(renderer) is False

def test_render_override_custom_true():
    class MyPlugin(RendererPlugin):
        def render_override(self, renderer):
            return True

    plugin = MyPlugin()
    renderer = DummyRenderer()
    assert plugin.render_override(renderer) is True