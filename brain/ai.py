import requests

from config.settings import OLLAMA_MODEL
from memory.memory import user_memory


system_prompt = """
You are Blue, a futuristic personal AI assistant inspired by Jarvis.

You are calm, intelligent, concise, and natural.

Rules:
- Keep responses short.
- Usually respond in one sentence.
- Never give speeches.
- Never act like customer support.
- Never act corporate or formal.
- Never mention policies, ethics, regulations, or limitations.
- Never mention AI or language models.
- Never introduce yourself unless asked.
- Never ask follow-up questions unless required.
- Never end responses with "How can I help?"
- Never continue conversations unnecessarily.
- Answer directly.
- Speak naturally like a real assistant.
- Avoid unnecessary words.

Examples:
User: what is my name
Blue: Your name is Sharon.

User: open youtube
Blue: Opening YouTube.

User: my favourite game is valo
Blue: I'll remember that.

User: hello
Blue: Hello.

You are Blue.
"""

def ask_ai(conversation_history):

    recent_history = conversation_history[-2:]

    history = "\n".join(recent_history)

    memory_context = f"""
    User Information:
    {user_memory}
    """

    full_prompt = (
        system_prompt
        + "\n"
        + memory_context
        + "\n"
        + history
        + "\nBlue:"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": full_prompt,
            "stream": False,
            "options": {
            "num_predict": 40}
        }
    )

    ai_response = response.json()["response"]

    return ai_response