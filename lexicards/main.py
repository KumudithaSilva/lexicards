from tkinter import Tk

from lexicards.data_retriever import DataRetriever
from lexicards.lexicard_controller import LexicalController
from lexicards.resources import ResourceLoader
from lexicards.ui import LexiUI


def main():
    root = Tk()
    loader = ResourceLoader()

    images = {
        "card_front_image": loader.load_image("card_front.png"),
        "wrong_image": loader.load_image("wrong.png"),
        "right_image": loader.load_image("right.png"),
    }

    ui = LexiUI(root, images)
    retriever = DataRetriever()
    LexicalController(ui, retriever)

    root.mainloop()


if __name__ == "__main__":
    main()
