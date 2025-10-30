import platform
from tkinter import Tk

from lexicards.controllers.data_loader import ResourceLoader
from lexicards.controllers.data_retriever import CSVDataRetrieverFactory
from lexicards.ui.builders.desktop_builder import DesktopLexiUiBuilder
from lexicards.controllers.lexical_controller import LexicalController
from lexicards.ui.builders.mac_builder import MacLexiUiBuilder
from lexicards.ui.director.ui_director import LexiUiDirector


def main():
    current_os = platform.system()
    root = Tk()
    loader = ResourceLoader()

    images = {
        "card_front_image": loader.load_image("card_front.png"),
        "wrong_image": loader.load_image("wrong.png"),
        "right_image": loader.load_image("right.png"),
        "audio_image": loader.load_image("audio.png"),
    }

    if current_os == "Darwin":
        builder = MacLexiUiBuilder(root, images)
    else:
        builder = DesktopLexiUiBuilder(root, images)

    director = LexiUiDirector(builder)
    ui = director.build_ui()
    retriever = CSVDataRetrieverFactory("data/japanese_words.csv").create_data_retriever()
    LexicalController(ui, retriever)

    root.mainloop()


if __name__ == "__main__":
    main()
