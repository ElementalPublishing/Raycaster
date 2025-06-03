"""
Event system: allows registering and dispatching custom events
for plugins and engine hooks.
"""

from typing import Callable, Dict, List, Optional


class Event:
    """
    Represents a generic event.
    """

    def __init__(self, name: str, data: Optional[dict] = None):
        self.name = name
        self.data = data or {}


class EventDispatcher:
    """
    Manages event listeners and dispatches events to them.
    """

    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}

    def register(self, event_name: str, listener: Callable):
        """
        Register a listener for a specific event name.
        """
        self.listeners.setdefault(event_name, []).append(listener)

    def unregister(self, event_name: str, listener: Callable):
        """
        Unregister a listener from a specific event name.
        """
        if event_name in self.listeners:
            self.listeners[event_name].remove(listener)

    def clear(self):
        """
        Remove all listeners (useful for tests).
        """
        self.listeners.clear()

    def dispatch(self, event_name: str, data: Optional[dict] = None) -> int:
        """
        Dispatch an event to all registered listeners.
        Returns the number of listeners called.
        """
        event = Event(event_name, data)
        count = 0
        for listener in self.listeners.get(event_name, []):
            count += 1  # Increment before calling the listener
            try:
                listener(event)
            except Exception as e:
                print(f"[EventDispatcher] Error in listener for '{event_name}': {e}")
                # Do not raise, continue to next listener
        return count
