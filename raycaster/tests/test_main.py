import sys
import pytest

def test_main_valid_args(monkeypatch, capsys):
    # Simulate command-line arguments
    monkeypatch.setattr(sys, "argv", ["main.py", "--resolution", "800x600", "--map", "testmap.json"])
    # Import main module fresh for each test
    import raycaster.main as main_mod

    # Mock select_backend to avoid GUI
    monkeypatch.setattr(main_mod, "select_backend", lambda: "renderer")

    # Dummy engine to capture calls
    called = {}
    class DummyEngine:
        def __init__(self, config, backend):
            called["config"] = config
            called["backend"] = backend
        def run(self):
            called["ran"] = True

    monkeypatch.setattr(main_mod, "RaycastingEngine", DummyEngine)

    main_mod.main()
    out = capsys.readouterr().out
    assert "Starting Raycaster Engine" in out
    assert called["backend"] == "renderer"
    assert called["config"].resolution == (800, 600)
    assert called["config"].map_path == "testmap.json"
    assert called["ran"]

def test_main_invalid_resolution(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "--resolution", "bad", "--map", "testmap.json"])
    import raycaster.main as main_mod
    monkeypatch.setattr(main_mod, "select_backend", lambda: "pygame")
    monkeypatch.setattr(main_mod, "RaycastingEngine", lambda *a, **kw: None)

    main_mod.main()
    out = capsys.readouterr().out
    assert "Invalid resolution format" in out