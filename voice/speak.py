import subprocess
import pygame
import uuid
import os

from config.settings import (
    PIPER_PATH,
    PIPER_MODEL,
    TEMP_FOLDER
)

pygame.mixer.init()


def speak(text):

    unique_id = uuid.uuid4().hex

    output_path = rf"{TEMP_FOLDER}\temp_{unique_id}.wav"

    text_file = rf"{TEMP_FOLDER}\temp_{unique_id}.txt"

    # WRITE TEXT
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(text)

    # PIPER COMMAND
    command = rf'"{PIPER_PATH}" --model "{PIPER_MODEL}" --output_file "{output_path}" < "{text_file}"'

    # GENERATE AUDIO
    subprocess.run(
        command,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # PLAY AUDIO
    pygame.mixer.music.stop()

    pygame.mixer.music.unload()

    pygame.mixer.music.load(output_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    # CLEANUP
    os.remove(output_path)
    os.remove(text_file)