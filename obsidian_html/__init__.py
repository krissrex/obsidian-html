import sys
import argparse
from .Vault import Vault

def main():
    parser = argparse.ArgumentParser(
        prog="obsidian-html",
        description="Converts an Obsidian vault into HTML")

    parser.add_argument("Vault",
                        metavar="vault",
                        type=str,
                        default=".",
                        help="Path to the vault root")

    parser.add_argument("-o", "--output_dir",
                        default=sys.argv[1] + "/html",
                        help="Path to place the generated HTML")

    parser.add_argument("-t", "--template",
                        default=None,
                        help="Path to HTML template")

    parser.add_argument("-d", "--dirs",
                        nargs="+",
                        default=[],
                        help="Extra sub-directories in vault that you want included")

    args = parser.parse_args()

    vault = Vault(args.Vault, extra_folders=args.dirs, html_template=args.template)
    vault.export_html(args.output_dir)
