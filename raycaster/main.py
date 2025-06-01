"""
Example entry point: sets up the engine and runs the game.
"""
from .engine import RaycastingEngine
from .config import EngineConfig
from .plugins.fps_counter import FPSCounterPlugin

def main():
    config = EngineConfig()
    engine = RaycastingEngine(config)
    # Register plugins
    engine.renderer.register_plugin(FPSCounterPlugin())
    engine.run()

if __name__ == "__main__":
    main()