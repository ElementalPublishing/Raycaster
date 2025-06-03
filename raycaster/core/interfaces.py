from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    """
    Abstract base class for all renderer backends.
    """

    @abstractmethod
    def render_frame(self):
        """Render a single frame."""
        pass

    @abstractmethod
    def flip(self):
        """Update the display (swap buffers)."""
        pass

    @abstractmethod
    def tick(self, framerate: int):
        """Limit the frame rate."""
        pass

    def cleanup(self):
        """Optional: Clean up resources (override if needed)."""
        pass

class BaseInputHandler(ABC):
    """
    Abstract base class for all input handler backends.
    """

    @abstractmethod
    def process_input(self):
        """Process input events and update game state."""
        pass