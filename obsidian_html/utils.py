import regex as re
import os


def slug_case(text):
    text = text.replace(".", "dot")
    text = text.replace("_", "-")
    return re.sub(r'[^\w\-/]+', '-', text)


def md_link(text, link):
    return "[" + text + "](" + link + ")"


def find_files(vault_root, extra_folders, no_extension=False):
    # Find all markdown-files in vault root.
    md_files = find_md_files(vault_root, no_extension)

    # Find all markdown-files in each extra folder.
    for folder in extra_folders:
        md_files += find_md_files(os.path.join(vault_root, folder),
                                  no_extension)

    return md_files


def find_md_files(root, no_extension):
    md_files = []
    for md_file in os.listdir(root):
        if not md_file.endswith(".md"):
            continue

        with open(os.path.join(root, md_file)) as f:
            content = f.read()

        if no_extension:
            md_file = md_file.replace(".md", "")

        md_files.append({"filename": md_file, "content": content})

    return md_files


def extract_links_from_file(document):
    matches = re.finditer(r"\[{2}([^\]]*?)[|#\]]([^\]]*?)\]+", document)

    links = []
    for match in matches:
        link = match.group(1)
        links.append(link)

    return links


def find_backlinks(target_note_name, all_notes):
    backlinks = []
    for note in all_notes:
        links = extract_links_from_file(note["content"])
        if target_note_name in links:
            backlinks.append({"text": note["filename"].replace(".md", ""),
                              "link": slug_case(note["filename"].replace(".md", ""))})

    return backlinks
