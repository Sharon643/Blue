from integrations.notion_client import add_task, get_tasks

def create_task(task_data):

    add_task(
        task_data["task"],
        task_data["priority"],
        task_data["due_date"]
    )

    return (
        f"Task added: "
        f"{task_data['task']}"
    )

def read_tasks():

    tasks = get_tasks()

    # print(tasks)
        

    if not tasks:
        return "You have no tasks."

    task_names = []

    for task in tasks[:5]:

        try:
            title = task["properties"]["Task"]["title"]

            if title:
                task_names.append(
                    title[0]["plain_text"]
                )

        except Exception:
            pass

    if not task_names:
        return "You have no tasks."

    return (
        "Your tasks are: "
        + ", ".join(task_names)
    )