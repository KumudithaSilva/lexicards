from abc import ABC, abstractmethod


class IAudioService(ABC):
    """
    Abstract base class for audio / text-to-speech services.
    """

    @abstractmethod
    def speak(self, text: str, lang: str):
        """
        Speak the given text in the specified language.

        Args:
            text (str): The word or sentence to speak.
            lang (str): Language code, e.g., 'en', 'ja', 'fr'.
        """
        pass

    @abstractmethod
    def speak_async(self, text: str, lang: str):
        """
        Speak the given text in the specified language in a non-blocking manner.

        Args:
            text (str): The word or sentence to speak.
            lang (str): Language code, e.g., 'en' for English, 'ja' for Japanese,
                        'fr' for French.
        """
        pass
