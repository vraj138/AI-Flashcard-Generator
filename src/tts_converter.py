from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    """
    Convert text to speech and save as an MP3 file.
    """
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        print(f"Saved speech to {filename}")
        # Optional: play sound (macOS/Linux)
        os.system(f"afplay {filename}" if os.name == "posix" else f"start {filename}")
    except Exception as e:
        print(f"Error in TTS: {e}")