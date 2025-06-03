"""
Entry point for the Raycaster Engine.
Allows configuration via command-line arguments and plugin selection.
"""

import argparse
from .core.engine import RaycastingEngine
from .core.config import EngineConfig
import tkinter as tk
from tkinter import simpledialog


def select_backend() -> str:
    """
    Prompt the user to select a backend using a Tkinter dialog.
    Returns the selected backend as a string.
    """
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
    """
    Parse command-line arguments, select backend, and start the engine.
    """
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
    parser.add_argument(
        "--backend",
        type=str,
        choices=["pygame", "renderer"],
        help="Backend to use (overrides GUI prompt)",
    )
    args = parser.parse_args()

    # Allow CLI override for backend (useful for CI/testing)
    backend = args.backend or select_backend()

    try:
        width, height = map(int, args.resolution.lower().split("x"))
    except Exception:
        print("Invalid resolution format. Use WIDTHxHEIGHT, e.g., 800x600.")
        return

    config = EngineConfig(
        resolution=(width, height), map_path=args.map, show_fps=args.fps
    )
    try:
        engine = RaycastingEngine(config, backend=backend)
        print(
            f"Starting Raycaster Engine at {width}x{height} with map {args.map} using backend '{backend}'"
        )
        engine.run()
    except Exception as e:
        print(f"Failed to start engine: {e}")


if __name__ == "__main__":
    main()
