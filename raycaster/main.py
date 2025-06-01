"""
Entry point for the Raycaster Engine.
Allows configuration via command-line arguments and plugin selection.
"""

import argparse
from .engine import RaycastingEngine
from .config import EngineConfig
from .plugins.fps_counter import FPSCounterPlugin

def main():
    parser = argparse.ArgumentParser(description="Raycaster Engine")
    parser.add_argument("--resolution", type=str, default="640x480", help="Screen resolution (e.g., 800x600)")
    parser.add_argument("--map", type=str, default="assets/maps/basic_map.json", help="Path to map file")
    parser.add_argument("--fps", action="store_true", help="Show FPS counter")
    args = parser.parse_args()

    try:
        width, height = map(int, args.resolution.lower().split('x'))
    except Exception:
        print("Invalid resolution format. Use WIDTHxHEIGHT, e.g., 800x600.")
        return

    config = EngineConfig(resolution=(width, height), map_path=args.map)
    engine = RaycastingEngine(config)

    if args.fps:
        engine.renderer.register_plugin(FPSCounterPlugin())

    print(f"Starting Raycaster Engine at {width}x{height} with map {args.map}")
    engine.run()

if __name__ == "__main__":
    main()