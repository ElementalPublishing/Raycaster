from ..plugin import RendererPlugin
import time


class FPSCounterPlugin(RendererPlugin):
    def __init__(self):
        self.last_time = time.time()
        self.frame_count = 0

    def post_render(self, renderer):
        self.frame_count += 1
        now = time.time()
        if now - self.last_time >= 1.0:
            print(f"FPS: {self.frame_count}")
            self.frame_count = 0
            self.last_time = now
