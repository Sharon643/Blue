def extract_task(text):

    text = text.lower()

    prefixes = [
        "add task",
        "add a task",
        "create task",
        "create a task",
        "remind me to"
    ]

    for prefix in prefixes:

        if prefix in text:

            return text.replace(prefix, "").strip()

    return text