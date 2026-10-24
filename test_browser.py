from tools.browser import open_website


print("Testing browser tool...")

success = open_website("https://www.youtube.com")

if success:
    print("Browser tool: SUCCSS")
else:
    print("Browser tool: FAILED")
