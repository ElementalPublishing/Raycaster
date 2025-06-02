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
raycaster/
│
├── backend/                      # Performance-critical routines (Cython only)
│   ├── __init__.py               # Backend interface/loader
│   ├── cython_backend.pyx        # Cython backend (compiled for speed)
│   └── api.py                    # Python API for backend (defines interface, docstrings)
│
├── core/                         # Main engine logic and orchestration
│   ├── __init__.py
│   ├── engine.py
│   ├── renderer.py
│   ├── map.py
│   ├── player.py
│   ├── input.py
│   ├── config.py
│   └── events.py
│
├── plugins/                      # Example and custom renderer plugins
│   ├── __init__.py
│   └── example_plugin.py
│
├── assets/                       # Maps, textures, audio, etc.
│   ├── maps/
│   │   └── example.json
│   ├── textures/
│   ├── audio/
│   └── ...
│
├── shared/                       # Utilities, math, helpers
│   ├── __init__.py
│   ├── utils.py
│   └── math.py
│
├── ui/                           # UI, HUD, menus, overlays
│   ├── __init__.py
│   ├── hud.py
│   └── menu.py
│
├── tests/                        # Unit and integration tests
│   └── ...
│
├── examples/                     # Example games, scripts, or demos
│   └── ...
│
├── docs/                         # Documentation, guides, architecture diagrams
│   └── ...
│
├── main.py                       # Entry point
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

- **backend/**: All performance-critical code is written in Cython (`cython_backend.pyx`). The `api.py` file defines the backend interface and documents how to extend or modify backend routines. Only Cython is supported for backend optimization, making it easy for Python developers to contribute and mod.
- **core/**: All game logic, orchestration, and engine features remain in Python for maximum flexibility and developer friendliness.
- **plugins/**: Drop Python scripts in `plugins/` to add overlays, effects, or new renderers.
- **assets/**: Place maps, textures, and sounds in the `assets/` folder.
- **shared/**: Utilities and helpers for use across the engine.
- **ui/**: User interface, HUD, and menu code.
- **tests/**, **examples/**, **docs/**: For testing, demos, and documentation.

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
- No native dependencies required by default; optional backend folder for future C/C++/Rust modules.

---

## Contributing

- Keep code modular and well-documented.
- Use type hints and docstrings.
- Add examples for new features.
- Open issues or pull requests for suggestions and improvements.

---

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details.
