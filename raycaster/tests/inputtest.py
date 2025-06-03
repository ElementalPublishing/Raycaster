import pytest

from raycaster.core.input import InputHandler


class DummyPlayer:
    def __init__(self):
        self.actions = []

    def move_forward(self):
        self.actions.append("forward")

    def move_backward(self):
        self.actions.append("backward")

    def strafe_left(self):
        self.actions.append("left")

    def strafe_right(self):
        self.actions.append("right")

    def turn_left(self):
        self.actions.append("turn_left")

    def turn_right(self):
        self.actions.append("turn_right")


def make_keys(pressed_indices, length=300):
    keys = [False] * length
    for idx in pressed_indices:
        keys[idx] = True
    return keys


def test_move_forward(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([119])  # pygame.K_w == 119
    handler.process_input(keys)
    assert "forward" in player.actions


def test_move_backward(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([115])  # pygame.K_s == 115
    handler.process_input(keys)
    assert "backward" in player.actions


def test_strafe_left(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([97])  # pygame.K_a == 97
    handler.process_input(keys)
    assert "left" in player.actions


def test_strafe_right(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([100])  # pygame.K_d == 100
    handler.process_input(keys)
    assert "right" in player.actions


def test_turn_left(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([276])  # pygame.K_LEFT == 276
    handler.process_input(keys)
    assert "turn_left" in player.actions


def test_turn_right(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([275])  # pygame.K_RIGHT == 275
    handler.process_input(keys)
    assert "turn_right" in player.actions


def test_no_action(monkeypatch):
    player = DummyPlayer()
    handler = InputHandler(player)
    keys = make_keys([])  # No keys pressed
    handler.process_input(keys)
    assert player.actions == []
