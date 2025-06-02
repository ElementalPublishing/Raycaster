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
├── backend/                # (Optional) Native or performance-critical modules
│   └── ...
├── core/                   # Main engine logic and orchestration
│   ├── engine.py
│   ├── renderer.py         # Raycasting renderer (plugin-ready, multi-core, overrideable)
│   ├── map.py
│   ├── player.py
│   ├── input.py
│   ├── config.py
│   └── events.py
├── plugins/                # Example and custom renderer plugins
│   ├── __init__.py
│   └── example_plugin.py
├── assets/                 # Maps, textures, audio, etc.
│   ├── maps/
│   │   └── example.json
│   ├── textures/
│   ├── audio/
│   └── ...
├── shared/                 # Utilities, math, helpers
│   ├── utils.py
│   └── math.py
├── ui/                     # UI, HUD, menus, overlays
│   ├── hud.py
│   └── menu.py
├── tests/                  # Unit and integration tests
│   └── ...
├── examples/               # Example games, scripts, or demos
│   └── ...
├── docs/                   # Documentation, guides, architecture diagrams
│   └── ...
├── main.py                 # Entry point
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

- **Modular:** Each subsystem is in its own file/folder for clarity and easy extension.
- **Plugins:** Drop Python scripts in `plugins/` to add overlays, effects, new renderers, or even fully override rendering.
- **Assets:** Place maps, textures, and sounds in the `assets/` folder.

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
