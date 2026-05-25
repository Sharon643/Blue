import webbrowser
import datetime
import subprocess
import os

from voice.speak import speak


# APP REGISTRY

APPS = {

    "discord": r"C:\Users\sharo\AppData\Local\Discord\app-1.0.9238\Discord.exe",

    "notion": r"C:\Users\sharo\AppData\Local\Programs\Notion\Notion.exe",

    "vs code": r"C:\Users\sharo\AppData\Local\Programs\Microsoft VS Code\Code.exe",

}


# COMMAND 

def execute_command(user_text):

    user_text = user_text.lower()

    # OPEN APPS

    if "open" in user_text:

        for app_name, app_path in APPS.items():

            if app_name in user_text:

                try:

                    subprocess.Popen(app_path)

                    speak(f"Opening {app_name}")

                    return True

                except:

                    speak(f"I couldn't open {app_name}")

                    return True

    # YOUTUBE SEARCH

    youtube_keywords = [
        "youtube",
        "yt"
    ]

    search_keywords = [
        "search",
        "play",
        "find",
        "look up"
    ]

    if any(word in user_text for word in youtube_keywords):

        if any(word in user_text for word in search_keywords):

            query = user_text

            # REMOVE COMMAND WORDS
            for word in youtube_keywords:
                query = query.replace(word, "")

            for word in search_keywords:
                query = query.replace(word, "")

            query = query.replace("for", "")
            query = query.replace("on", "")
            query = query.replace("in", "")

            query = query.strip()

            url = (
                "https://www.youtube.com/results?search_query="
                + query
            )

            webbrowser.open(url)

            speak(f"Searching YouTube for {query}")

            return True

    # GOOGLE SEARCH

    google_keywords=["google"]
    
    if any(word in user_text for word in google_keywords):
        if any(word in user_text for word in search_keywords):

            query=user_text

            for word in google_keywords:
                query=query.replace(word,"")
            for word in search_keywords:
                query=query.replace(word,"")
            
            query=query.replace("on","")
            query=query.replace("for","")
            query=query.replace("in","")

            query=query.strip()

            url=(
                "https://www.google.com/search?q="
                +query
            )
            webbrowser.open(url)
            
            speak(f"Searching google for {query}")

            return True

    #DATE TIME

    if "what time" in user_text:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")
 
    elif "what date" in user_text:

        current_date = datetime.datetime.now().strftime("%B %d, %Y")

        speak(f"The date is {current_date}")
        

        return True

    return False