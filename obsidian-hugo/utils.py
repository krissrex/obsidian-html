import re

def slug_case(text):
    text = text.replace(".", "dot")
    return re.sub(r'[\W_]+', '-', text)

def md_link(text, link):
    return "[" + text + "](" + link + ")"
