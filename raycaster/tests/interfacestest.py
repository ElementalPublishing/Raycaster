import pytest
from raycaster.core.interfaces import BaseRenderer, BaseInputHandler

def test_base_renderer_abstract_methods():
    # Attempting to instantiate BaseRenderer directly should fail
    with pytest.raises(TypeError):
        BaseRenderer()

    # Subclass must implement all abstract methods
    class DummyRenderer(BaseRenderer):
        def render_frame(self): return "frame"
        def flip(self): return "flip"
        def tick(self, framerate: int): return f"tick {framerate}"

    renderer = DummyRenderer()
    assert renderer.render_frame() == "frame"
    assert renderer.flip() == "flip"
    assert renderer.tick(60) == "tick 60"
    # Optional cleanup should not raise
    renderer.cleanup()

def test_base_input_handler_abstract_methods():
    with pytest.raises(TypeError):
        BaseInputHandler()

    class DummyInputHandler(BaseInputHandler):
        def process_input(self): return "input"

    handler = DummyInputHandler()
    assert handler.process_input() == "input"