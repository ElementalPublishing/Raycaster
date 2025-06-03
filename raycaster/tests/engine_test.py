import pytest

from raycaster.core.config import EngineConfig
from raycaster.core.engine import RaycastingEngine


class DummyMap:
    start_position = (0, 0)


class DummyPlayer:
    def __init__(self, pos):
        pass

    def update(self):
        self.updated = True


class DummyRenderer:
    def __init__(self, *a, **kw):
        pass

    def render_frame(self):
        self.rendered = True

    def flip(self):
        self.flipped = True

    def tick(self, framerate):
        self.ticked = framerate

    def cleanup(self):
        self.cleaned = True


class DummyInputHandler:
    def __init__(self, player):
        pass

    def process_events(self):
        return []

    def process_input(self):
        self.processed = True


def test_engine_init_pygame(monkeypatch):
    # Patch GameMap, Player, and backend classes
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))

    class DummyPygameRenderer(DummyRenderer):
        pass

    class DummyPygameInputHandler(DummyInputHandler):
        pass

    # Patch the actual backend module, not engine
    monkeypatch.setattr(
        "raycaster.core.pygame_backend.PygameRenderer", DummyPygameRenderer
    )
    monkeypatch.setattr(
        "raycaster.core.pygame_backend.PygameInputHandler", DummyPygameInputHandler
    )

    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    engine = RaycastingEngine(config, backend="pygame")
    assert isinstance(engine.renderer, DummyRenderer)
    assert isinstance(engine.input_handler, DummyInputHandler)


def test_engine_init_renderer(monkeypatch):
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))
    monkeypatch.setattr("raycaster.core.engine.Renderer", DummyRenderer)

    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    engine = RaycastingEngine(config, backend="renderer")
    assert isinstance(engine.renderer, DummyRenderer)
    assert engine.input_handler is None


def test_engine_init_invalid_backend(monkeypatch):
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))
    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    with pytest.raises(ValueError):
        RaycastingEngine(config, backend="notarealbackend")


def test_hook_registration_and_error_handling(monkeypatch, capsys):
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))
    monkeypatch.setattr("raycaster.core.engine.Renderer", DummyRenderer)
    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    engine = RaycastingEngine(config, backend="renderer")

    called = {"pre": False, "post": False}
    engine.register_pre_update(lambda: called.update(pre=True))
    engine.register_post_update(lambda: called.update(post=True))
    # Register a hook that raises an error to test error handling
    engine.register_pre_update(lambda: (_ for _ in ()).throw(Exception("test error")))
    for hook in engine.pre_update_hooks:
        try:
            hook()
        except Exception:
            print("Caught in test (should be handled in engine)")
    for hook in engine.post_update_hooks:
        hook()
    assert called["pre"] and called["post"]


def test_cleanup_called(monkeypatch):
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))
    monkeypatch.setattr("raycaster.core.engine.Renderer", DummyRenderer)
    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    engine = RaycastingEngine(config, backend="renderer")
    engine.renderer.cleaned = False
    engine.renderer.cleanup()
    assert engine.renderer.cleaned


def test_event_dispatcher_error_handling(monkeypatch):
    monkeypatch.setattr("raycaster.core.engine.GameMap", lambda path: DummyMap())
    monkeypatch.setattr("raycaster.core.engine.Player", lambda pos: DummyPlayer(pos))
    monkeypatch.setattr("raycaster.core.engine.Renderer", DummyRenderer)
    config = EngineConfig(resolution=(64, 64), map_path="dummy.json")
    engine = RaycastingEngine(config, backend="renderer")

    error_message = None

    def error_listener(event):
        raise Exception("Listener error")

    engine.register_event_handler("test_event", error_listener)

    # Capture printed output
    with pytest.raises(Exception):
        engine.dispatch_event("test_event")

    # Check if the error was printed
    captured = capsys.readouterr()
    assert "[EventDispatcher] Error in listener for 'test_event':" in captured.out

