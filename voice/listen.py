from faster_whisper import WhisperModel

import speech_recognition as sr

import tempfile

# LOAD MODEL
model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)

recognizer = sr.Recognizer()


# LISTEN

def listen():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.pause_threshold = 0.5

        recognizer.energy_threshold = 300

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=3
        )

        # SAVE TEMP AUDIO
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            temp_audio.write(
                audio.get_wav_data()
            )

            temp_path = temp_audio.name

        # WHISPER TRANSCRIPTION
        segments, _ = model.transcribe(
            temp_path
        )

        text = ""

        for segment in segments:

            text += segment.text

        text = text.strip()

        return text