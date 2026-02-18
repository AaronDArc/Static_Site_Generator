This is a project that I am doing on Boot.Dev. By the time it is finished, I would be able to make a static site!

The details of the project would create a static generator as quoted

"Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
Open the file and read its contents.

Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).

Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
Raw markdown -> TextNode -> HTMLNode

Join all the HTMLNode blocks under one large parent HTMLNode for the pages.

Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.

Write the full HTML string to a file for that page in the /public directory."