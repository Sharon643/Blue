from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
TASKS_DB_ID = os.getenv("TASKS_DB_ID")
TASKS_DATA_SOURCE_ID = os.getenv("TASKS_DATA_SOURCE_ID")

notion = Client(auth=NOTION_TOKEN)


def add_task(task_name):

    notion.pages.create(
        parent={
            "database_id": TASKS_DB_ID
        },
        properties={
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
    )

def get_tasks():

    response = notion.data_sources.query(
        data_source_id=TASKS_DATA_SOURCE_ID
    )
    return response["results"]