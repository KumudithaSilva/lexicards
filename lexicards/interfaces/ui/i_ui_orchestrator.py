from abc import ABC, abstractmethod


class IUiOrchestrator(ABC):
    """Interface for wiring UI events to controller actions."""

    @abstractmethod
    def wire_callbacks(self, controller):
        """Connect UI events' buttons with controller logic."""
        pass

    @abstractmethod
    def schedule_auto_meaning(self, controller):
        """Connect UI events with controller logic."""
        pass
