from raycaster.core.player import Player


def test_player_init_defaults():
    player = Player((1.5, 2.5))
    assert player.x == 1.5
    assert player.y == 2.5
    assert player.angle == 0.0
    assert player.move_speed == 0.05
    assert player.turn_speed == 0.03


def test_player_init_custom_speeds():
    player = Player((0.0, 0.0), move_speed=0.1, turn_speed=0.2)
    assert player.move_speed == 0.1
    assert player.turn_speed == 0.2


def test_player_update_stub():
    player = Player((0.0, 0.0))
    # Should not raise or change state (yet)
    player.update()
    assert player.x == 0.0
    assert player.y == 0.0
    assert player.angle == 0.0
