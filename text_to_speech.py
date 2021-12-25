import gtts
from pathlib import Path

TTS_FOLDER_PATH = Path("audio_files/tts_files")
TTS_FOLDER_PATH.mkdir(parents=True, exist_ok=True)  # make the directory in case it didn't exist

ILLEGAL_WINDOWS_CHAR = {"<": "less than",
                        ">": "greater than",
                        ":": "colon",
                        '"': "double quote",
                        '/': "forward slash",
                        "\\": "backslash",
                        "|": "vertical bar",
                        "?": "question mark",
                        "*": "asteris"}


def replace_illegal_windows_char(string):
    for key, value in ILLEGAL_WINDOWS_CHAR.items():
        string = string.replace(key, " " + value + " ")  # pad the value to separate it from other words
    return string


def in_tts_folder(legal_text):
    for item in TTS_FOLDER_PATH.iterdir():
        if item.name == legal_text + ".mp3":
            return True
    return False


def get_mp3_path(text):
    """
    turn text to speech
    :param text: string
    :return: mp3 of the speech Path
    """
    # Searches if we already have the mp3
    # rename illegal characters
    legal_text = replace_illegal_windows_char(text)
    if not in_tts_folder(legal_text):
        tts = gtts.gTTS(legal_text)
        tts.save(str(TTS_FOLDER_PATH.joinpath(legal_text + ".mp3")))
    return TTS_FOLDER_PATH.joinpath(legal_text + ".mp3")

