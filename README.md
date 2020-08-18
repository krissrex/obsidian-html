# Obsidian to HTML converter

This is a short Python script to convert an [Obsidian](https://obsidian.md/) vault into a vault of HTML files, with the goal of publishing them as static files. It is heavily dependent on the excellent [markdown2](https://github.com/trentm/python-markdown2) by [trentm](https://github.com/trentm), but also deals with some parsing and file handling that makes it compatible with Obsidian's flavor of Markdown.

## Installation

Not available on PyPi yet, so for now you'll have to clone this repository and run:

    pip install .

inside it.

## Usage

This package is still under construction, so usage isn't very simple right now. If you want you can clone the repo and figure out how, but it might be a bit broken.

## Deploying vault with GitHub Actions

Make a GitHub Actions workflow using the YAML below, and your vault will be published to GitHub Pages every time you push to the repository.

1. Make sure you have GitHub Pages set up in the vault, and that it has `gh-pages` `/root` as its source.
2. Modify the following YAML job to match your repository.

    ```yaml
    name: Deploy to GitHub Pages

    on:
      push:
        branches: [ master ]
      
    jobs:
      deploy:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2

        - name: Set up Python 3.8
          uses: actions/setup-python@v2
          with:
            python-version: 3.8

        - name: Install obsidian-html
          run: |
            python -m pip install --upgrade pip
            pip install git+https://github.com/kmaasrud/obsidian-html.git
            
        - name: Generate HTML through obsidian-html
          run: python -m obsidian_html <path to vault> -o ./html

        - name: Deploy
          uses: s0/git-publish-subdir-action@develop
          env:
            REPO: self
            BRANCH: gh-pages
            FOLDER: html
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    ```

## To do

- [x] Generate backlinks
- [x] Support HTML template (which will make adding CSS much easier)
- [ ] Support local attachments
- [ ] Support the `![[]]` embedding syntax (perhaps using iframe or some similar method)
- [ ] Upload to PyPi
- [x] Write a GitHub Actions workflow to automate the process from vault to a publish GitHub Pages page
- [ ] Support extra features added by the user through YAML metadata

## Known issues

- Links in headers lead to weird header ids, and thus malfunctioning header links from other pages.
