import json
import os


CHAT_MEMORY_FILE = "memory/memory.json"

USER_MEMORY_FILE = "memory/user_memory.json"



# CHAT MEMORY

def load_chat_memory():

    if not os.path.exists(CHAT_MEMORY_FILE):

        return []

    with open(CHAT_MEMORY_FILE, "r") as f:

        try:

            return json.load(f)

        except:

            return []


def save_chat_memory(conversation_history):

    with open(CHAT_MEMORY_FILE, "w") as f:

        json.dump(
            conversation_history,
            f,
            indent=4
        )



# USER MEMORY

def load_user_memory():

    if not os.path.exists(USER_MEMORY_FILE):

        return {}

    with open(USER_MEMORY_FILE, "r") as f:

        try:

            return json.load(f)

        except:

            return {}


def save_user_memory(user_memory):

    with open(USER_MEMORY_FILE, "w") as f:

        json.dump(
            user_memory,
            f,
            indent=4
        )


# GLOBALS
conversation_history = load_chat_memory()

user_memory = load_user_memory()