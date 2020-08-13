import re

def slug_case(text):
    text = text.replace(".", "dot")
    text = text.replace("_", "-")
    return re.sub(r'[^\w\-/]+', '-', text)

def md_link(text, link):
    return "[" + text + "](" + link + ")"
