import os
import sys
from format import *

def format_file(file_name, vault_root):
    with open(vault_root + "/" + file_name) as f:
        doc = f.read()

    new_doc = format_internal_links(
        format_internal_aliased_links(
            format_internal_header_links(doc)))

    new_doc = f"+++\ntitle = \"{file_name.replace('.md', '')}\"\n+++\n\n" + new_doc

    with open(vault_root + "/hugo/content/" + file_name, "w") as f:
        f.write(new_doc)

def find_files(vault_root, extra_folders):
    md_files = [f for f in os.listdir(vault_root) if f.endswith(".md")]
    for folder in extra_folders:
        md_files += [folder + "/" + f for f in os.listdir(vault_root + "/" + folder) if f.endswith(".md")]

    return md_files

def main(vault_root, extra_folders = []):
    if not os.path.exists(vault_root + "/hugo/content"):
        os.makedirs(vault_root + "/hugo/content")
    for folder in extra_folders:
        if not os.path.exists(vault_root + "/hugo/content/" + folder):
            os.makedirs(vault_root + "/hugo/content/" + folder)

    for md_file in find_files(vault_root, extra_folders):
        format_file(md_file, vault_root)

if __name__ == "__main__":
    main(sys.argv[1], extra_folders = sys.argv[2:])
