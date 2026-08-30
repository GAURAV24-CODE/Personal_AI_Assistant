
import json
from pathlib import Path

from ollama import chat

memory_file = Path("memory.json")


def load_memory():
    if memory_file.exists():
        return json.loads(memory_file.read_text())

    return {
        "name": "Gaurav",
        "goal": "Get placed in a good company",
        "tcs_day": 3
    }


memory = load_memory()

instructions = f"""
You are Jarvis, Gaurav's friendly personal AI assistant.

Speak naturally, warmly, and clearly.
Help Gaurav with studying, planning work, motivation, and general questions.
Keep replies practical and not too long.

Gaurav's information:
Name: {memory['name']}
Goal: {memory['goal']}
Current TCS NQT day: {memory['tcs_day']}
"""

messages = [
    {"role": "system", "content": instructions}
]

print(f"Jarvis: Hello {memory['name']}. I am ready to talk.")
print("Jarvis: Type 'bye' when you want to stop.")

while True:
    message = input("\nYou: ").strip()

    if message.lower() == "bye":
        print("Jarvis: Goodbye, Gaurav. Keep working toward your goals!")
        break

    messages.append({"role": "user", "content": message})

    response = chat(
        model="gemma3:1b",
        messages=messages
    )

    reply = response.message.content
    print(f"\nJarvis: {reply}")

    messages.append({"role": "assistant", "content": reply})