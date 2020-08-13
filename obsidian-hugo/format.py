import re
from utils import slug_case, md_link

def format_internal_links(document):
    """Links that are neither aliased, nor links to headers"""
    matches = re.finditer("\\[{2}([^|#]*?)\\]{2}", document)

    return obsidian_to_commonmark_link(document, matches, no_groups = 1)

def format_internal_aliased_links(document):
    """Aliased links"""
    matches = re.finditer("\\[{2}([^|#\\]]*?)\\|(.*?)\\]{2}", document)

    return obsidian_to_commonmark_link(document, matches)

def format_internal_header_links(document):
    """Header links (TODO: Headers need to be slug case formatted, so this does not work right now)"""
    matches = re.finditer("\\[{2}([^|#\\]]*?)#(.*?)\\]{2}", document)

    return obsidian_to_commonmark_link(document, matches)

def obsidian_to_commonmark_link(document, matches, no_groups = 2):
    for match in matches:
        text = match.group(no_groups)
        link = slug_case(match.group(1))
        document = document.replace(match.group(), md_link(text, link))

    return document
