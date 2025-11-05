from lexicards.interfaces.ui.i_ui_orchestrator import IUiOrchestrator


class UiOrchestrator(IUiOrchestrator):
    """Connects UI components with the controller actions."""

    def __init__(self, ui):
        self.ui = ui

    def wire_callbacks(self, controller):
        """Wire UI button events to controller logic."""
        self.ui.set_known_callback(controller.generate_random_new_word)
        self.ui.set_unknown_callback(controller.generate_random_unknown_word)
        self.schedule_auto_meaning(controller)

    def schedule_auto_meaning(self, controller):
        """Automatically refresh meaning every few seconds."""
        def update_meaning():
            controller.generate_word_meaning()
            self.ui.get_root().after(5000, update_meaning)
        self.ui.get_root().after(5000, update_meaning)

