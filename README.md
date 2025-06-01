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
   (e.g., `pygame`: `pip install pygame`)
2. **Run the engine**  
   ```sh
   python -m raycaster.main
   ```
3. **Customize**  
   Edit the modules to add features, logic, and rendering.

## Changelog

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
