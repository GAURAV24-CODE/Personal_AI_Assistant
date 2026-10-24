def detect_intent(user_input):
    """
    Detect the basic intention behind the user's request.
    """

    text = user_input.lower().strip()


    # ==============================
    # OPEN WEBSITE / APP
    # ==============================

    open_commands = [
        "open ",
        "go to ",
        "launch ",
        "start "
    ]

    if any(text.startswith(command) for command in open_commands):
        return "open"


    # ==============================
    # YOUTUBE SEARCH / PLAY
    # ==============================

    youtube_commands = [
        "search youtube",
        "play ",
        "play music",
        "play song",
        "play lofi"
    ]

    if any(command in text for command in youtube_commands):
        return "youtube"


    # ==============================
    # GOOGLE / WEB SEARCH
    # ==============================

    if (
        text.startswith("search ")
        or text.startswith("search for ")
        or "search google" in text
        or "search the web" in text
    ):
        return "web_search"


    # ==============================
    # YOUTUBE
    # ==============================

    if "youtube" in text:
        return "youtube"


    # ==============================
    # REMINDERS
    # ==============================

    reminder_commands = [
        "remind me",
        "set a reminder",
        "reminder"
    ]

    if any(command in text for command in reminder_commands):
        return "reminder"


    # ==============================
    # STUDY / LEARNING
    # ==============================

    study_words = [
        "study",
        "learn",
        "teach me",
        "quiz me",
        "explain",
        "practice",
        "lesson"
    ]

    if any(word in text for word in study_words):
        return "study"


    # ==============================
    # NORMAL CONVERSATION
    # ==============================

    return "conversation"