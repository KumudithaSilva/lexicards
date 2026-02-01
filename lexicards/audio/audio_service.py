import threading

import pyttsx3

from lexicards.interfaces.audio.i_audio_servcie import IAudioService


class AudioService(IAudioService):
    """
    Audio service implementation using pyttsx3 for real-time text-to-speech.

    Attributes:
        lock: Threading lock to ensure the TTS engine is used safely in multithreaded environment.
    """

    def __init__(self):
        """
        Initialize the TTS engine, detect available voices, and store them in a dictionary.
        """
        self.lock = threading.Lock()

    # --------------------------
    # Real-time Speech
    # --------------------------
    def speak(self, text: str, lang: str):
        """
        Speak the given text in the specified language.

        Args:
            text (str): Text to be spoken.
            lang (str): Language code ('en', 'ja', 'fr').

        Note:
            pyttsx3 engines cannot be safely reused,
            so a new engine is created per call to ensure speech always works.
        """
        lang = lang.strip().lower().lstrip("\ufeff")[0:2]

        with self.lock:
            engine = pyttsx3.init()
            voice_id = self._select_voice(engine, lang)
            if not voice_id:
                return

            engine.setProperty("voice", voice_id)
            engine.say(text)
            engine.runAndWait()

    def speak_async(self, text: str, lang: str):
        """Run speak in a background thread."""
        threading.Thread(target=self.speak, args=(text, lang), daemon=True).start()

    # --------------------------
    # Voice Detection
    # --------------------------
    @staticmethod
    def _select_voice(engine, lang: str) -> str | None:
        """
        Select a voice matching the requested language.

        Args:
            engine: pyttsx3 engine instance.
            lang (str): Language code ('ja', 'en', 'fr').

        Returns:
            str | None: Voice ID if found, otherwise None.
        """
        for voice in engine.getProperty("voices"):
            vid = voice.id.lower()
            name = voice.name.lower()

            if lang == "ja" and ("ja" in vid or "japanese" in name):
                return voice.id
            if lang == "fr" and ("fr" in vid or "french" in name):
                return voice.id
            if lang == "en" and ("en" in vid or "english" in name):
                return voice.id

        return None
