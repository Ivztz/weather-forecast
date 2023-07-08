def final():
    """final project details"""
    text = open("README.md").read().lower().strip()
    print(len(text))

final()