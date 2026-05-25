import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:


        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300

        audio = recognizer.listen(source)

        try:

            text = recognizer.recognize_google(audio)

            return text

        except:

            return ""