from obsidian_html import Vault

vault = Vault("/home/kmaasrud/Brain/vault",
              extra_folders=["daily"], html_template="./template.html")

vault.export_html("/home/kmaasrud/Brain/html")
