from lexicards.interfaces.ui.i_ui_orchestrator import IUiOrchestrator


class UiOrchestrator(IUiOrchestrator):
    """Connects UI components with the controller actions."""

    def __init__(self, ui):
        self.ui = ui

    def wire_callbacks(self, controller):
        """Wire UI button events to controller logic."""
        self.ui.get_root().after(1000, controller.start_first_word)
        self.ui.set_known_callback(controller.handle_known_word)
        self.ui.set_unknown_callback(controller.handle_unknown_word)
        self.ui.set_next_callback(controller.handle_next_word)
