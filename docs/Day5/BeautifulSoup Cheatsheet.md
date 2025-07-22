BeautifulSoup Cheatsheet
BeautifulSoup is a Python library for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

1. Installation
If you don't have BeautifulSoup installed, you can install it using pip:

pip install beautifulsoup4
pip install lxml # Optional, but recommended for faster parsing

2. Basic Parsing
To get started, you need to import BeautifulSoup and provide it with the HTML/XML content.

from bs4 import BeautifulSoup

# Sample HTML content
html_doc = """
<html><head><title>My Document</title></head>
<body>
    <p class="title"><b>The Document Title</b></p>

    <a href="http://example.com/one" class="external-link" id="link1">Link One</a>
    <a href="http://example.com/two" class="external-link" id="link2">Link Two</a>
    <p>This is some other content.</p>
    <div class="container">
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </div>
</body>
</html>
"""

# Create a BeautifulSoup object
# 'lxml' is a common and fast parser; 'html.parser' is built-in
soup = BeautifulSoup(html_doc, 'lxml')

# Pretty-print the parsed HTML
print(soup.prettify())

3. Navigating the Parse Tree
BeautifulSoup allows you to navigate the parsed document using object-oriented access.

Accessing Tags
You can access tags directly as attributes of the BeautifulSoup object or other tags.

# Get the first <head> tag
head_tag = soup.head
print(f"Head Tag: {head_tag}")

# Get the first <title> tag within <head>
title_tag = soup.title
print(f"Title Tag: {title_tag}")

# Get the tag's name
print(f"Title Tag Name: {title_tag.name}")

# Get the string content of the tag
print(f"Title Tag Content: {title_tag.string}")

# Accessing attributes of a tag
link_one = soup.a
print(f"Link One href: {link_one['href']}")
print(f"Link One class: {link_one['class']}")

# Get all attributes as a dictionary
print(f"Link One attributes: {link_one.attrs}")

Navigating Down
.contents: A list of the tag's direct children.

.children: An iterator of the tag's direct children.

.descendants: An iterator of all children, grandchildren, etc.

body_tag = soup.body
print("\nBody Tag Contents:")
for child in body_tag.contents:
    if child.name: # Only print actual tags
        print(child.name)

print("\nBody Tag Descendants (Examples):")
for descendant in body_tag.descendants:
    if descendant.name:
        print(descendant.name, end=" ")
        if descendant.name == 'li': break # Stop after a few examples

Navigating Up
.parent: The direct parent of a tag.

.parents: An iterator of all ancestors.

# Find the parent of the title tag
p_tag = soup.p
print(f"\nParent of <p>: {p_tag.parent.name}")

# Iterate through parents of a specific link
link2 = soup.find(id="link2")
print(f"Parents of <a id='link2'>:")
for parent in link2.parents:
    if parent is None:
        continue
    if parent.name:
        print(parent.name)

Navigating Sideways
.next_sibling: The next sibling after the current tag.

.previous_sibling: The previous sibling before the current tag.

.next_siblings: An iterator of all following siblings.

.previous_siblings: An iterator of all preceding siblings.

first_p_tag = soup.p
print(f"\nNext sibling of first <p>: {first_p_tag.next_sibling.next_sibling.name}") # Skip newline
print(f"Previous sibling of first <p>: {first_p_tag.previous_sibling.previous_sibling.name}") # Skip newline

print("\nNext siblings of first <p> (examples):")
for sibling in first_p_tag.next_siblings:
    if sibling.name:
        print(sibling.name)

4. Searching the Tree (find() and find_all())
These are the most powerful methods for locating specific elements.

find_all(name, attrs, recursive, string, limit)
Finds all occurrences of a tag that match the criteria. Returns a list of tags.

name: Tag name (e.g., 'a', 'p'). Can be a string, list, regular expression, or function.

attrs: A dictionary of attribute values (e.g., {'class': 'external-link'}).

recursive: If False, only examines direct children. Default is True.

string: Searches for strings instead of tags.

limit: Stop searching after a certain number of matches.

# Find all <a> tags
all_links = soup.find_all('a')
print(f"\nAll links: {all_links}")

# Find all <p> tags with class 'title'
title_p = soup.find_all('p', class_='title') # 'class_' because 'class' is a Python keyword
print(f"Paragraphs with class 'title': {title_p}")

# Find all tags that have an 'id' attribute
tags_with_id = soup.find_all(id=True)
print(f"Tags with an 'id' attribute: {tags_with_id}")

# Find all <li> tags
list_items = soup.find_all('li')
for item in list_items:
    print(f"List Item: {item.string}")

# Find tags containing specific text (using 'string')
p_with_content = soup.find_all(string="This is some other content.")
print(f"Tags with specific string content: {p_with_content}")

find(name, attrs, recursive, string)
Similar to find_all(), but returns only the first match.

# Find the first <a> tag
first_link = soup.find('a')
print(f"\nFirst link found: {first_link}")

# Find the first <p> tag with class 'title'
first_title_p = soup.find('p', class_='title')
print(f"First paragraph with class 'title': {first_title_p}")

Common Search Patterns
# By tag name
print(f"\nFind all 'p' tags: {soup.find_all('p')}")

# By CSS class (note the underscore!)
print(f"Find all 'a' tags with class 'external-link': {soup.find_all('a', class_='external-link')}")

# By ID
print(f"Find tag with id 'link1': {soup.find(id='link1')}")

# By attribute value (any attribute)
print(f"Find all tags with href='http://example.com/one': {soup.find_all(href='http://example.com/one')}")

# Using a list of tag names
print(f"Find all 'p' or 'a' tags: {soup.find_all(['p', 'a'])}")

# Using regular expressions
import re
print(f"Find all tags whose name starts with 'b': {soup.find_all(re.compile("^b"))}") # e.g., <body>, <b>
print(f"Find all tags with 'link' in their ID: {soup.find_all(id=re.compile("link"))}")

5. Modifying the Tree
BeautifulSoup allows you to modify the parse tree.

# Sample HTML for modification
html_mod = """
<html>
<body>
    <p>Original text.</p>
    <div id="target">Content here</div>
</body>
</html>
"""
soup_mod = BeautifulSoup(html_mod, 'lxml')

# Change tag name
p_tag_mod = soup_mod.p
p_tag_mod.name = "div"
print(f"\nAfter changing p to div: {soup_mod.prettify()}")

# Modify tag attributes
div_tag_mod = soup_mod.find(id="target")
div_tag_mod['class'] = 'new-class'
div_tag_mod['data-type'] = 'example'
print(f"After modifying attributes: {soup_mod.prettify()}")

# Add new content
new_tag = soup_mod.new_tag("span")
new_tag.string = "Added span text."
div_tag_mod.append(new_tag) # Add inside the div
print(f"After appending a new tag: {soup_mod.prettify()}")

# Replace content
div_tag_mod.string = "New replaced content."
print(f"After replacing div content: {soup_mod.prettify()}")

# Remove content
span_to_remove = soup_mod.find('span')
if span_to_remove:
    span_to_remove.decompose() # Removes the tag and its contents
print(f"After removing span: {soup_mod.prettify()}")

6. CSS Selectors (select() and select_one())
BeautifulSoup also supports CSS selectors using the select() method (returns a list) and select_one() (returns the first match).

# Select all <p> tags
print(f"\nSelect all 'p' tags: {soup.select('p')}")

# Select tags by class
print(f"Select all elements with class 'external-link': {soup.select('.external-link')}")

# Select tag by ID
print(f"Select element with id 'link2': {soup.select('#link2')}")

# Select direct children
print(f"Select direct children <li> of .container: {soup.select('div.container > ul > li')}")

# Select descendants
print(f"Select all <li> descendants of .container: {soup.select('div.container li')}")

# Select combined selectors
print(f"Select 'p' or 'a' tags: {soup.select('p, a')}")

# Select tags with specific attribute values
print(f"Select 'a' tags with href starting with 'http://example.com': {soup.select('a[href^="http://example.com"]')}")

# Select the first matching element
print(f"Select first link: {soup.select_one('a')}")
