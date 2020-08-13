import os
import sys
from file_handling import format_file
from utils import find_files


def main(vault_root, out_dir, extra_folders=[]):
    # Ensure out_dir exists as well as its sub-folders.
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for folder in extra_folders:
        if not os.path.exists(out_dir + "/" + folder):
            os.makedirs(out_dir + "/" + folder)

    # Format each markdown-file.
    for md_file in find_files(vault_root, extra_folders):
        format_file(md_file, vault_root, out_dir)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], extra_folders=sys.argv[3:])
