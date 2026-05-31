from integrations.notion_client import add_task , get_tasks , notion
from dotenv import load_dotenv
import os

load_dotenv()
tasks = get_tasks()

print(len(tasks))
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
TASKS_DB_ID = os.getenv("TASKS_DB_ID")
# add_task(
#     "Apply for NVIDIA internship"
# )

# import os

# print(os.getcwd())

# print(notion.databases)
# print(dir(notion.databases))

# db = notion.databases.retrieve(
#     database_id=TASKS_DB_ID
# )

# print(db)