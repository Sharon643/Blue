def detect_intent(user_text):

    text = user_text.lower()

    MEMORY_WRITE_PHRASES = [
    "my name is",
    "i am from",
    "i'm from",
    "i like",
    "i love",
    "my favorite",
    "my favourite",
    "i study",
    "i work as"
    ]

    for phrase in MEMORY_WRITE_PHRASES:

        if phrase in user_text.lower():

            return "memory_write"
    

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
    
    TASK_PHRASES = [
    "add task",
    "create task",
    "add a task",
    "create a task",
    "remind me to"
    ]

    for phrase in TASK_PHRASES:
        if phrase in user_text.lower():
            return "task"

    # MEMORY INTENTS


    memory_keywords = [
        "i like",
        "i love",
        "my favourite",
        "my favorite is",
        "i am",
        "i study",
        "i work",
        "my name is"
        ]

    if any(phrase in text for phrase in memory_keywords):

        return "memory"

    # DEFAULT


    return "conversation"