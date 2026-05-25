def detect_intent(user_text):

    text = user_text.lower()

    # COMMAND INTENTS

    command_keywords = [
        "open ",
        "search ",
        "play ",
        "find ",
        "youtube ",
        "google ",
        "launch "
    ]

    if any(word in text for word in command_keywords):

        return "command"

    # MEMORY INTENTS


    memory_keywords = [
        "i like",
        "i love",
        "my favourite",
        "my favorite",
        "i am",
        "i study",
        "i work",
        "my name"
        ]

    if any(phrase in text for phrase in memory_keywords):

        return "memory"

    # DEFAULT


    return "conversation"