import os
from utils import find_files, slug_case, find_backlinks, md_link
from format import htmlify


class Vault:
    def __init__(self, vault_root, extra_folders=[]):
        self.notes = find_files(vault_root, extra_folders, no_extension=True)
        self.extra_folders = extra_folders
        self._add_backlinks()

    def _add_backlinks(self):
        for note in self.notes:
            backlinks = find_backlinks(note["filename"], self.notes)
            if backlinks:
                note["content"] += "<div class=\"backlinks\" markdown=\"1\">\n## Backlinks\n\n"
                for backlink in backlinks:
                    note["content"] += f"- {md_link(backlink['text'], backlink['link'])}\n"
                note["content"] += "</div>"

    def convert_to_html(self):
        notes_html = []
        for note in self.notes:
            filename_html = slug_case(note["filename"]) + ".html"
            content_html = htmlify(note["content"])

            notes_html.append(
                {"filename": filename_html, "content": content_html})

        return notes_html

    def export_html(self, out_dir):
        # Ensure out_dir exists, as well as its sub-folders.
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        for folder in self.extra_folders:
            if not os.path.exists(out_dir + "/" + folder):
                os.makedirs(out_dir + "/" + folder)

        notes_html = self.convert_to_html()

        for note in notes_html:
            with open(os.path.join(out_dir, note["filename"]), "w") as f:
                f.write(note["content"])
