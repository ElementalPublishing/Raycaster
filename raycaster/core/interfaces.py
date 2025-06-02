from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    @abstractmethod
    def render_frame(self):
        pass

    @abstractmethod
    def flip(self):
        pass

    @abstractmethod
    def tick(self, framerate: int):
        pass

class BaseInputHandler(ABC):
    @abstractmethod
    def process_input(self):
        pass