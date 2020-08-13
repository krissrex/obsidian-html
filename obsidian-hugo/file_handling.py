import os
from format import format_internal_links, format_internal_aliased_links, format_internal_header_links, format_internal_header_links, format_tags
from utils import slug_case

def format_file(file_name, vault_root):
    with open(vault_root + "/" + file_name) as f:
        doc = f.read()

    doc = format_internal_links(
        format_internal_aliased_links(
            format_internal_header_links(
                format_tags(doc))))

    html = markdown2.markdown(doc, extras=["break-on-newline, fenced-code-blocks, header-ids, strike, tables"]

    with open(os.path.dirname(vault_root) + "/html/" + slug_case(file_name), "w") as f:
        f.write(html)

def find_files(vault_root, extra_folders):
    md_files = [f for f in os.listdir(vault_root) if f.endswith(".md")]
    for folder in extra_folders:
        md_files += [folder + "/" + f for f in os.listdir(vault_root + "/" + folder) if f.endswith(".md")]

    return md_files
