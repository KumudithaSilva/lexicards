from tkinter import Tk
from lexicards.controllers.data_retriever import CSVDataRetrieverFactory


def main():
    root = Tk()

    factory = CSVDataRetrieverFactory("data/japanese_words.csv")
    factory.create_data_retriever()

    root.mainloop()


if __name__ == "__main__":
    main()
