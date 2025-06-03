import pytest
from raycaster.core.config import EngineConfig


def test_config_defaults():
    config = EngineConfig()
    assert config.resolution == (640, 480)
    assert config.fov == 60.0
    assert config.map_path == "assets/maps/basic_map.json"


def test_config_custom_values():
    config = EngineConfig(
        resolution=(800, 600), fov=90.0, map_path="foo/bar.json", custom="yes"
    )
    assert config.resolution == (800, 600)
    assert config.fov == 90.0
    assert config.map_path == "foo/bar.json"
    assert config.custom == "yes"


def test_config_invalid_resolution():
    with pytest.raises(ValueError):
        EngineConfig(resolution=(0, 480))
    with pytest.raises(ValueError):
        EngineConfig(resolution=(640,))
    with pytest.raises(ValueError):
        EngineConfig(resolution="not_a_tuple")


def test_config_invalid_fov():
    with pytest.raises(ValueError):
        EngineConfig(fov=0)
    with pytest.raises(ValueError):
        EngineConfig(fov=-10)


def test_config_invalid_map_path():
    with pytest.raises(ValueError):
        EngineConfig(map_path="")
    with pytest.raises(ValueError):
        EngineConfig(map_path=None)
