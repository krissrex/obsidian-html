import re

def format_internal_links(document):
    """Formats Obsidian internal links"""
    # Links that are neither aliased, nor link to headers
    out = re.sub("\\[{2}([^|#]*?)\\]{2}", "[\\1](\"\\1.md\")", document)
    # Aliased links
    out = re.sub("\\[{2}([^|#\\]]*?)\\|(.*?)\\]{2}", "[\\2](\"\\1.md\")", out)
    # Header links (TODO: Headers need to be slug case formatted, so this does not work right now)
    out = re.sub("\\[{2}([^|#\\]]*?)#(.*?)\\]{2}", "[\\2](\"\\1.md#\\2\")", out)

    return out

doc = """[[rclone]] is easily installed on [[Arch Linux]] via [[Arch pacman|pacman]]:

	sudo pacman -S rclone
	
1. Use `rclone config` and follow the steps as wished

	- Most defaults are fine
	- There's no need for a `client-id` or a `client-secret`

2. The mount needs to be opened at startup. The command is:
		
		rclone --vfs-cache-mode writes mount "<name of config>":  ~/OneDrive
		
[[Some link|some alias]] and some more text, and whhoops, here is a [[some link#header link]], and another [[link|alias]]."""

print(format_internal_links(doc))
