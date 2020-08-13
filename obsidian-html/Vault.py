from .utils import find_files


class Vault:
    def __init__(self, vault_root, extra_folders=[]):
        self.notes = find_files(vault_root, extra_folders)
