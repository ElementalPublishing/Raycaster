import os

from raycaster.core.pygame_backend import PygameInputHandler, PygameRenderer


class DummyMap:
    pass


class DummyPlayer:
    angle = 0


class DummyConfig:
    resolution = (32, 32)
    map_path = "dummy.json"


def test_renderer_init_headless(monkeypatch):
    # Ensure headless mode sets SDL_VIDEODRIVER
    monkeypatch.setenv("SDL_VIDEODRIVER", "")
    renderer = PygameRenderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    assert os.environ["SDL_VIDEODRIVER"] == "dummy"
    assert renderer.screen.get_width() == 32
    assert renderer.screen.get_height() == 32


def test_render_frame_and_flip(monkeypatch):
    renderer = PygameRenderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    # Should not raise
    renderer.render_frame()
    renderer.flip()


def test_tick(monkeypatch):
    renderer = PygameRenderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    renderer.tick(30)  # Should not raise


def test_cleanup(monkeypatch):
    renderer = PygameRenderer(DummyMap(), DummyPlayer(), DummyConfig(), headless=True)
    renderer.cleanup()  # Should not raise


def test_input_handler(monkeypatch):
    player = DummyPlayer()
    handler = PygameInputHandler(player)
    # Patch pygame.event.get and pygame.key.get_pressed
    monkeypatch.setattr("pygame.event.get", lambda: [])
    monkeypatch.setattr("pygame.key.get_pressed", lambda: [0] * 300)
    events = handler.process_events()
    assert isinstance(events, list)
    handler.process_input()  # Should not raise
