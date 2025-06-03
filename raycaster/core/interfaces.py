from abc import ABC, abstractmethod
from .baserenderer import BaseRenderer


class BaseInputHandler(ABC):
    """
    Abstract base class for all input handler backends.
    """

    @abstractmethod
    def process_input(self):
        """Process input events and update game state."""
        pass
