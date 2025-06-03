from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    """
    Abstract base class for all renderer backends.
    """

    @abstractmethod
    def render_frame(self):
        pass

    @abstractmethod
    def flip(self):
        pass

    @abstractmethod
    def tick(self, framerate: int):
        pass

    def cleanup(self):
        pass