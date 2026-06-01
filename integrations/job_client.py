from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
JOBS_DB_ID = os.getenv("JOBS_DB_ID")
JOBS_DATASOURCE_ID = os.getenv("JOBS_DATSOURCE_ID")

notion = Client(auth=NOTION_TOKEN)

def add_job_application(
    company,
    role,
    status="Applied"
):

    notion.pages.create(
        parent={
            "database_id": JOBS_DB_ID
        },
        properties={
            "Company": {
                "title": [
                    {
                        "text": {
                            "content": company
                        }
                    }
                ]
            },

            "Role": {
                "rich_text": [
                    {
                        "text": {
                            "content": role
                        }
                    }
                ]
            },

            "Status": {
                "select": {
                    "name": status
                }
            }
        }
    )