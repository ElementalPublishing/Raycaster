"""
Entry point for the Raycaster Engine.
Allows configuration via command-line arguments and plugin selection.
"""

import argparse
from .core.engine import RaycastingEngine
from .core.config import EngineConfig
import tkinter as tk
from tkinter import simpledialog


def select_backend():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    backend = simpledialog.askstring(
        "Select Backend",
        "Enter backend to use (pygame/renderer):",
        initialvalue="pygame",
    )
    root.destroy()
    return backend or "pygame"


def main():
    backend = select_backend()  # <-- Add this line

    parser = argparse.ArgumentParser(description="Raycaster Engine")
    parser.add_argument(
        "--resolution",
        type=str,
        default="640x480",
        help="Screen resolution (e.g., 800x600)",
    )
    parser.add_argument(
        "--map", type=str, default="assets/maps/basic_map.json", help="Path to map file"
    )
    parser.add_argument("--fps", action="store_true", help="Show FPS counter")
    args = parser.parse_args()

    try:
        width, height = map(int, args.resolution.lower().split("x"))
    except Exception:
        print("Invalid resolution format. Use WIDTHxHEIGHT, e.g., 800x600.")
        return

    config = EngineConfig(resolution=(width, height), map_path=args.map)
    engine = RaycastingEngine(config, backend=backend)  # <-- Pass backend here

    print(f"Starting Raycaster Engine at {width}x{height} with map {args.map} using backend '{backend}'")
    engine.run()


if __name__ == "__main__":
    main()
