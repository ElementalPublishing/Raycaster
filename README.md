# Raycaster Engine

A modular, developer-friendly Python raycasting engine template for retro-style shooters.

---

## Features

- Cross-platform: Runs on Windows, macOS, and Linux (Python 3.12+)
- Configurable resolution and field of view (FOV)
- Modular codebase for easy extension and maintenance
- **Plugin system** for renderer customization, overlays, and even full rendering override
- Advanced renderer architecture (multi-core support, future GPU/extension ready)
- Map loading from JSON files
- Player movement and collision detection
- Designed for learning, prototyping, and retro game development

---

## Developer Experience

- **Clear, documented code:** All modules include docstrings and inline comments.
- **Type hints everywhere:** For better editor support and fewer bugs.
- **Hot-reload plugins:** Drop new Python files in `plugins/` and see changes on restart.
- **Minimal setup:** One command to install, one to run.
- **Extensive examples:** See `plugins/` and `assets/maps/` for ready-to-use templates.
- **Easy debugging:** Modular design means you can test or swap out any subsystem.
- **Contributing guide:** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add features or report issues.
- **Active changelog:** Stay up to date with every release.

---

## Project Structure

```
Raycaster/                        # Project root (repo root)
│
├── pyproject.toml                # Build and dependency config (root)
├── README.md                     # Project overview and instructions (root)
├── CONTRIBUTING.md               # Contribution guidelines (root)
├── LICENSE                       # License file (root)
├── .gitignore                    # Git ignore rules (root)
│
└── raycaster/                    # Main Python package and all engine code
    │
    ├── backend/                  # Performance-critical routines (Cython only)
    │   ├── __init__.py           # Backend interface/loader
    │   ├── cython_backend.pyx    # Cython backend (compiled for speed)
    │   └── api.py                # Python API for backend (defines interface, docstrings)
    │
    ├── core/                     # Main engine logic and orchestration
    │   ├── __init__.py
    │   ├── engine.py
    │   ├── renderer.py
    │   ├── map.py
    │   ├── player.py
    │   ├── input.py
    │   ├── config.py
    │   └── events.py
    │
    ├── plugins/                  # Example and custom renderer plugins
    │   ├── __init__.py
    │   └── example_plugin.py
    │
    ├── assets/                   # Maps, textures, audio, etc.
    │   ├── maps/
    │   │   └── example.json
    │   ├── textures/
    │   ├── audio/
    │   └── ...
    │
    ├── shared/                   # Utilities, math, helpers
    │   ├── __init__.py
    │   ├── utils.py
    │   └── math.py
    │
    ├── ui/                       # UI, HUD, menus, overlays
    │   ├── __init__.py
    │   ├── hud.py
    │   └── menu.py
    │
    ├── tests/                    # Unit and integration tests
    │   └── ...
    │
    ├── examples/                 # Example games, scripts, or demos
    │   └── ...
    │
    ├── docs/                     # Documentation, guides, architecture diagrams
    │   └── ...
    │
    ├── main.py                   # Entry point
    ├── plugin.py                 # Plugin system core
    └── ...
```

- **All configuration and documentation files** (`pyproject.toml`, `README.md`, `CONTRIBUTING.md`, `LICENSE`, `.gitignore`) are in the **project root**.
- **All code, assets, and engine modules** are inside the `raycaster/` package directory.
- This structure matches your GitHub repository and is ready for packaging and distribution.

---

## Backend Modding & Extensibility

The backend is designed to be **modular and easy to extend**, inspired by popular moddable games:

- **All backend routines are defined in `backend/api.py`** with clear docstrings and type hints.
- **Performance-critical implementations are in `cython_backend.pyx`**. Developers can optimize or swap out routines as long as they match the API.
- **To mod or extend the backend:**  
  1. Read the API in `backend/api.py`.
  2. Implement or optimize routines in `cython_backend.pyx`.
  3. Rebuild the Cython extension (see docs for build instructions).

This approach keeps the backend fast, modular, and accessible for Python developers—no C++ or Rust required!

---

## Plugin Rendering Override

The engine now supports **full rendering override by plugins**.  
If a plugin implements a `render_override(renderer)` method and returns `True`, the default rendering is skipped and the plugin takes full control of the frame rendering.

**Example plugin interface:**
```python
class RendererPlugin:
    def pre_render(self, renderer):
        pass

    def post_render(self, renderer):
        pass

    def render_override(self, renderer):
        # Return True to skip default rendering
        return False
```

---

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
   - Edit modules or add plugins in `plugins/` to extend features and rendering.
   - Add new maps to `assets/maps/` (JSON format).

---

## Quickstart

1. Clone the repo and install dependencies:
   ```sh
   git clone https://github.com/yourname/raycaster.git
   cd raycaster
   poetry install
   ```

2. Run the engine:
   ```sh
   poetry run python -m raycaster.main
   ```
   or, if you set up the script entry point:
   ```sh
   poetry run raycaster
   ```

3. Customize:
   - Edit modules or add plugins in `plugins/` to extend features and rendering.
   - Add new maps to `assets/maps/` (JSON format).

---

## Cross-Platform Notes

- Requires **Python 3.12+** and [Poetry](https://python-poetry.org/).
- Uses only cross-platform libraries (e.g., `pygame`).
- Multi-core rendering uses Python’s `concurrent.futures` for best performance on all modern CPUs.
- No native dependencies required by default; backend uses Cython for speed.

---

## Contributing

- Keep code modular and well-documented.
- Use type hints and docstrings.
- Add examples for new features.
- Open issues or pull requests for suggestions and improvements.

---

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details.

---

## Changelog

### v0.10.0
- **Added support for a modular Cython backend:** Performance-critical routines can now be implemented in Cython for improved speed and Python developer accessibility.
- **Modular backend API:** All backend routines are defined in `backend/api.py` with clear docstrings and type hints, making it easy to extend or optimize.
- **Project structure finalized:** 
  - All config and documentation files (`pyproject.toml`, `README.md`, etc.) are in the project root.
  - All code, assets, and engine modules are inside the `raycaster/` package directory.
- **Plugin system improvements:** Plugins can fully override rendering or add overlays/effects with a simple interface.
- **Hot-reload plugins:** Drop new Python files in `plugins/` and see changes on restart.
- **Expanded dev dependencies:** Added `pytest`, `pytest-cov`, `mypy`, `flake8`, `pre-commit`, and `isort` for a robust, modern development workflow.
- **Improved documentation:** Updated README and API docs for clarity and onboarding.
- **Cross-platform:** Works on Windows, macOS, and Linux (Python 3.12+).
- **Easy modding:** Backend and plugins are easy to extend and customize, inspired by popular moddable games.

---

### v0.9.1
- Initial modular structure established.
- Plugin system introduced for renderer customization.
- Added hot-reload support for plugins.
- Improved documentation and developer onboarding.
- Added example maps and plugins.
- Established cross-platform compatibility (Python 3.12+, Poetry).
- Added type hints and docstrings throughout the codebase.

---

### v0.9.0
- Renderer now uses ProcessPoolExecutor for multi-core raycasting, enabling efficient parallel rendering on modern CPUs.
- Improved performance and scalability for a wide range of hardware.

---

### v0.8.0
- Added keyboard input handling to InputHandler for player movement (WASD and arrow keys).

---

### v0.7.1
- Patch release: Update dependency constraints for Black and Python 3.9+ compatibility.

---

### v0.7.0
- Raised minimum Python version to 3.12.0 for modern language features and compatibility.
- Added Black as a development dependency for automatic code formatting.
- Applied PEP8 formatting and improved code style across all modules.
- Updated documentation and project configuration for clarity and maintainability.

---

### v0.6.0
- Added support for loading map files from JSON, enabling easy map editing and expansion.
- Clarified and documented the recommended project folder structure (`assets/maps/`).
- Improved configuration: map file path is now set via `config.map_path`.
- Updated documentation and code comments for better usability.

---

### v0.5.0
- Added a main engine loop with proper event handling and frame limiting.
- The engine window now stays open and responds to user input/events.
- Integrated input processing and player updates into the main loop.
- Improved overall engine structure for future expansion.
- Project version and dependencies updated in `pyproject.toml`.
- Added multi-core rendering support.
- Improved asset management and map loading.
- Enhanced player movement and collision detection.
- Refined plugin API for overlays and effects.
- Added more example plugins and maps.

---

### v0.4.0
- Graphics context initialization with `pygame`—the engine now opens a window and is ready for rendering.
- Improved renderer structure for future extensibility and plugin support.
- Project now fully managed with Poetry for easier dependency and package management.
- General code cleanup and preparation for next development steps.

---

### v0.3.0
- Improved entry point with command-line argument parsing (resolution, map, FPS counter).
- Users can now toggle plugins and set options from the command line.
- Introduced UI and HUD modules.
- Added shared utilities and math helpers.
- Improved code organization and modularity.
- Added first round of unit tests.

---

### v0.2.0
- Introduced a flexible plugin system for the renderer, allowing easy extension and customization.
- Scaffolded an advanced renderer architecture to support future features and plugins.
- Added an example FPS counter plugin.
- Improved code modularity and scalability for future development.
- Updated documentation and project structure.

---

### v0.1.0
- Initial commit.
- Project initialized.
- Basic raycasting engine implemented in Python.
- Simple map and player movement.
- Basic plugin system scaffolded.
- Initial documentation and project structure.
