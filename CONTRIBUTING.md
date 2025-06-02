# Contributing to Raycaster Engine

Thank you for your interest in contributing!  
We welcome bug reports, feature requests, code improvements, and documentation updates.

---

## Project Structure

- **All configuration and documentation files** (`pyproject.toml`, `README.md`, `CONTRIBUTING.md`, `LICENSE`, `.gitignore`) are in the project root.
- **All code, assets, and engine modules** are inside the `raycaster/` package directory.
- **Performance-critical code** is in `raycaster/backend/` (Cython backend, see `api.py` for the interface).
- **Plugins** go in `raycaster/plugins/`.
- **Assets** (maps, textures, audio) go in `raycaster/assets/`.

---

## How to Contribute

### 1. Fork and Clone

- Fork the repository on GitHub.
- Clone your fork locally:
  ```sh
  git clone https://github.com/yourusername/Raycaster.git
  cd Raycaster
  ```

### 2. Set Up Your Environment

- Install [Poetry](https://python-poetry.org/).
- Install dependencies:
  ```sh
  poetry install
  ```

### 3. Make Your Changes

- Add new features or fix bugs in the appropriate module.
- For performance-critical code, update `raycaster/backend/cython_backend.pyx` and ensure the interface matches `api.py`.
- Add or update plugins in `raycaster/plugins/`.
- Add tests in `raycaster/tests/`.

### 4. Code Style & Quality

- Format code with `black` and `isort`.
- Run `flake8` and `mypy` for linting and type checking.
- Run tests with `pytest`.

  ```sh
  poetry run black .
  poetry run isort .
  poetry run flake8 .
  poetry run mypy raycaster/
  poetry run pytest
  ```

### 5. Commit and Push

- Use clear, descriptive commit messages.
- Push your branch to your fork.

### 6. Open a Pull Request

- Go to the original repo and open a Pull Request from your fork/branch.
- Describe your changes and reference any related issues.

---

## Guidelines

- **Keep code modular and well-documented.**
- **Use type hints and docstrings.**
- **Add examples for new features.**
- **Update documentation as needed.**
- **Be respectful and constructive in discussions.**

---

## Need Help?

Open an issue or start a discussion on GitHub.  
Thank you for helping make Raycaster Engine better!