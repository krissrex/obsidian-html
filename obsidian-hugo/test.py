import markdown

md = "# This is a header\n\nAnd [this](link-destination) is a link"

html = markdown.markdown(md)

print(html)
