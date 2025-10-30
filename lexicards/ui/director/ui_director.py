from lexicards.ui.builders.base_builder import LexiUiBuilderAbstract


class LexiUiDirector:

    def __init__(self, builder: LexiUiBuilderAbstract):
        self.builder = builder

    def build_ui(self):
        self.builder.create_new_ui()
        self.builder.build_window()
        self.builder.build_canvas()
        self.builder.build_text_elements()
        self.builder.build_buttons()

        return self.builder.get_result()