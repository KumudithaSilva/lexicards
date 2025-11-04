from lexicards.interfaces.ui.i_ui_director import IUiDirector


class MacUiDirector(IUiDirector):
    """Coordinates the UI building process using a given builder."""

    def __init__(self, builder):
        self.builder = builder

    def construct_ui(self):
        self.builder.build_window()
        self.builder.build_canvas()
        self.builder.create_title_label()
        self.builder.create_word_label()
        self.builder.build_title_text()
        self.builder.build_word_text()
        self.builder.build_buttons()
        self.builder.build_audio_button()

        return self.builder.get_ui()
