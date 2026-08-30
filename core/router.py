def detect_intent(user_input):
    """
    Detect the basic intention behind the user's request.
    """

    text = user_input.lower().strip()

    # Open websites/apps
    if text.startswith("open "):
        return "open"

    # YouTube requests
    if "youtube" in text:
        return "youtube"

    if "play" in text and any(word in text for word in [
        "music",
        "song",
        "lofi",
        "lo-fi"
    ]):
        return "youtube"

    # Web searches
    if text.startswith("search ") or "search for" in text:
        return "web_search"

    # Reminders
    if "remind me" in text or "set a reminder" in text:
        return "reminder"

    # Study / learning
    study_words = [
        "study",
        "learn",
        "teach me",
        "quiz me",
        "explain"
    ]

    if any(word in text for word in study_words):
        return "study"

    # Everything else is normal conversation
    return "conversation"