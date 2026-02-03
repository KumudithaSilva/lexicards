from lexicards.ui.orchestrator.ui_orchestrator import UiOrchestrator


class MacUiOrchestrator(UiOrchestrator):
    """Adds Mac-specific audio wiring."""

    def wire_callbacks(self, controller):
        super().wire_callbacks(controller)
        self.ui.set_audio_callback(controller.handle_speak)
