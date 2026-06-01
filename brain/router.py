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
    

    #TASK READ AND WRITE INTENTS
    TASK_CREATE_PHRASES = [
        "add task",
        "add a task",
        "create task",
        "create a task",
        "remind me to"
    ]

    TASK_READ_PHRASES = [
        "what are my tasks",
        "show my tasks",
        "list my tasks",
        "my tasks"
    ]

    for phrase in TASK_CREATE_PHRASES:

        if phrase in text:
            return "task_create"

    for phrase in TASK_READ_PHRASES:

        if phrase in text:
            return "task_read"
        
    if "applied to" in text:
        return "job_create"
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