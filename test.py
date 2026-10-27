from core.router import detect_intent


tests = [
    "Hello Jarvis",
    "Open YouTube",
    "Search Python loops",
    "Play lo-fi music",
    "Teach  Python",
    "Remind me t study at 7 PM"
]


for text in tests:
    intent = detect_intent(text)

    print(f"User   : {text}")
    print(f"Intent : {intent}")
    print("-" * 40)