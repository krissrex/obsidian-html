from utils import find_files, slug_case, find_backlinks
from format import htmlify


class Vault:
    def __init__(self, vault_root, extra_folders=[]):
        self.notes = find_files(vault_root, extra_folders)
        print(find_backlinks("Version control system", self.notes))

    def convert_to_html(self):
        notes_html = []
        for filename, content in self.notes.items():
            filename_html = slug_case(filename.replace(".md", "")) + ".html"
            content_html = htmlify(content)

            notes_html.append(
                {"filename": filename_html, "content": content_html})

        return notes_html
