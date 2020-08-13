import regex
from utils import find_files, md_link, slug_case


def extract_links_from_file(document):
    matches = regex.finditer(r"\[{2}([^\]]*?)[|#\]]([^\]]*?)\]+", document)

    links = []
    for match in matches:
        text = match.group(2) if match.group(2) else match.group(1)
        link = slug_case(match.group(1))
        links.append({"text": text, "link": link})

    return links


def find_backlinks(md_file, vault_root, extra_folders):
    pass


def add_backlinks(document):
    pass
