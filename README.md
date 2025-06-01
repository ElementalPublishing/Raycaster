# Raycaster Engine

A modular, developer-friendly Python raycasting engine template for retro-style shooters.

## Features

- Configurable resolution and field of view (FOV)
- Modular codebase for easy extension
- **Plugin system** for renderer customization and overlays
- Advanced renderer architecture for future features
- Map loading from JSON files
- Player movement and collision detection
- Designed for learning, prototyping, and retro game development

## Project Structure

- `engine.py` — Main engine loop and core logic
- `renderer.py` — Raycasting renderer (now supports plugins)
- `map.py` — Map loading and collision detection
- `player.py` — Player state and movement
- `input.py` — Input handling
- `config.py` — Engine configuration
- `main.py` — Example entry point
- `plugins/` — Example and custom renderer plugins

## Getting Started

1. **Install dependencies**  
   ```sh
   poetry install
   ```

2. **Run the engine**  
   ```sh
   poetry run python -m raycaster.main
   ```
   or, if you set up the script entry point:
   ```sh
   poetry run raycaster
   ```

3. **Customize**  
   Edit the modules to add features, logic, and rendering.

## Changelog

### v0.7.1
- Patch release: Update dependency constraints for Black and Python 3.9+ compatibility.

### v0.7.0
- Raised minimum Python version to 3.12.0 for modern language features and compatibility.
- Added Black as a development dependency for automatic code formatting.
- Applied PEP8 formatting and improved code style across all modules.
- Updated documentation and project configuration for clarity and maintainability.

### v0.6.0
- Added support for loading map files from JSON, enabling easy map editing and expansion.
- Clarified and documented the recommended project folder structure (`assets/maps/`).
- Improved configuration: map file path is now set via `config.map_path`.
- Updated documentation and code comments for better usability.

### v0.5.0
- Added a main engine loop with proper event handling and frame limiting.
- The engine window now stays open and responds to user input/events.
- Integrated input processing and player updates into the main loop.
- Improved overall engine structure for future expansion.
- Project version and dependencies updated in `pyproject.toml`.

### v0.4.0
- Graphics context initialization with `pygame`—the engine now opens a window and is ready for rendering.
- Improved renderer structure for future extensibility and plugin support.
- Project now fully managed with Poetry for easier dependency and package management.
- General code cleanup and preparation for next development steps.

### v0.3.0
- Improved entry point with command-line argument parsing (resolution, map, FPS counter).
- Users can now toggle plugins and set options from the command line.

### v0.2.0
- Introduced a flexible plugin system for the renderer, allowing easy extension and customization.
- Scaffolded an advanced renderer architecture to support future features and plugins.
- Added an example FPS counter plugin.
- Improved code modularity and scalability for future development.
- Updated documentation and project structure.

## Contributing

- Keep code modular and well-documented.
- Use type hints and docstrings.
- Add examples for new features.
- Open issues or pull requests for suggestions and improvements.

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details.
