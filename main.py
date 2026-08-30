import json
from pathlib import Path

from ollama import chat
from core.router import detect_intent


# ==============================
# MEMORY
# ==============================

memory_file = Path("memory.json")


def load_memory():
    if memory_file.exists():
        return json.loads(memory_file.read_text(encoding="utf-8"))

    return {
        "name": "Gaurav",
        "goal": "Get placed in a good company",
        "tcs_day": 3
    }


memory = load_memory()


# ==============================
# JARVIS PERSONALITY
# ==============================

instructions = f"""
You are Jarvis, Gaurav's friendly personal AI assistant.

You are NOT only a study assistant.

You can help Gaurav with:

- General conversation
- Studying and learning
- Python and programming
- SQL and data analytics
- AI and machine learning
- Career preparation
- Projects
- Productivity
- Planning
- General questions
- Web research
- YouTube
- PC tasks

PERSONALITY:

- Friendly
- Helpful
- Natural
- Supportive
- Intelligent
- Practical
- Talk like a helpful friend
- Do not sound robotic
- Keep normal replies reasonably short

IMPORTANT:

Never claim that you performed an action unless the application
actually performed that action.

Gaurav's information:

Name: {memory['name']}
Goal: {memory['goal']}
Current TCS NQT day: {memory['tcs_day']}
"""


# ==============================
# CONVERSATION MEMORY
# ==============================

messages = [
    {
        "role": "system",
        "content": instructions
    }
]


# ==============================
# START JARVIS
# ==============================

print(
    f"Jarvis: Hello {memory['name']}. "
    "I am ready to help with anything."
)

print("Jarvis: Type 'bye' when you want to stop.")


# ==============================
# MAIN CHAT LOOP
# ==============================

while True:

    message = input("\nYou: ").strip()

    # Ignore empty input
    if not message:
        continue

    # Exit
    if message.lower() == "bye":
        print(
            "Jarvis: Goodbye, Gaurav. "
            "Keep working toward your goals!"
        )
        break

    # ==============================
    # DETECT USER INTENT
    # ==============================

    intent = detect_intent(message)

    print(f"[Intent: {intent}]")


    # ==============================
    # ADD USER MESSAGE
    # ==============================

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )


    # ==============================
    # SEND TO OLLAMA
    # ==============================

    try:

        response = chat(
            model="gemma3:1b",
            messages=messages
        )

        reply = response.message.content

    except Exception as e:

        reply = (
            "Sorry Gaurav, I couldn't process that request. "
            f"Error: {e}"
        )


    # ==============================
    # DISPLAY RESPONSE
    # ==============================

    print(f"\nJarvis: {reply}")


    # ==============================
    # SAVE ASSISTANT RESPONSE
    # ==============================

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )