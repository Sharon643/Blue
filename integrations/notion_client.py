from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
TASKS_DB_ID = os.getenv("TASKS_DB_ID")
TASKS_DATA_SOURCE_ID = os.getenv("TASKS_DATA_SOURCE_ID")

notion = Client(auth=NOTION_TOKEN)


def add_task(
    task_name,
    priority=None,
    due_date=None
):

    properties = {
        "Task": {
            "title": [
                {
                    "text": {
                        "content": task_name
                    }
                }
            ]
        }
    }

    if priority:

        properties["Priority"] = {
            "select": {
                "name": priority
            }
        }

    if due_date:

        properties["Due date"] = {
            "date": {
                "start": due_date
            }
        }

    notion.pages.create(
        parent={
            "database_id": TASKS_DB_ID
        },
        properties=properties
    )

def get_tasks():

    response = notion.data_sources.query(
        data_source_id=TASKS_DATA_SOURCE_ID
    )
    return response["results"]