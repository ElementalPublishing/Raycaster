import pygame

from .interfaces import BaseInputHandler, BaseRenderer


class PygameRenderer(BaseRenderer):
    def __init__(self, map_obj, player, config, headless: bool = False):
        # Allow headless mode for CI/testing (no window)
        import os

        if headless:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.init()
        self.screen = pygame.display.set_mode(config.resolution)
        pygame.display.set_caption("Raycaster Engine (Pygame)")
        self.clock = pygame.time.Clock()
        self.map_obj = map_obj
        self.player = player
        self.config = config

    def render_frame(self):
        # Example: fill screen with a color (replace with real rendering)
        self.screen.fill((0, 0, 0))
        # ...your pygame rendering code...

    def flip(self):
        pygame.display.flip()

    def tick(self, framerate: int):
        self.clock.tick(framerate)

    def cleanup(self):
        pygame.quit()


class PygameInputHandler(BaseInputHandler):
    def __init__(self, player):
        self.player = player

    def process_events(self):
        return pygame.event.get()

    def process_input(self, keys=None):
        if keys is None:
            keys = pygame.key.get_pressed()
        # ...input handling logic...
