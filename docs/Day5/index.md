---
title: Day 5 Web Scraping with Beautiful Soup & Selenium
layout: default
nav_order: 6
has_children: false
nav_exclude: false
---

# Day 5. Web Scraping. 🕷️ Beautiful Soup & Selenium 
{: .no_toc }

Welcome to Day 5! Today, you’ll learn how to extract data from websites using Python. We’ll start with Beautiful Soup for static pages, then level up to Selenium for dynamic, interactive sites. By the end, you’ll be able to collect data from the web for your own projects!

---

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 🌱 What is Web Scraping?
Web scraping is the process of automatically collecting information from websites. It’s useful for gathering data that isn’t available via an API.

- **Beautiful Soup**: Parses HTML and XML documents. Great for static pages.
- **Selenium**: Automates browsers. Useful for dynamic sites that require interaction (clicks, typing, etc).

---

## 🥣 Beautiful Soup Basics <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
For parsing and navigating HTML/XML with Python
Requires: beautifulsoup4 and a parser like lxml or Python's built-in html.parser.

### 🧩 What can you do with Beautiful soup?
Here's a breakdown of its core capabilities:

* **Parse HTML and XML:** Beautiful Soup takes raw HTML or XML content and transforms it into a navigable "parse tree" made of Python objects. This tree makes it simple to access and manipulate specific parts of the document.

* **Navigate the Parse Tree:** You can easily move through the HTML/XML structure:
    * **By tag name:** Find elements like `<div>`, `<a>`, or `<p>`.
    * **By attributes:** Locate elements based on their `id`, `class`, `href`, or any other attribute.
    * **By text content:** Search for specific words or phrases within elements.
    * **Using relationships:** Travel up (parent), down (children, descendants), or sideways (siblings) in the tree.

* **Search for Specific Elements:** Beautiful Soup offers strong methods like `find()` (to get the first match) and `find_all()` (to get all matches) to pinpoint the exact data you're looking for. You can combine these with various filters (tag names, attributes, CSS selectors, regular expressions, or even custom functions) for precise selection.

* **Extract Data:** Once you've found the elements you want, you can easily pull out:
    * **Text content:** Get the visible text inside a tag (e.g., `soup.title.string`).
    * **Attribute values:** Access the values of attributes like `href` from an `<a>` tag or `src` from an `<img>` tag.

* **Handle Malformed HTML:** One of Beautiful Soup's strengths is its ability to deal with "tag soup"—poorly structured or incomplete HTML. It tries to make sense of it and build a usable parse tree.

* **Integrate with Other Libraries:**
    * **Requests:** Often used with the `requests` library to fetch the HTML content from a URL before Beautiful Soup parses it.
    * **Selenium:** For dynamic websites that rely heavily on JavaScript for rendering, you might use Selenium (a browser automation tool) to load the page, and then pass the rendered HTML to Beautiful Soup for parsing.
    * **Pandas:** Extracted data can be easily structured and stored in Pandas DataFrames for further analysis or export to formats like CSV or Excel.

---

### 🧰 Common Uses for Beautiful Soup

Beautiful Soup is primarily used for:

* **Web Scraping:** This is its main purpose. You can use it to:
    * Collect product information (names, prices, descriptions) from e-commerce sites.
    * Extract news articles, blog posts, or research papers.
    * Gather job listings or real estate data.
    * Perform sentiment analysis by scraping reviews or comments.
* **Data Mining:** Turning unstructured web data into organized datasets for analysis.
* **Content Aggregation:** Building tools that pull content from multiple online sources into one centralized location.

In short, Beautiful Soup empowers Python developers to programmatically interact with web content, making it an essential tool for anyone looking to extract and work with data from the internet.

### 📦 Install the required packages
```bash
pip install beautifulsoup4 requests lxml
```

### 📄 Example: Scraping a Local HTML File
Suppose you have a file called `website.html`:

```python
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
```

### 🧼 Cleaning HTML
```python
clean_text = soup.get_text(strip=True)
```

### 🔍 Finding Elements
You can search for tags, classes, ids, and more:

```python
# Find the first <a> tag
anchor = soup.find("a")
print(anchor)

# Find all <a> tags
all_anchors = soup.find_all("a")
for tag in all_anchors:
    # .getText() gets the visible text inside the tag
    print(tag.getText())
    # .get() retrieves the value of an attribute (e.g., href)
    print(tag.get("href"))
```

#### Search by attributes (id, class, etc.)
```python
# Find by id
heading = soup.find(name="h1", id="name")

# Find by class (note: use class_ because 'class' is a reserved word)
section = soup.find(name="h3", class_="heading")

# Find all elements with a specific class
items = soup.find_all(class_="item")
```

#### Search using CSS selectors
```python
# Use .select() for CSS selectors
links = soup.select("a.storylink")  # All <a> tags with class 'storylink'
ids = soup.select("#main")          # Element with id 'main'
classes = soup.select(".heading")   # All elements with class 'heading'
```

### 🌳 Navigating the Tree
```python
tag.name         # Tag name
tag.attrs        # Tag attributes as dict
tag['href']      # Specific attribute

tag.text         # All text inside tag (recursive)
tag.string       # Direct string only
tag.parent
tag.children      # Generator of children
tag.contents      # List of children
tag.next_sibling
tag.previous_sibling

```


### 🔗 Navigating and Following Links
You can extract and follow links by combining `.get("href")` with requests:

```python
for tag in soup.find_all("a"):
    link = tag.get("href")
    if link and link.startswith("http"):
        print("Following:", link)
        # You can fetch the linked page with requests.get(link)
```

For further reference follow to the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">documentation</a>


---

## 🌐 Scraping Live Websites <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

To scrape a live website, use the `requests` library to fetch the page:

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Get all article titles
titles = soup.find_all("a", class_="storylink")
for title in titles:
    print(title.getText())
```

---

## ⚖️ Is Web Scraping Legal? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Only scrape public data.
- Respect robots.txt and website terms.
- Don’t overload servers (add delays if scraping many pages).
- Use scraped data responsibly.

---

## 🤖 Selenium for Dynamic Websites <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Some sites load content with JavaScript or require interaction. Selenium lets you control a real browser to handle these cases. 

Unlike Beautiful Soup, which is limited to scraping data, Selenium allows for interaction with web pages, such as typing, clicking, and scrolling.  It enables the automation of continuous actions and entire workflows of a particular job or task.  It effectively drives a browser to perform actions like a human user. 

Selenium can automate almost anything a human can do on a website, like filling forms, transferring information, or playing web-based games.

### 🚗 Introduction to Selenium WebDriver

* **What it is:** Selenium WebDriver is a well-known automation and testing tool for web developers.
* **Why use it (over Beautiful Soup):** Unlike Beautiful Soup, which is limited to scraping data, Selenium allows for interaction with web pages, such as typing, clicking, and scrolling. It enables the automation of continuous actions and entire workflows of a particular job or task. It effectively drives a browser to perform actions like a human user.
* **Capabilities:** Selenium can automate almost anything a human can do on a website, like filling forms, transferring information, or playing web-based games.

### 🔧 Installation and Setup of Selenium

1.  **Install Chrome Browser:** While Selenium works with other browsers like Firefox or Safari, Chrome is recommended for consistency and use of Chrome Developer Tools. Download the Chrome driver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) and place it in your PATH.
2.  **Install Selenium Package:**
    * Import `selenium` in your Python file (e.g., `main.py`).
    * Install the package using the provided light bulb option in your IDE.
```bash
pip install selenium
```
3.  **Import WebDriver Module:** Change the import statement to `from selenium import webdriver`.
4.  **Create a Driver Instance:** Initialize a Chrome driver object: `driver = webdriver.Chrome()`.
    * **Chromedriver:** This acts as a bridge between the Selenium code and the Chrome browser, telling Selenium how to interact with the browser. Different drivers exist for different browsers (e.g., Safari, Firefox).
5.  **Browser Control:**
    * `driver.close()`: Closes the active tab.
    * `driver.quit()`: Quits the entire browser. It's preferred to use `quit()` after completing tasks to ensure a fresh browser instance for future runs.

### 🔎 Example: Open a Page and Find an Element
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time_module

# Start the browser
browser = webdriver.Chrome()
browser.get("https://www.python.org")

# Find elements
event_times = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time, name in zip(event_times, event_names):
    print(time.text, name.text)

# Wait for 3 seconds before closing
time_module.sleep(3)

browser.quit()
```

### 🔍 Finding and Selecting Elements on a Website

**Locating Elements:** 

Selenium offers various strategies to find HTML elements on a webpage. Once you have identified an element with the inspect tool of the browser, you can copy its Xpath or other and usit as identifier with:

* **`find_element()` method:** Used to find a single element.
* **`By` Class:** Important for specifying the location strategy (e.g., `By.CLASS_NAME`, `By.ID`, `By.NAME`, `By.LINK_TEXT`).
* **Examples:**
    * **By Class Name:** To get the price of an item on Amazon, you might find elements with classes like "a-price-whole" (for dollars) and "a-price-fraction" (for cents).
    * **Accessing Text Content:** After finding an element, use `.text` to retrieve the text content within that HTML element.
    * **By Name:** Useful for form input fields.
    * **By Link Text:** Specifically for clicking on links by their visible text.
* **`find_elements()` method:** For every `find_element()` method, there's a `find_elements()` counterpart that returns a list of all matching elements.
* **Inspecting Elements:** Use Chrome Developer Tools (right-click -> Inspect) to examine the HTML structure and identify IDs, class names, or other attributes for elements.

### 🖱️ Automating Interactions (Typing and Clicking)

* **Clicking Elements:**
    * After identifying an element, use the `.click()` method on the element object.
    * Selenium can click on links based on their `LINK_TEXT`.
* **Typing into Input Fields:**
    * First, find the input field element.
    * Use the `.send_keys()` method on the element object, passing the string you want to type.
* **Sending Special Keys:** To send keys like `Enter` or `Return`, import the `Keys` class from `selenium.webdriver.common.keys`.


---

## 📝 Challenge: Scrape Upcoming Python Events <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Use Selenium to open [python.org](https://www.python.org/)
- Extract the date and name of the next 5 events
- Store them in a dictionary like:

```python
events = {
    0: {"time": "2025-06-11", "name": "PyCon"},
    1: {"time": "2025-06-18", "name": "DjangoCon"},
    # ...
}
```

---

## 🚀 Summary <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Use Beautiful Soup for static HTML scraping
- Use Selenium for dynamic, interactive sites
- Always respect website rules and ethics

You now have the tools to collect data from almost any website. Happy scraping!
