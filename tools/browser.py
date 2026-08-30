import webbrowser


def open_website(url):
    """
    Open a website in the default browser.
    """

    try:
        webbrowser.open(url)
        return True

    except Exception as e:
        print(f"Browser error: {e}")
        return False