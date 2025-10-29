from tkinter import Tk

from lexicards.controllers.data_loader import ResourceLoader
from lexicards.controllers.data_retriever import CSVDataRetrieverFactory
from lexicards.ui.lexi_ui_test import LexiUi
from lexicards.controllers.lexical_controller import LexicalController


def main():
    root = Tk()
    loader = ResourceLoader()

    images = {
        "card_front_image": loader.load_image("card_front.png"),
        "wrong_image": loader.load_image("wrong.png"),
        "right_image": loader.load_image("right.png"),
    }

    ui = LexiUi(root, images)
    retriever = CSVDataRetrieverFactory("data/japanese_words.csv").create_data_retriever()
    LexicalController(ui, retriever)

    root.mainloop()


if __name__ == "__main__":
    main()
