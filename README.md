# Raycaster Engine

A modular, developer-friendly Python raycasting engine template for retro-style shooters.

## Features

- Configurable resolution and field of view (FOV)
- Modular codebase for easy extension
- Map loading from JSON files
- Player movement and collision detection
- Designed for learning, prototyping, and retro game development

## Project Structure

- `engine.py` — Main engine loop and core logic
- `renderer.py` — Raycasting renderer
- `map.py` — Map loading and collision detection
- `player.py` — Player state and movement
- `input.py` — Input handling
- `config.py` — Engine configuration
- `main.py` — Example entry point

## Getting Started

1. **Install dependencies**  
   (e.g., `pygame` if used: `pip install pygame`)
2. **Run the engine**  
   ```sh
   python -m raycaster.main
   ```
3. **Customize**  
   Edit the modules to add features, logic, and rendering.

## Contributing

- Keep code modular and well-documented.
- Use type hints and docstrings.
- Add examples for new features.
- Open issues or pull requests for suggestions and improvements.

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details.
