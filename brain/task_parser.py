from datetime import date, timedelta


def parse_task(text):

    result = {
        "task": "",
        "priority": None,
        "due_date": None
    }

    cleaned = text.lower().strip()

    # ---------- Priority ----------

    if "high priority" in cleaned:
        result["priority"] = "High"
        cleaned = cleaned.replace(
            "high priority", ""
        )

    elif "medium priority" in cleaned:
        result["priority"] = "Medium"
        cleaned = cleaned.replace(
            "medium priority", ""
        )

    elif "low priority" in cleaned:
        result["priority"] = "Low"
        cleaned = cleaned.replace(
            "low priority", ""
        )

    # ---------- Due Dates ----------

    if "tomorrow" in cleaned:

        result["due_date"] = (
            date.today() +
            timedelta(days=1)
        ).isoformat()

        cleaned = cleaned.replace(
            "tomorrow", ""
        )

    elif "today" in cleaned:

        result["due_date"] = (
            date.today()
        ).isoformat()

        cleaned = cleaned.replace(
            "today", ""
        )

    elif "next week" in cleaned:

        result["due_date"] = (
            date.today() +
            timedelta(days=7)
        ).isoformat()

        cleaned = cleaned.replace(
            "next week", ""
        )

    # ---------- Command Prefixes ----------

    prefixes = [
        "add a task to",
        "create a task to",
        "add task to",
        "create task to",
        "remind me to",
        "add a task",
        "create a task",
        "add task",
        "create task"
    ]

    for prefix in prefixes:

        if cleaned.startswith(prefix):

            cleaned = cleaned[
                len(prefix):
            ].strip()

            break

    result["task"] = cleaned

    return result