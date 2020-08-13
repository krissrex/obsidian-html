import regex as re
from .utils import slug_case, md_link


def format_internal_links(document):
    """Links that are neither aliased, nor links to headers"""
    matches = re.finditer("\\[{2}([^|#]*?)\\]{2}", document)

    return obsidian_to_commonmark_links(document, matches, no_groups=1)


def format_internal_aliased_links(document):
    """Aliased links"""
    matches = re.finditer("\\[{2}([^|#\\]]*?)\\|(.*?)\\]{2}", document)

    return obsidian_to_commonmark_links(document, matches)


def format_internal_header_links(document):
    """Header links (TODO: Headers need to be slug case formatted, so this does not work right now)"""
    matches = re.finditer("\\[{2}([^|#\\]]*?)#(.*?)\\]{2}", document)

    return obsidian_to_commonmark_links(document, matches)


def format_tags(document):
    """Obsidian style tags. Removes #-icon and adds a span tag."""
    matches = re.finditer(r"#([\p{L}_]+)", document)

    for match in matches:
        document = document.replace(
            match.group(), "<span class=\"tag\">" + match.group(1) + "</span>")

    return document


def obsidian_to_commonmark_links(document, matches, no_groups=2):
    for match in matches:
        text = match.group(no_groups)
        link = slug_case(match.group(1))
        document = document.replace(match.group(), md_link(text, link))

    return document
