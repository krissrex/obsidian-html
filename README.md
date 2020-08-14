# Obsidian to HTML converter

This is a short Python script to convert an [Obsidian](https://obsidian.md/) vault into a vault of HTML files, with the goal of publishing them as static files. It is heavily dependent on the excellent [markdown2](https://github.com/trentm/python-markdown2) by [trentm](https://github.com/trentm), but also deals with some parsing and file handling that makes it compatible with Obsidian's flavor of Markdown.

## Installation

Not available on PyPi yet, so for now you'll have to clone this repository and run:

  pip install .

inside it.

## Usage

This package is still under construction, so usage isn't very simple right now. If you want you can clone the repo and figure out how, but it might be a bit broken.

## To do

- [x] Generate backlinks
- [ ] Support HTML template (which will make adding CSS much easier)
- [ ] Support local attachments
- [ ] Support the `![[]]` embedding syntax (perhaps using iframe or some similar method)
- [ ] Upload to PyPi
- [ ] Write a GitHub Actions workflow to automate the process from vault to a publish GitHub Pages page
- [ ] Support extra features added by the user through YAML metadatYAML metadata

## Known issues

- Links in headers lead to weird header ids, and thus malfunctioning header links from other pages.
