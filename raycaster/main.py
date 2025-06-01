"""
Example entry point: sets up the engine and runs the game.
"""

from .engine import RaycastingEngine
from .config import EngineConfig

def main():
    config = EngineConfig()
    engine = RaycastingEngine(config)
    engine.run()

if __name__ == "__main__":
    main()