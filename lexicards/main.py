from tkinter import Tk

from lexicards.resources import ResourceLoader


def main():
    root = Tk()
    loader = ResourceLoader()

    images = {
        "main_logo": loader.load_image("lexicards.png"),
        "main_icon": loader.get_resource_path("lexicards.ico"),
    }

    root.mainloop()


if __name__ == "__main__":
    main()
