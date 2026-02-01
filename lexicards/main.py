import platform
from tkinter import Tk

from lexicards.audio.audio_service import AudioService
from lexicards.controllers.lexical_controller import LexicalController
from lexicards.data.data_loader import ResourceLoader
from lexicards.data.data_remover import CSVDataRemoverFactory
from lexicards.data.data_retriever import CSVDataRetrieverFactory
from lexicards.data.data_saver import CSVDataSaverFactory
from lexicards.manager.word_manager import WordManager
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

    icon_path = loader.get_resource_path("lexicards.ico")
    root.iconbitmap(icon_path)

    images = {
        "card_front_image": loader.load_image("card_front.png"),
        "card_back_image": loader.load_image("card_back.png"),
        "wrong_image": loader.load_image("wrong.png"),
        "right_image": loader.load_image("right.png"),
        "audio_image": loader.load_image("audio.png"),
        "next_image": loader.load_image("next.png"),
    }

    # -----------------------------
    # Platform-specific UI setup
    # -----------------------------
    if current_os == "Darwin":
        builder = DesktopLexiUiBuilder(root, images)
        director = DesktopUiDirector(builder)
        orchestrator_class = UiOrchestrator
    else:
        builder = MacLexiUiBuilder(root, images)
        director = MacUiDirector(builder)
        orchestrator_class = MacUiOrchestrator

    # -----------------------------
    # Construct and initialize UI
    # -----------------------------
    ui = director.construct_ui()
    ui_manager = UiManager(ui, images)

    # -----------------------------
    # Controller & Wiring
    # -----------------------------

    retriever = CSVDataRetrieverFactory()
    saver_factory = CSVDataSaverFactory(
        foreign_language="Japanese", native_language="English"
    )
    remover_factory = CSVDataRemoverFactory()

    # -----------------------------
    # WordManager
    # -----------------------------
    manager = WordManager(
        loader_factory=retriever,
        saver_factory=saver_factory,
        data_remover=remover_factory,
        source_file="japanese_words.csv",
    )

    # -----------------------------
    # Audio
    # -----------------------------
    audio = AudioService()

    # -----------------------------
    # Controller
    # -----------------------------
    controller = LexicalController(ui_manager, manager, audio)

    # -----------------------------
    # Orchestrator
    # -----------------------------
    orchestrator = orchestrator_class(ui)
    orchestrator.wire_callbacks(controller)

    # -----------------------------
    # Start app
    # -----------------------------
    root.mainloop()


if __name__ == "__main__":
    main()
