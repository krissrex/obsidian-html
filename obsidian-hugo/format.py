import re

def format_internal_links(document):
    """Links that are neither aliased, nor link to headers"""
    return re.sub("\\[{2}([^|#]*?)\\]{2}", "[\\1]({{ ref \"\\1.md\" }})", document)

def format_internal_aliased_links(document):
    """Aliased links"""
    return re.sub("\\[{2}([^|#\\]]*?)\\|(.*?)\\]{2}", "[\\2]({{ ref \"\\1.md\" }})", document)

def format_internal_header_links(document):
    """Header links (TODO: Headers need to be slug case formatted, so this does not work right now)"""
    return re.sub("\\[{2}([^|#\\]]*?)#(.*?)\\]{2}", "[\\2]({{ ref \"\\1.md#\\2\" }})", document)

with open("/home/kmaasrud/Brain/Obsidian and GitHub Pages workflow.md") as f:
    doc = f.read()

doc = format_internal_links(doc)
doc = format_internal_aliased_links(doc)

with open("/home/kmaasrud/Brain/Obsidian and GitHub Pages workflow 2.md", "w") as f:
    f.write(doc)
