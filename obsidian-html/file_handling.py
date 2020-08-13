import os
import markdown2
from .format import format_internal_links, format_internal_aliased_links, format_internal_header_links, format_internal_header_links, format_tags
from .utils import slug_case


def format_file(file_name, vault_root, out_dir):
    with open(vault_root + "/" + file_name) as f:
        doc = f.read()

    # Formatting of Obsidian tags and links.
    doc = format_internal_links(
        format_internal_aliased_links(
            format_internal_header_links(
                format_tags(doc))))

    markdown2_extras = [
        # Parser should work withouth strict linebreaks.
        "break-on-newline",
        # Support of ```-codeblocks and syntax highlighting.
        "fenced-code-blocks",
        # Make slug IDs for each header. Needed for internal header links.
        "header-ids",
        # Support for strikethrough formatting.
        "strike",
        # GFM tables.
        "tables",
        # Support for lists that start without a newline directly above.
        "cuddled-lists"
    ]

    html = markdown2.markdown(doc, extras=markdown2_extras)

    # Make slug filename.
    html_file_name = slug_case(file_name.replace(".md", "")) + ".html"
    with open(out_dir + "/" + html_file_name, "w") as f:
        f.write(html)


def find_files(vault_root, extra_folders):
    # Find all markdown-files in vault root.
    md_files = [f for f in os.listdir(vault_root) if f.endswith(".md")]

    # Find all markdown-files in each extra folder.
    for folder in extra_folders:
        md_files += [folder + "/" + f for f in
                     os.listdir(vault_root + "/" + folder) if f.endswith(".md")]

    return md_files
