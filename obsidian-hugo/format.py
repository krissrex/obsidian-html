import re

def slug_case(text):
    text = text.replace(".", "dot")
    return re.sub(r'[\W_]+', '-', text)

def format_internal_links(document):
    """Links that are neither aliased, nor link to headers"""
    return re.sub("\\[{2}([^|#]*?)\\]{2}", "[\\1]({{ ref \"\\1.md\" }})", document)

def format_internal_aliased_links(document):
    """Aliased links"""
    return re.sub("\\[{2}([^|#\\]]*?)\\|(.*?)\\]{2}", "[\\2]({{ ref \"\\1.md\" }})", document)

def format_internal_header_links(document):
    """Header links (TODO: Headers need to be slug case formatted, so this does not work right now)"""
    matches = re.finditer("\\[{2}([^|#\\]]*?)#(.*?)\\]{2}", document)

    for match in matches:
        link_text = match.group(2)
        link = match.group(1) + ".md#" + slug_case(match.group(2))
        full_link = "[" + link_text + "]({{< ref \"" + link + "\" >}})"
        document = document.replace(match.group(), full_link)

    return document

with open("/home/kmaasrud/Brain/Just a test.md") as f:
    doc = f.read()

doc = format_internal_links(
    format_internal_aliased_links(
        format_internal_header_links(doc)))

print(doc)
