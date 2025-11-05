import platform
from tkinter import Tk

from lexicards.controllers.data_loader import ResourceLoader
from lexicards.controllers.data_retriever import CSVDataRetrieverFactory
from lexicards.controllers.lexical_controller import LexicalController
from lexicards.ui.builders.desktop_ui_builder import DesktopLexiUiBuilder
from lexicards.ui.builders.mac_ui_builder import MacLexiUiBuilder
from lexicards.ui.director.ui_desktop_director import DesktopUiDirector
from lexicards.ui.director.ui_mac_director import MacUiDirector
from lexicards.ui.manager.ui_manager import UiManager
from lexicards.ui.orchestrator.ui_mac_orchestrator import MacUiOrchestrator
from lexicards.ui.orchestrator.ui_orchestrator import UiOrchestrator


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

    # -----------------------------
    # Platform-specific UI setup
    # -----------------------------
    if current_os == "Darwin":
        builder = MacLexiUiBuilder(root, images)
        director = MacUiDirector(builder)
        orchestrator_class = MacUiOrchestrator
    else:
        builder = DesktopLexiUiBuilder(root, images)
        director = DesktopUiDirector(builder)
        orchestrator_class = UiOrchestrator

    # -----------------------------
    # Construct and initialize UI
    # -----------------------------
    ui = director.construct_ui()
    ui_manager = UiManager(ui)

    # -----------------------------
    # Controller & Wiring
    # -----------------------------
    retriever = CSVDataRetrieverFactory(
        "data/japanese_words.csv"
    ).create_data_retriever()
    controller = LexicalController(ui_manager, retriever)

    orchestrator = orchestrator_class(ui)
    orchestrator.wire_callbacks(controller)

    # -----------------------------
    # Start app
    # -----------------------------
    root.mainloop()


if __name__ == "__main__":
    main()
