import requests
import json

from config.settings import OLLAMA_MODEL


def extract_memory(user_text):

    prompt = f"""
    You are a memory extraction system.

    Extract useful long-term user information.

    Return ONLY raw valid JSON.

    Do NOT store temporary actions, searches, or commands.
    Do NOT store search queries.
    Do NOT store recent activities.
    Only store stable long-term personal information.
    Do not explain.
    Do not use markdown.
    Do not write anything except JSON.

    If nothing important exists, return:
    {{}}

    Example:
    User: My favorite game is Valorant

    Output:
    {{"favorite_game":"Valorant"}}

    User message:
    {user_text}
    """

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            }
        )

        result = response.json()["response"].strip()
        # print("MEMORY RAW RESPONSE:", result)

        # REMOVE MARKDOWN
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        memory_data = json.loads(result)

        return memory_data

    except Exception as e:

        print("Memory Extraction Error:", e)

        return {}