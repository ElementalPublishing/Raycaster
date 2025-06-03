import pytest
from raycaster.core.map import GameMap

def test_init_from_data():
    data = {
        "grid": [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        "start_position": (1.5, 1.5)
    }
    game_map = GameMap(data=data)
    assert game_map.map_data == data["grid"]
    assert game_map.start_position == (1.5, 1.5)

def test_init_from_file(tmp_path):
    map_file = tmp_path / "testmap.json"
    map_content = {
        "grid": [
            [1, 1],
            [0, 1]
        ],
        "start_position": (0.5, 0.5)
    }
    map_file.write_text(str(map_content).replace("'", '"'))
    game_map = GameMap(map_path=str(map_file))
    assert game_map.map_data == map_content["grid"]
    assert game_map.start_position == (0.5, 0.5)

def test_missing_grid_raises():
    data = {"start_position": (1, 1)}
    with pytest.raises(ValueError):
        GameMap(data=data)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        GameMap(map_path="nonexistent.json")

def test_is_wall_and_bounds():
    data = {
        "grid": [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    }
    game_map = GameMap(data=data)
    # Inside wall
    assert game_map.is_wall(0, 0)
    # Inside empty space
    assert not game_map.is_wall(1, 1)
    # Out of bounds
    assert game_map.is_wall(-1, 1)
    assert game_map.is_wall(1, -1)
    assert game_map.is_wall(3, 1)
    assert game_map.is_wall(1, 3)