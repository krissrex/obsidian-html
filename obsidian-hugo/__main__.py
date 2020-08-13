import os
import sys
from .format import *

def main(vault_root, extra_folders = []):
    parent_of_vault = os.path.dirname(vault_root)
    if not os.path.exists(parent_of_vault + "/hugo"):
        os.makedirs(parent_of_vault + "/hugo")
        os.makedirs(parent_of_vault + "/hugo/content")
    for folder in extra_folders:
        if not os.path.exists(parent_of_vault + "/hugo/content/" + folder):
            os.makedirs(parent_of_vault + "/hugo/content/" + folder)

    for md_file in find_files(vault_root, extra_folders):
        format_file(md_file, vault_root)

if __name__ == "__main__":
    main(sys.argv[1], extra_folders = sys.argv[2:])
