---
title: Day 4 Web Foundations HTML, CSS, Bootstrap & Web Design
layout: default
nav_order: 5
has_children: false
nav_exclude: false
---

# Day 4. Web Foundations. 🕸️ HTML, CSS, Bootstrap & Web Design
{: .no_toc }

Welcome to Day 4! Today, you’ll build a solid foundation in web development by learning how the internet works, the essentials of HTML and CSS, and how to use Bootstrap for rapid, beautiful web design. We’ll also cover the basics of web design theory to help you create websites people will love.

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

## 🌐 How Does the Internet Actually Work?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Before building websites, it’s important to understand how the internet connects users and servers.

- **Internet**: A [global network of computers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) communicating via protocols (TCP/IP).
- **Websites**: Hosted on servers, accessed by clients (browsers) via [URLs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL) (Uniform Resource Locator).
- **HTTP/HTTPS**: Protocols for transferring web data.
- **DNS** ([Domain Name System](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name)): Translates human-friendly domain names (like google.com) into IP addresses.

**How Websites Work:**
1. You type a URL in your browser.
2. The browser asks a DNS server for the IP address.
3. The browser sends an HTTP request to the server.
4. The server responds with HTML (for elements), CSS (format), JS (actions), images, etc.
5. The browser (Chrome, Firefox, Edge, Safari) renders the page.

when you deploy a website and assign a domain to an IP address at the DNS server. DNS servers run 24/7 but they update DNS-IP pairs once or twice a day only.

**Inspecting Websites**

The files that are received by the browser can be reviewed with DevTools (F12) in Chrome to inspect and modify HTML, CSS live. You can also right click over an element and then click on inspect and it takes you to the piece of code that you want to check. 

To do a test right click in the title `Inspecting Websites` and click in inspect. 

![Inspect_window_Chrome](Inspect_window_Chrome.png)

The browser has a set of tools for inspecting elements (the html code), styles (the CSS code), a terminal to directly execute code or see in what order and how long does it take to download and run the code from the server. You can also recorde actions, or load extensions. The browser has many more possibilities than what it looks at first.

![Editing HTML in browser](Editing_HTML_in_browser.gif)

---


## 📝 HTML: The Structure of the Web<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### What is HTML?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- **HTML (HyperText Markup Language)** is the standard language for creating web pages that can be rendered by most browsers. It structures content using **elements** (tags) such as `<title>My First Webpage</title>` in a static non-formatted fashion. 
Generally tags have an open tag such as `<details></details>`, but some tags don’t need a closing tag, e.g. `<img />` for images, `<br>` for new line, `<hr>` for a horizontal line.

### HTML Boilerplate<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Every HTML page starts with a basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My First Webpage</title>
</head>
<body>
  <!-- Content goes here --> 
   Hello World!
</body>
</html>
```

### Headings, Paragraphs, and Lists<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
The [most basic elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Solve_HTML_problems) are headings or titles (there are 7 of them), paragraphs and lists. You can find the full list of elements in [W3Schools](https://www.w3schools.com/html/default.asp)

Try and play with the code below in [W3Schools html web testing](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My First Webpage</title>
</head>
<body>
  <h1>Main Heading</h1>
  <h2>Subheading</h2>
  <p>This is a paragraph of text.</p>

  <ul>
    <li>Unordered list item</li>
  </ul>
  <ol>
    <li>Ordered list item</li>
  </ol>
</body>
</html>

```

### Anchor and Image Elements<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Anchor elements are used to create links. Images are included with the tag `<img src="image file">`. It is recommended to include a description for accessibility. 

```html
<a href="https://www.example.com">Visit Example</a>
<img src="image.jpg" alt="Description">
```

### Nesting and Indentation<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

HTML elements can be nested. It is recommended to write them with proper indentation improves readability.

```html
<ul>
  <li>
    <a href="#">Nested Link</a>
  </li>
</ul>
```

### Forms<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Forms are used to collect user input on a web page. Each form can have labels, input fields, and placeholders to guide the user as well as buttons to submit the information.

Example:
```html
<form>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Enter your name">
  <button type="submit">Send</button>
</form>
```

### Styles<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

You can style HTML elements inline using the `style` attribute directly in the tag. This is called inline styling. For example, you can change the font size, text alignment, color, and more.

Example:
```html
<p style="font-size:18px; text-align:center; color:blue; font-family:Arial;">This is a styled paragraph.</p>
```

Instead of asigning tab by tag the styles, which would be messy and take a long time, tags are assigned to classes and or IDs and then the styles for the classes or IDs are specified in a CSS file as it is explained later on. 


### HTML Elements with IDs and Classes<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Both IDs and classes are attributes that can be added to HTML elements to make them selectable for CSS styling or JavaScript manipulation. The key differences:

- **ID**: Must be unique on the page (only one element should have a specific ID)
- **Class**: Can be reused across multiple elements

```html
<h2 id="welcome-title" class="section-title">Welcome to My Website</h2>
<p id="intro-text" class="content-paragraph">This paragraph has both an ID and a class. 
The ID "intro-text" can only be used once on this page, while the "content-paragraph" 
class can be applied to multiple paragraph elements.</p>
```

In CSS, you would select these elements using:
```css
/* Select by ID (uses # symbol) */
#welcome-title {
  color: navy;
  font-size: 28px;
}

#intro-text {
  font-style: italic;
}

/* Select by class (uses . symbol) */
.section-title {
  border-bottom: 2px solid #ccc;
  padding-bottom: 10px;
}

.content-paragraph {
  line-height: 1.6;
  margin-bottom: 20px;
}
```



### Divs<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
The <div> HTML element is a generic container for flow content. It's a "division" or "section" of a web page. They are used to group other HTML elements together. 

### Full html template<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

<details markdown="block">
  <summary>
    For a full showcase view of all types of HTML elements see the code below. 
  </summary>

This can be visualised in [W3Schools html web testing](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic)

{% raw %}
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Elements Showcase</title>
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Light gray background */
            color: #374151; /* Dark gray text */
        }
    </style>
</head>
<body class="p-4 sm:p-8 md:p-12 lg:p-16">
    <div class="max-w-4xl mx-auto bg-white shadow-xl rounded-xl p-6 sm:p-8 md:p-10 lg:p-12">

        <!-- Header Section -->
        <header class="mb-12 text-center">
            <h1 class="text-4xl sm:text-5xl font-extrabold text-blue-600 mb-4 rounded-lg p-2">HTML Elements Showcase</h1>
            <p class="text-lg sm:text-xl text-gray-700">A comprehensive template demonstrating common HTML elements with Tailwind CSS.</p>
        </header>

        <!-- Navigation Section -->
        <nav class="mb-12">
            <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Navigation</h2>
            <ul class="flex flex-wrap gap-4 justify-center">
                <li><a href="#typography" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Typography</a></li>
                <li><a href="#links-images" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Links & Images</a></li>
                <li><a href="#lists" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Lists</a></li>
                <li><a href="#tables" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Tables</a></li>
                <li><a href="#forms" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Forms</a></li>
                <li><a href="#media" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Media</a></li>
                <li><a href="#interactive" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Interactive</a></li>
            </ul>
        </nav>

        <!-- Main Content Area -->
        <main>
            <!-- Typography Section -->
            <section id="typography" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Typography</h2>

                <!-- Headings -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Headings</h3>
                <p class="mb-4">HTML provides six levels of headings, from `h1` (most important) to `h6` (least important).</p>
                <h1 class="text-4xl font-extrabold text-blue-700 mb-2">Heading 1 (h1) - Main Title</h1>
                <h2 class="text-3xl font-bold text-blue-600 mb-2">Heading 2 (h2) - Section Title</h2>
                <h3 class="text-2xl font-semibold text-blue-500 mb-2">Heading 3 (h3) - Sub-section Title</h3>
                <h4 class="text-xl font-medium text-blue-400 mb-2">Heading 4 (h4) - Minor Heading</h4>
                <h5 class="text-lg font-normal text-blue-300 mb-2">Heading 5 (h5) - Smaller Heading</h5>
                <h6 class="text-base font-light text-blue-200 mb-6">Heading 6 (h6) - Least Important Heading</h6>

                <!-- Paragraphs -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Paragraphs</h3>
                <p class="mb-4 text-gray-600 leading-relaxed">
                    This is a standard paragraph (`&lt;p&gt;`) of text. It's used for blocks of content.
                    We can add some <strong class="font-bold text-gray-800">strong (bold) text</strong> and
                    <em>emphasized (italic) text</em> using `&lt;strong&gt;` and `&lt;em&gt;` tags.
                </p>
                <p class="mb-6 text-gray-600 leading-relaxed">
                    Here's another paragraph demonstrating various inline text formatting options.
                    You can <mark class="bg-yellow-200 px-1 rounded">highlight text</mark> using `&lt;mark&gt;`.
                    <del class="line-through text-red-500">Deleted text</del> (`&lt;del&gt;`) and
                    <ins class="underline text-green-600">inserted text</ins> (`&lt;ins&gt;`) are also possible.
                    For scientific notation, you might use H<sub class="align-sub">2</sub>O (`&lt;sub&gt;`) or
                    E=mc<sup class="align-super">2</sup> (`&lt;sup&gt;`).
                </p>
            </section>

            <!-- Links and Images Section -->
            <section id="links-images" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Links & Images</h2>

                <!-- Links -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Links</h3>
                <p class="mb-4">
                    This is an external link:
                    <a href="https://www.google.com" target="_blank" rel="noopener noreferrer"
                       class="text-blue-600 hover:text-blue-800 underline font-medium transition-colors duration-200">
                        Visit Google
                    </a>.
                    Links (`&lt;a&gt;`) are crucial for navigation. The `target="_blank"` attribute opens the link in a new tab, and `rel="noopener noreferrer"` is a security best practice for external links.
                </p>

                <!-- Images -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Images</h3>
                <p class="mb-4">
                    An image (`&lt;img&gt;`) displayed below. The `alt` attribute is important for accessibility.
                    The `onerror` attribute provides a fallback in case the image fails to load.
                </p>
                <div class="flex justify-center mb-6">
                    <img src="https://placehold.co/400x200/ADD8E6/000000?text=Placeholder+Image"
                         alt="A simple placeholder image"
                         class="max-w-full h-auto rounded-lg shadow-md border-2 border-gray-200"
                         onerror="this.onerror=null;this.src='https://placehold.co/400x200/FF0000/FFFFFF?text=Image+Load+Error';">
                </div>
            </section>

            <!-- Lists Section -->
            <section id="lists" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Lists</h2>

                <!-- Unordered List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Unordered List (`&lt;ul&gt;`)</h3>
                <p class="mb-2">Items in an unordered list are typically marked with bullet points.</p>
                <ul class="list-disc list-inside mb-6 pl-4 text-gray-700">
                    <li class="mb-1">Item One</li>
                    <li class="mb-1">Item Two
                        <ul class="list-circle list-inside mt-1 pl-4">
                            <li class="mb-1">Nested Item A</li>
                            <li class="mb-1">Nested Item B</li>
                        </ul>
                    </li>
                    <li class="mb-1">Item Three</li>
                </ul>

                <!-- Ordered List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Ordered List (`&lt;ol&gt;`)</h3>
                <p class="mb-2">Items in an ordered list are typically numbered.</p>
                <ol class="list-decimal list-inside mb-6 pl-4 text-gray-700">
                    <li class="mb-1">First step</li>
                    <li class="mb-1">Second step</li>
                    <li class="mb-1">Third step</li>
                </ol>

                <!-- Description List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Description List (`&lt;dl&gt;`)</h3>
                <p class="mb-2">A list of terms and their descriptions.</p>
                <dl class="mb-6 text-gray-700">
                    <dt class="font-semibold text-gray-800 mt-2">HTML</dt>
                    <dd class="ml-6 mb-1">HyperText Markup Language: The standard markup language for creating web pages.</dd>
                    <dt class="font-semibold text-gray-800 mt-2">CSS</dt>
                    <dd class="ml-6 mb-1">Cascading Style Sheets: A stylesheet language used to describe the presentation of a document written in HTML.</dd>
                    <dt class="font-semibold text-gray-800 mt-2">JavaScript</dt>
                    <dd class="ml-6 mb-1">A programming language that enables interactive web pages.</dd>
                </dl>
            </section>

            <!-- Tables Section -->
            <section id="tables" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md overflow-x-auto">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Tables</h2>
                <p class="mb-4">Tables (`&lt;table&gt;`) are used to display tabular data.</p>
                <table class="w-full border-collapse text-left rounded-lg overflow-hidden shadow-md">
                    <thead class="bg-blue-600 text-white">
                        <tr>
                            <th class="py-3 px-4 border-b border-blue-700">Name</th>
                            <th class="py-3 px-4 border-b border-blue-700">Age</th>
                            <th class="py-3 px-4 border-b border-blue-700">City</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white">
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">John Doe</td>
                            <td class="py-2 px-4 border-b border-gray-200">30</td>
                            <td class="py-2 px-4 border-b border-gray-200">New York</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">Jane Smith</td>
                            <td class="py-2 px-4 border-b border-gray-200">24</td>
                            <td class="py-2 px-4 border-b border-gray-200">Los Angeles</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">Peter Jones</td>
                            <td class="py-2 px-4 border-b border-gray-200">45</td>
                            <td class="py-2 px-4 border-b border-gray-200">Chicago</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <!-- Forms Section -->
            <section id="forms" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Forms</h2>
                <p class="mb-4">Forms (`&lt;form&gt;`) are used to collect user input.</p>

                <form class="space-y-6">
                    <!-- Text Input -->
                    <div>
                        <label for="username" class="block text-sm font-medium text-gray-700 mb-1">Username:</label>
                        <input type="text" id="username" name="username" placeholder="Enter your username"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                               required>
                    </div>

                    <!-- Email Input -->
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email:</label>
                        <input type="email" id="email" name="email" placeholder="you@example.com"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Password Input -->
                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password:</label>
                        <input type="password" id="password" name="password" placeholder="••••••••"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                               minlength="8">
                    </div>

                    <!-- Number Input -->
                    <div>
                        <label for="quantity" class="block text-sm font-medium text-gray-700 mb-1">Quantity:</label>
                        <input type="number" id="quantity" name="quantity" value="1" min="1" max="10"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Textarea -->
                    <div>
                        <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message:</label>
                        <textarea id="message" name="message" rows="4" placeholder="Your message here..."
                                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"></textarea>
                    </div>

                    <!-- Select (Dropdown) -->
                    <div>
                        <label for="country" class="block text-sm font-medium text-gray-700 mb-1">Country:</label>
                        <select id="country" name="country"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-white">
                            <option value="">--Please choose an option--</option>
                            <option value="usa">United States</option>
                            <option value="can">Canada</option>
                            <option value="mex">Mexico</option>
                        </select>
                    </div>

                    <!-- Checkbox -->
                    <div class="flex items-center">
                        <input type="checkbox" id="newsletter" name="newsletter"
                               class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500">
                        <label for="newsletter" class="ml-2 block text-sm text-gray-900">Subscribe to newsletter</label>
                    </div>

                    <!-- Radio Buttons (Fieldset for grouping) -->
                    <fieldset class="border border-gray-300 p-4 rounded-md">
                        <legend class="text-base font-medium text-gray-900">Favorite Color:</legend>
                        <div class="mt-2 space-y-2">
                            <div class="flex items-center">
                                <input type="radio" id="color_red" name="fav_color" value="red"
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_red" class="ml-2 block text-sm text-gray-900">Red</label>
                            </div>
                            <div class="flex items-center">
                                <input type="radio" id="color_blue" name="fav_color" value="blue" checked
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_blue" class="ml-2 block text-sm text-gray-900">Blue</label>
                            </div>
                            <div class="flex items-center">
                                <input type="radio" id="color_green" name="fav_color" value="green"
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_green" class="ml-2 block text-sm text-gray-900">Green</label>
                            </div>
                        </div>
                    </fieldset>

                    <!-- File Input -->
                    <div>
                        <label for="profile_pic" class="block text-sm font-medium text-gray-700 mb-1">Upload Profile Picture:</label>
                        <input type="file" id="profile_pic" name="profile_pic" accept="image/*"
                               class="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100">
                    </div>

                    <!-- Range Input -->
                    <div>
                        <label for="volume" class="block text-sm font-medium text-gray-700 mb-1">Volume:</label>
                        <input type="range" id="volume" name="volume" min="0" max="100" value="50"
                               class="mt-1 block w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer range-lg">
                    </div>

                    <!-- Date Input -->
                    <div>
                        <label for="event_date" class="block text-sm font-medium text-gray-700 mb-1">Event Date:</label>
                        <input type="date" id="event_date" name="event_date"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Color Input -->
                    <div>
                        <label for="fav_color_picker" class="block text-sm font-medium text-gray-700 mb-1">Choose your favorite color:</label>
                        <input type="color" id="fav_color_picker" name="fav_color_picker" value="#4A90E2"
                               class="mt-1 block w-24 h-10 border border-gray-300 rounded-md cursor-pointer">
                    </div>

                    <!-- Submit Button -->
                    <div>
                        <button type="submit"
                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                            Submit Form
                        </button>
                    </div>
                </form>
            </section>

            <!-- Media Section -->
            <section id="media" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Media</h2>

                <!-- Audio -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Audio (`&lt;audio&gt;`)</h3>
                <p class="mb-4">Embed audio content. Note: A real audio file URL would be needed here.</p>
                <div class="flex justify-center mb-6">
                    <audio controls class="w-full max-w-lg rounded-lg shadow-md bg-gray-200 p-2">
                        <!-- Replace with a valid audio source -->
                        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>

                <!-- Video -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Video (`&lt;video&gt;`)</h3>
                <p class="mb-4">Embed video content. Note: A real video file URL would be needed here.</p>
                <div class="flex justify-center mb-6">
                    <video controls width="640" height="360" poster="https://placehold.co/640x360/A0A0A0/FFFFFF?text=Video+Placeholder"
                           class="max-w-full h-auto rounded-lg shadow-md border-2 border-gray-200">
                        <!-- Replace with a valid video source -->
                        <source src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </section>

            <!-- Interactive Elements Section -->
            <section id="interactive" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Interactive Elements</h2>

                <!-- Details/Summary -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Details and Summary (`&lt;details&gt;`, `&lt;summary&gt;`)</h3>
                <p class="mb-4">Provides an on-demand disclosure widget that the user can open and close.</p>
                <details class="bg-white border border-gray-300 rounded-md p-4 shadow-sm cursor-pointer hover:bg-gray-100 transition-colors duration-200">
                    <summary class="font-semibold text-lg text-blue-700">Click to reveal more information</summary>
                    <div class="mt-3 text-gray-700 leading-relaxed">
                        <p>This content is hidden by default and is revealed when the summary is clicked.</p>
                        <p>It's useful for FAQs, accordions, or hiding less important details.</p>
                    </div>
                </details>
            </section>
        </main>

        <!-- Aside Section (for tangential content) -->
        <aside class="mb-12 p-6 bg-blue-50 rounded-lg shadow-md border-l-4 border-blue-300">
            <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">About This Template</h2>
            <p class="text-gray-700 leading-relaxed">
                This template serves as a quick reference for common HTML elements. Each section demonstrates a different category of tags and how they can be styled using utility classes from <a href="https://tailwindcss.com/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 underline font-medium">Tailwind CSS</a>.
            </p>
            <p class="mt-3 text-gray-700 leading-relaxed">
                Remember to apply semantic HTML for better accessibility and SEO.
            </p>
        </aside>

        <!-- Footer Section -->
        <footer class="text-center text-gray-600 mt-12 pt-6 border-t-2 border-gray-200">
            <p>&copy; 2025 HTML Elements Showcase. All rights reserved.</p>
            <p class="text-sm mt-2">
                Created with love using HTML and Tailwind CSS.
            </p>
        </footer>

    </div>

    <!-- JavaScript Example (Optional) -->
    <script>
        // A simple JavaScript example demonstrating a console log
        // This script runs after the HTML document is loaded.
        console.log("HTML Elements Showcase Loaded!");

        // Example of adding an event listener to a button (if you had one)
        document.addEventListener('DOMContentLoaded', () => {
            const submitButton = document.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.addEventListener('click', (event) => {
                    // Prevent default form submission for demonstration
                    event.preventDefault();
                    console.log('Form submission attempted!');
                    // In a real application, you would handle form data here,
                    // e.g., send it to a server using fetch API.
                    // For now, we'll just show a simple message in the console.
                });
            }
        });
    </script>
</body>
</html>
```
{% endraw %}

</details>

<details>
  <summary>
    Full element showcase rendered below.
  </summary>
You can use F12 or right click inspect to see the html code for each element.

{% raw %}
```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Elements Showcase</title>
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Light gray background */
            color: #374151; /* Dark gray text */
        }
    </style>
</head>
<body class="p-4 sm:p-8 md:p-12 lg:p-16">
    <div class="max-w-4xl mx-auto bg-white shadow-xl rounded-xl p-6 sm:p-8 md:p-10 lg:p-12">

        <!-- Header Section -->
        <header class="mb-12 text-center">
            <h1 class="text-4xl sm:text-5xl font-extrabold text-blue-600 mb-4 rounded-lg p-2">HTML Elements Showcase</h1>
            <p class="text-lg sm:text-xl text-gray-700">A comprehensive template demonstrating common HTML elements with Tailwind CSS.</p>
        </header>

        <!-- Navigation Section -->
        <nav class="mb-12">
            <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Navigation</h2>
            <ul class="flex flex-wrap gap-4 justify-center">
                <li><a href="#typography" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Typography</a></li>
                <li><a href="#links-images" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Links & Images</a></li>
                <li><a href="#lists" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Lists</a></li>
                <li><a href="#tables" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Tables</a></li>
                <li><a href="#forms" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Forms</a></li>
                <li><a href="#media" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Media</a></li>
                <li><a href="#interactive" class="text-blue-600 hover:text-blue-800 text-lg font-medium p-2 rounded-md hover:bg-blue-50 transition-colors duration-200">Interactive</a></li>
            </ul>
        </nav>

        <!-- Main Content Area -->
        <main>
            <!-- Typography Section -->
            <section id="typography" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Typography</h2>

                <!-- Headings -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Headings</h3>
                <p class="mb-4">HTML provides six levels of headings, from `h1` (most important) to `h6` (least important).</p>
                <h1 class="text-4xl font-extrabold text-blue-700 mb-2">Heading 1 (h1) - Main Title</h1>
                <h2 class="text-3xl font-bold text-blue-600 mb-2">Heading 2 (h2) - Section Title</h2>
                <h3 class="text-2xl font-semibold text-blue-500 mb-2">Heading 3 (h3) - Sub-section Title</h3>
                <h4 class="text-xl font-medium text-blue-400 mb-2">Heading 4 (h4) - Minor Heading</h4>
                <h5 class="text-lg font-normal text-blue-300 mb-2">Heading 5 (h5) - Smaller Heading</h5>
                <h6 class="text-base font-light text-blue-200 mb-6">Heading 6 (h6) - Least Important Heading</h6>

                <!-- Paragraphs -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Paragraphs</h3>
                <p class="mb-4 text-gray-600 leading-relaxed">
                    This is a standard paragraph (`&lt;p&gt;`) of text. It's used for blocks of content.
                    We can add some <strong class="font-bold text-gray-800">strong (bold) text</strong> and
                    <em>emphasized (italic) text</em> using `&lt;strong&gt;` and `&lt;em&gt;` tags.
                </p>
                <p class="mb-6 text-gray-600 leading-relaxed">
                    Here's another paragraph demonstrating various inline text formatting options.
                    You can <mark class="bg-yellow-200 px-1 rounded">highlight text</mark> using `&lt;mark&gt;`.
                    <del class="line-through text-red-500">Deleted text</del> (`&lt;del&gt;`) and
                    <ins class="underline text-green-600">inserted text</ins> (`&lt;ins&gt;`) are also possible.
                    For scientific notation, you might use H<sub class="align-sub">2</sub>O (`&lt;sub&gt;`) or
                    E=mc<sup class="align-super">2</sup> (`&lt;sup&gt;`).
                </p>
            </section>

            <!-- Links and Images Section -->
            <section id="links-images" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Links & Images</h2>

                <!-- Links -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Links</h3>
                <p class="mb-4">
                    This is an external link:
                    <a href="https://www.google.com" target="_blank" rel="noopener noreferrer"
                       class="text-blue-600 hover:text-blue-800 underline font-medium transition-colors duration-200">
                        Visit Google
                    </a>.
                    Links (`&lt;a&gt;`) are crucial for navigation. The `target="_blank"` attribute opens the link in a new tab, and `rel="noopener noreferrer"` is a security best practice for external links.
                </p>

                <!-- Images -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Images</h3>
                <p class="mb-4">
                    An image (`&lt;img&gt;`) displayed below. The `alt` attribute is important for accessibility.
                    The `onerror` attribute provides a fallback in case the image fails to load.
                </p>
                <div class="flex justify-center mb-6">
                    <img src="https://placehold.co/400x200/ADD8E6/000000?text=Placeholder+Image"
                         alt="A simple placeholder image"
                         class="max-w-full h-auto rounded-lg shadow-md border-2 border-gray-200"
                         onerror="this.onerror=null;this.src='https://placehold.co/400x200/FF0000/FFFFFF?text=Image+Load+Error';">
                </div>
            </section>

            <!-- Lists Section -->
            <section id="lists" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Lists</h2>

                <!-- Unordered List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Unordered List (`&lt;ul&gt;`)</h3>
                <p class="mb-2">Items in an unordered list are typically marked with bullet points.</p>
                <ul class="list-disc list-inside mb-6 pl-4 text-gray-700">
                    <li class="mb-1">Item One</li>
                    <li class="mb-1">Item Two
                        <ul class="list-circle list-inside mt-1 pl-4">
                            <li class="mb-1">Nested Item A</li>
                            <li class="mb-1">Nested Item B</li>
                        </ul>
                    </li>
                    <li class="mb-1">Item Three</li>
                </ul>

                <!-- Ordered List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Ordered List (`&lt;ol&gt;`)</h3>
                <p class="mb-2">Items in an ordered list are typically numbered.</p>
                <ol class="list-decimal list-inside mb-6 pl-4 text-gray-700">
                    <li class="mb-1">First step</li>
                    <li class="mb-1">Second step</li>
                    <li class="mb-1">Third step</li>
                </ol>

                <!-- Description List -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Description List (`&lt;dl&gt;`)</h3>
                <p class="mb-2">A list of terms and their descriptions.</p>
                <dl class="mb-6 text-gray-700">
                    <dt class="font-semibold text-gray-800 mt-2">HTML</dt>
                    <dd class="ml-6 mb-1">HyperText Markup Language: The standard markup language for creating web pages.</dd>
                    <dt class="font-semibold text-gray-800 mt-2">CSS</dt>
                    <dd class="ml-6 mb-1">Cascading Style Sheets: A stylesheet language used to describe the presentation of a document written in HTML.</dd>
                    <dt class="font-semibold text-gray-800 mt-2">JavaScript</dt>
                    <dd class="ml-6 mb-1">A programming language that enables interactive web pages.</dd>
                </dl>
            </section>

            <!-- Tables Section -->
            <section id="tables" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md overflow-x-auto">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Tables</h2>
                <p class="mb-4">Tables (`&lt;table&gt;`) are used to display tabular data.</p>
                <table class="w-full border-collapse text-left rounded-lg overflow-hidden shadow-md">
                    <thead class="bg-blue-600 text-white">
                        <tr>
                            <th class="py-3 px-4 border-b border-blue-700">Name</th>
                            <th class="py-3 px-4 border-b border-blue-700">Age</th>
                            <th class="py-3 px-4 border-b border-blue-700">City</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white">
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">John Doe</td>
                            <td class="py-2 px-4 border-b border-gray-200">30</td>
                            <td class="py-2 px-4 border-b border-gray-200">New York</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">Jane Smith</td>
                            <td class="py-2 px-4 border-b border-gray-200">24</td>
                            <td class="py-2 px-4 border-b border-gray-200">Los Angeles</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-4 border-b border-gray-200">Peter Jones</td>
                            <td class="py-2 px-4 border-b border-gray-200">45</td>
                            <td class="py-2 px-4 border-b border-gray-200">Chicago</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <!-- Forms Section -->
            <section id="forms" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Forms</h2>
                <p class="mb-4">Forms (`&lt;form&gt;`) are used to collect user input.</p>

                <form class="space-y-6">
                    <!-- Text Input -->
                    <div>
                        <label for="username" class="block text-sm font-medium text-gray-700 mb-1">Username:</label>
                        <input type="text" id="username" name="username" placeholder="Enter your username"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                               required>
                    </div>

                    <!-- Email Input -->
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email:</label>
                        <input type="email" id="email" name="email" placeholder="you@example.com"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Password Input -->
                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password:</label>
                        <input type="password" id="password" name="password" placeholder="••••••••"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                               minlength="8">
                    </div>

                    <!-- Number Input -->
                    <div>
                        <label for="quantity" class="block text-sm font-medium text-gray-700 mb-1">Quantity:</label>
                        <input type="number" id="quantity" name="quantity" value="1" min="1" max="10"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Textarea -->
                    <div>
                        <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message:</label>
                        <textarea id="message" name="message" rows="4" placeholder="Your message here..."
                                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"></textarea>
                    </div>

                    <!-- Select (Dropdown) -->
                    <div>
                        <label for="country" class="block text-sm font-medium text-gray-700 mb-1">Country:</label>
                        <select id="country" name="country"
                                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-white">
                            <option value="">--Please choose an option--</option>
                            <option value="usa">United States</option>
                            <option value="can">Canada</option>
                            <option value="mex">Mexico</option>
                        </select>
                    </div>

                    <!-- Checkbox -->
                    <div class="flex items-center">
                        <input type="checkbox" id="newsletter" name="newsletter"
                               class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500">
                        <label for="newsletter" class="ml-2 block text-sm text-gray-900">Subscribe to newsletter</label>
                    </div>

                    <!-- Radio Buttons (Fieldset for grouping) -->
                    <fieldset class="border border-gray-300 p-4 rounded-md">
                        <legend class="text-base font-medium text-gray-900">Favorite Color:</legend>
                        <div class="mt-2 space-y-2">
                            <div class="flex items-center">
                                <input type="radio" id="color_red" name="fav_color" value="red"
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_red" class="ml-2 block text-sm text-gray-900">Red</label>
                            </div>
                            <div class="flex items-center">
                                <input type="radio" id="color_blue" name="fav_color" value="blue" checked
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_blue" class="ml-2 block text-sm text-gray-900">Blue</label>
                            </div>
                            <div class="flex items-center">
                                <input type="radio" id="color_green" name="fav_color" value="green"
                                       class="focus:ring-blue-500 h-4 w-4 text-blue-600 border-gray-300">
                                <label for="color_green" class="ml-2 block text-sm text-gray-900">Green</label>
                            </div>
                        </div>
                    </fieldset>

                    <!-- File Input -->
                    <div>
                        <label for="profile_pic" class="block text-sm font-medium text-gray-700 mb-1">Upload Profile Picture:</label>
                        <input type="file" id="profile_pic" name="profile_pic" accept="image/*"
                               class="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100">
                    </div>

                    <!-- Range Input -->
                    <div>
                        <label for="volume" class="block text-sm font-medium text-gray-700 mb-1">Volume:</label>
                        <input type="range" id="volume" name="volume" min="0" max="100" value="50"
                               class="mt-1 block w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer range-lg">
                    </div>

                    <!-- Date Input -->
                    <div>
                        <label for="event_date" class="block text-sm font-medium text-gray-700 mb-1">Event Date:</label>
                        <input type="date" id="event_date" name="event_date"
                               class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    </div>

                    <!-- Color Input -->
                    <div>
                        <label for="fav_color_picker" class="block text-sm font-medium text-gray-700 mb-1">Choose your favorite color:</label>
                        <input type="color" id="fav_color_picker" name="fav_color_picker" value="#4A90E2"
                               class="mt-1 block w-24 h-10 border border-gray-300 rounded-md cursor-pointer">
                    </div>

                    <!-- Submit Button -->
                    <div>
                        <button type="submit"
                                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-200">
                            Submit Form
                        </button>
                    </div>
                </form>
            </section>

            <!-- Media Section -->
            <section id="media" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Media</h2>

                <!-- Audio -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Audio (`&lt;audio&gt;`)</h3>
                <p class="mb-4">Embed audio content. Note: A real audio file URL would be needed here.</p>
                <div class="flex justify-center mb-6">
                    <audio controls class="w-full max-w-lg rounded-lg shadow-md bg-gray-200 p-2">
                        <!-- Replace with a valid audio source -->
                        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>

                <!-- Video -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Video (`&lt;video&gt;`)</h3>
                <p class="mb-4">Embed video content. Note: A real video file URL would be needed here.</p>
                <div class="flex justify-center mb-6">
                    <video controls width="640" height="360" poster="https://placehold.co/640x360/A0A0A0/FFFFFF?text=Video+Placeholder"
                           class="max-w-full h-auto rounded-lg shadow-md border-2 border-gray-200">
                        <!-- Replace with a valid video source -->
                        <source src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </section>

            <!-- Interactive Elements Section -->
            <section id="interactive" class="mb-12 p-6 bg-gray-50 rounded-lg shadow-md">
                <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">Interactive Elements</h2>

                <!-- Details/Summary -->
                <h3 class="text-2xl font-bold text-gray-700 mb-3">Details and Summary (`&lt;details&gt;`, `&lt;summary&gt;`)</h3>
                <p class="mb-4">Provides an on-demand disclosure widget that the user can open and close.</p>
                <details class="bg-white border border-gray-300 rounded-md p-4 shadow-sm cursor-pointer hover:bg-gray-100 transition-colors duration-200">
                    <summary class="font-semibold text-lg text-blue-700">Click to reveal more information</summary>
                    <div class="mt-3 text-gray-700 leading-relaxed">
                        <p>This content is hidden by default and is revealed when the summary is clicked.</p>
                        <p>It's useful for FAQs, accordions, or hiding less important details.</p>
                    </div>
                </details>
            </section>
        </main>

        <!-- Aside Section (for tangential content) -->
        <aside class="mb-12 p-6 bg-blue-50 rounded-lg shadow-md border-l-4 border-blue-300">
            <h2 class="text-3xl font-semibold text-gray-800 mb-4 pb-2 border-b-2 border-blue-300 rounded-lg">About This Template</h2>
            <p class="text-gray-700 leading-relaxed">
                This template serves as a quick reference for common HTML elements. Each section demonstrates a different category of tags and how they can be styled using utility classes from <a href="https://tailwindcss.com/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 underline font-medium">Tailwind CSS</a>.
            </p>
            <p class="mt-3 text-gray-700 leading-relaxed">
                Remember to apply semantic HTML for better accessibility and SEO.
            </p>
        </aside>

        <!-- Footer Section -->
        <footer class="text-center text-gray-600 mt-12 pt-6 border-t-2 border-gray-200">
            <p>&copy; 2025 HTML Elements Showcase. All rights reserved.</p>
            <p class="text-sm mt-2">
                Created with love using HTML and Tailwind CSS.
            </p>
        </footer>

    </div>

    <!-- JavaScript Example (Optional) -->
    <script>
        // A simple JavaScript example demonstrating a console log
        // This script runs after the HTML document is loaded.
        console.log("HTML Elements Showcase Loaded!");

        // Example of adding an event listener to a button (if you had one)
        document.addEventListener('DOMContentLoaded', () => {
            const submitButton = document.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.addEventListener('click', (event) => {
                    // Prevent default form submission for demonstration
                    event.preventDefault();
                    console.log('Form submission attempted!');
                    // In a real application, you would handle form data here,
                    // e.g., send it to a server using fetch API.
                    // For now, we'll just show a simple message in the console.
                });
            }
        });
    </script>
</body>
</html>
```
{% endraw %}

</details>

---

## 🎨 CSS: Styling the Web<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### Why Do We Need CSS?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- **CSS (Cascading Style Sheets)** controls the appearance of HTML elements. It separates content (HTML) from presentation (CSS).

### Adding CSS<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**Inline:**
```html
<p style="color: red;">Red text</p>
```
**Internal:**
When you set a list of styles in the html file to apply to all elements.

```html
<head>
  <style>
    p { color: blue; } // Aplies to all paragraphs
  </style>
</head>
```

**External:**
In a css file that is referred in the html file as shown below. 
```html
<link rel="stylesheet" href="styles.css">
```

### CSS Selectors and Properties<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Selectors allow you to target specific elements, groups of elements, or elements based on their attributes, states, or relationships to other elements.

#### Simple Selectors<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>


<details markdown="block">
  <summary>
    Universal Selector (*)
  </summary>
Selects all elements on the page.

```css
* {
  box-sizing: border-box;
}
```

</details>

<details markdown="block">
  <summary>
    Element Selector
  </summary>
Selects all HTML elements of a specified type (tag name).

```css
p {
  font-size: 16px;
}
```

</details>

<details markdown="block">
  <summary>
    Class Selector (.class_name)
  </summary>
Selects all elements with a specific class attribute.

```css
.my-class {
  color: blue;
}
```

</details>

<details markdown="block">
  <summary>
    ID Selector (#id_name)
  </summary>
Selects a single element with a specific id attribute. IDs should be unique within a page.

```css
#header {
  background-color: gray;
}
```
</details>

#### Combinator Selectors<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Combinators allow you to select elements based on their relationship to other elements in the document tree.

<details markdown="block">
  <summary>
    Descendant Selector
  </summary>

```css
div p {
  margin-bottom: 10px;
} /* Selects all paragraphs inside any div */
```

</details>

<details markdown="block">
  <summary>
    Child Selector
  </summary>

```css
ul > li {
  list-style-type: none;
} /* Selects all li elements that are direct children of a ul */
```
</details>

#### Attribute Selectors<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
They select elements based on their attributes.

<details markdown="block">
  <summary>
    Presence Selector ([attribute])
  </summary>

Selects elements that have the specified attribute.

```css
[data-tooltip] {
  position: relative;
}
```
</details>

<details markdown="block">
  <summary>
    Attribute Value Selector ([attribute="value"])
  </summary>

Selects elements where the attribute's value is exactly equal to "value".

```css
input[type="text"] {
  border: 1px solid #ccc;
}
```

</details>

#### Pseudo-classes<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Select elements based on a specific state, condition, or position.


<details markdown="block">
  <summary>
    User Action Pseudo-classes
  </summary>

`:hover:` When the mouse pointer is over an element.

`:active:` When an element is being activated by the user (e.g., clicked).

`:focus:` When an element has input focus.

`:visited:` For links that have been visited by the user.

`:link:` For unvisited links.

</details>

<details markdown="block">
  <summary>
    Structural Pseudo-classes
  </summary>

`:first-child:` Selects the first child of its parent.

`:last-child:` Selects the last child of its parent.

`:nth-child(n):` Selects the n-th child of its parent (can use keywords like even, odd, or formulas like 2n+1).

`:first-of-type:` Selects the first sibling of its type.

`:last-of-type:` Selects the last sibling of its type.

`:nth-of-type(n):` Selects the n-th sibling of its type.

`:only-child:` Selects an element that is the only child of its parent.

`:only-of-type:` Selects an element that is the only sibling of its type.

`:empty:` Selects elements that have no children (including text nodes).

`:root:` Selects the root element of the document (usually <html>).

</details>


<details markdown="block">
  <summary>
    Form Pseudo-classes
  </summary>

`:checked:` For radio buttons or checkboxes that are checked.

`:disabled:` For disabled input elements.

`:enabled:` For enabled input elements.

`:required:` For input elements with the required attribute.

`:optional:` For input elements without the required attribute.

`:valid:` For input elements with valid values.

`:invalid:` For input elements with invalid values.

</details>

<details markdown="block">
  <summary>
    Other Pseudo-classes
  </summary>

`:not(selector):` Selects elements that do NOT match the given selector.

`:has(selector):` Selects elements that contain at least one element matching the given selector (still experimental/not fully supported in all browsers).

`:is(selector-list):` Matches any element in a comma-separated list of selectors.

`:where(selector-list):` Similar to :is(), but adds no specificity.

</details>

#### Pseudo-elements <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
For specific parts of an element. Prefixed with a double colon (::).


<details markdown="block">
  <summary>
    Other Pseudo-classes
  </summary>

`::before:` Inserts content before the content of an element.

`::after:` Inserts content after the content of an element.

`::first-letter:` Selects the first letter of the first line of a block-level element.

`::first-line:` Selects the first line of a block-level element.

`::selection:` Selects the portion of an element that is highlighted by the user.

`::marker:` Selects the marker box of a list item (e.g., bullets or numbers).

`::placeholder:` Selects the placeholder text in an input field.

</details>


### CSS Colors<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Colors in CSS can be expressed in different ways:

- Named colors: `red`, `blue`
- Hex: `#ff5733`
- RGB: `rgb(255, 87, 51)`

### Font Properties<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
In CSS there are two main types of fonts: 
- System Fonts (or Web-Safe Fonts): These are fonts that are generally pre-installed on most operating systems (like Arial, Times New Roman, Verdana, Georgia, etc.). When you specify a system font in your CSS, the user's browser will try to use that font if it's available on their system. If not, it will fall back to a generic font family you specify (e.g., sans-serif).

- Web Fonts (or Custom Fonts): These are font files that you host yourself or link from a web font service (like Google Fonts, Adobe Fonts). When you use a web font, the font file is downloaded by the user's browser along with your website's other assets. This ensures that the user sees the exact font you intended, regardless of what fonts are installed on their system.

The common ways to get web fonts:

- Self-hosting: You download the font files (e.g., .woff2, .woff, .ttf, .otf) and place them on your server.
- Google Fonts: This is a very popular and easy way. You select fonts from their library, and Google provides you with a <link> tag to put in your HTML <head> or an @import rule for your CSS, which handles the font hosting and delivery for you.
- Other font services: There are many other services offering web fonts, often with different licensing models.

Below an example of font asigned to the body.
```css
body {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
}
```

### The CSS Box Model<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Every element on a web page is treated as a rectangular box by the browser. The CSS box model describes how these boxes are structured and how spacing works around and inside elements:

- **Content**: The actual text, image, or other media inside the element.
- **Padding**: The space between the content and the border. Padding adds space *inside* the element, around the content.
- **Border**: The line that wraps around the padding and content. Borders can have different widths, styles, and colors.
- **Margin**: The space *outside* the border, separating the element from other elements on the page. Margins create space between boxes.

Visually, the structure is:

```
|  Margin  |  ← space outside the border
| [Border  |  ← border wraps the padding and content
| |Padding |  ← space inside the border, around content
| | Content|  ← the actual element content
```
You can explore the result in the chrome inspector.

![Margin and border](Margin_border_Chrome.gif)

You can control each part with CSS properties like `margin`, `padding`, and `border`. For example:

```css
div {
  margin: 20px;      /* space outside the border */
  padding: 10px;     /* space inside the border */
  border: 2px solid #333; /* border around the element */
}
```



---

## 🚀 Introduction to JavaScript<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

JavaScript is the programming language that brings web pages to life. While HTML provides the structure and CSS handles the appearance, JavaScript enables interactivity, dynamic content, and logic on the client side (in the browser). Javascript has an extensive and complex list of commands, modules and frameworks that are not explained here. Javascript may be used both for Frontend and Backend. We will only cover some basics here to be able to identify it when inspecting websites. 

### What Can JavaScript Do?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
- Respond to user actions (clicks, typing, mouse movement)
- Change the content or style of a web page without reloading
- Validate forms before they are submitted
- Create interactive elements like sliders, modals, and tabs
- Fetch data from servers and update the page (AJAX, APIs)
- Build games, animations, and much more

### How to Use JavaScript<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
You can add JavaScript to your web page in several ways:
- **Inline**: Directly in an HTML element’s attribute (not recommended for complex code)
- **Internal**: Inside a `<script>` tag in your HTML file
- **External**: In a separate `.js` file linked to your HTML

Example (inline):
```html
<button onclick="alert('Hello!')">Click me</button>
```

Example (internal):
```html
<script>
  function greet() {
    alert('Hello from JavaScript!');
  }
</script>
<button onclick="greet()">Greet</button>
```

Example (external):
```html
<script src="script.js"></script>
```

### Try It Yourself<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Open your browser’s DevTools (F12), go to the Console tab, and type:
```js
console.log('Hello, world!');
```
You’ll see the message appear in the console. This is a great way to experiment and learn JavaScript basics!

---

## 💡 Bootstrap: Rapid Web Design<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### What is Bootstrap?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

It is a popular CSS framework for building responsive, mobile-first websites quickly. It includes ready-made components (buttons, navbars, cards) and a grid system.

### Bootstrap Layout<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Bootstrap styles are included as a reference in your html file. You can directly link the cloud repository or download a copy and store it with the rest of your files. 
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css">
<div class="container">
  <div class="row">
    <div class="col-md-6">Column 1</div>
    <div class="col-md-6">Column 2</div>
  </div>
</div>
```

### Bootstrap Components<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Bootstrap includes:
- Buttons: `<button class="btn btn-primary">Click</button>`
- Alerts: `<div class="alert alert-success">Success!</div>`
- Navbars, cards, forms, and more.

<details markdown="block">
  <summary>
    Bootstrap template code
  </summary>

This template was generated with Gemini with the prompt: `can you write an html code with all types of HTML/css elements in a template fashion to showcase what can be done in Bootstrap?`

You can visualise this code in [W3Schools html web testing](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic)<br>

{% raw %}
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap & Tailwind CSS Showcase</title>
    <!-- Inter font from Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" xintegrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f9fa; /* Light gray background */
        }
        .section-header {
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
            font-weight: 600;
            color: #343a40;
        }
        .card {
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-radius: 0.75rem; /* More rounded corners */
            overflow: hidden;
            transition: transform 0.2s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .btn-custom {
            background-image: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
            border: none;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            color: white; /* Ensure text remains white on hover */
        }
        /* Custom styles for better spacing and aesthetics */
        .container-fluid {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .container {
            padding-top: 3rem;
            padding-bottom: 3rem;
        }
    </style>
</head>
<body>

    <!-- Navbar Section -->
    <nav class="navbar navbar-expand-lg bg-white shadow-sm py-3 px-4">
        <div class="container-fluid">
            <a class="navbar-brand text-lg font-bold text-gray-800" href="#">Bootstrap Showcase</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto space-x-4">
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" aria-current="page" href="#layout">Layout</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#components">Components</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#forms">Forms</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#utilities">Utilities</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-blue-600 to-purple-700 text-white py-20 px-4 text-center rounded-b-lg shadow-lg">
        <div class="container mx-auto">
            <h1 class="text-5xl font-extrabold mb-4">Explore Bootstrap's Power</h1>
            <p class="text-xl mb-8 opacity-90">A comprehensive template showcasing essential Bootstrap features and responsive design.</p>
            <button class="btn btn-lg btn-custom shadow-md hover:shadow-xl">Get Started</button>
        </div>
    </div>

    <main class="container mx-auto mt-12 px-4 md:px-0">

        <!-- Layout Section -->
        <section id="layout" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">1. Layout & Grid System</h2>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-blue-100 border border-blue-300 rounded-md text-blue-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 1 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-green-100 border border-green-300 rounded-md text-green-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 2 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-yellow-100 border border-yellow-300 rounded-md text-yellow-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 3 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-12">
                    <div class="p-4 bg-purple-100 border border-purple-300 rounded-md text-purple-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Full Width Column (col-md-12)</p>
                    </div>
                </div>
            </div>
            <p class="mt-6 text-gray-700">Demonstrates Bootstrap's responsive grid system, adapting columns for different screen sizes.</p>
        </section>

        <!-- Components Section -->
        <section id="components" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">2. Core Components</h2>

            <!-- Cards -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.1 Cards</h3>
            <div class="row g-4 mb-8">
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/FF5733/ffffff?text=Image+1" class="card-img-top w-full h-48 object-cover" alt="Card Image 1">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title One</h5>
                            <p class="card-text text-gray-700">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="#" class="btn btn-primary bg-blue-500 hover:bg-blue-600 border-none rounded-md px-4 py-2">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/33FF57/ffffff?text=Image+2" class="card-img-top w-full h-48 object-cover" alt="Card Image 2">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title Two</h5>
                            <p class="card-text text-gray-700">Another example card with a slightly longer content to show card height consistency.</p>
                            <a href="#" class="btn btn-success bg-green-500 hover:bg-green-600 border-none rounded-md px-4 py-2">Learn more</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/5733FF/ffffff?text=Image+3" class="card-img-top w-full h-48 object-cover" alt="Card Image 3">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title Three</h5>
                            <p class="card-text text-gray-700">This card demonstrates an image at the top and standard body content.</p>
                            <a href="#" class="btn btn-warning bg-yellow-500 hover:bg-yellow-600 border-none rounded-md px-4 py-2">View details</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Buttons -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.2 Buttons</h3>
            <div class="flex flex-wrap gap-3 mb-8 items-center">
                <button type="button" class="btn btn-primary rounded-lg px-4 py-2 shadow-md">Primary</button>
                <button type="button" class="btn btn-secondary rounded-lg px-4 py-2 shadow-md">Secondary</button>
                <button type="button" class="btn btn-success rounded-lg px-4 py-2 shadow-md">Success</button>
                <button type="button" class="btn btn-danger rounded-lg px-4 py-2 shadow-md">Danger</button>
                <button type="button" class="btn btn-warning rounded-lg px-4 py-2 shadow-md">Warning</button>
                <button type="button" class="btn btn-info rounded-lg px-4 py-2 shadow-md">Info</button>
                <button type="button" class="btn btn-light rounded-lg px-4 py-2 shadow-md">Light</button>
                <button type="button" class="btn btn-dark rounded-lg px-4 py-2 shadow-md">Dark</button>
                <button type="button" class="btn btn-link rounded-lg px-4 py-2">Link</button>
                <button type="button" class="btn btn-outline-primary rounded-lg px-4 py-2">Outline Primary</button>
                <button type="button" class="btn btn-custom rounded-lg px-4 py-2">Custom Gradient</button>
            </div>

            <!-- Alerts -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.3 Alerts</h3>
            <div class="mb-8 space-y-3">
                <div class="alert alert-primary rounded-lg p-3" role="alert">
                    A simple primary alert—check it out!
                </div>
                <div class="alert alert-secondary rounded-lg p-3" role="alert">
                    A simple secondary alert—check it out!
                </div>
                <div class="alert alert-success rounded-lg p-3" role="alert">
                    A simple success alert—check it out!
                </div>
                <div class="alert alert-danger rounded-lg p-3" role="alert">
                    A simple danger alert—check it out!
                </div>
                <div class="alert alert-warning rounded-lg p-3" role="alert">
                    A simple warning alert—check it out!
                </div>
                <div class="alert alert-info rounded-lg p-3" role="alert">
                    A simple info alert—check it out!
                </div>
            </div>

            <!-- Modals -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.4 Modals</h3>
            <button type="button" class="btn btn-primary rounded-lg px-4 py-2 shadow-md" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Launch demo modal
            </button>

            <!-- Modal Structure -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog rounded-lg">
                    <div class="modal-content rounded-lg shadow-lg">
                        <div class="modal-header border-b border-gray-200">
                            <h5 class="modal-title text-xl font-semibold" id="exampleModalLabel">Modal title</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body text-gray-700">
                            This is a sample modal content. You can put any HTML content here, such as forms, images, or text.
                        </div>
                        <div class="modal-footer border-t border-gray-200">
                            <button type="button" class="btn btn-secondary rounded-lg px-4 py-2" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary rounded-lg px-4 py-2">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Forms Section -->
        <section id="forms" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">3. Forms</h2>
            <form>
                <div class="mb-4">
                    <label for="exampleInputEmail1" class="form-label text-gray-700 font-medium">Email address</label>
                    <input type="email" class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="exampleInputEmail1" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text text-sm text-gray-500 mt-1">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-4">
                    <label for="exampleInputPassword1" class="form-label text-gray-700 font-medium">Password</label>
                    <input type="password" class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="exampleInputPassword1">
                </div>
                <div class="mb-4 form-check">
                    <input type="checkbox" class="form-check-input rounded-sm" id="exampleCheck1">
                    <label class="form-check-label text-gray-700" for="exampleCheck1">Check me out</label>
                </div>
                <div class="mb-4">
                    <label for="formControlTextarea1" class="form-label text-gray-700 font-medium">Example textarea</label>
                    <textarea class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="formControlTextarea1" rows="3"></textarea>
                </div>
                <div class="mb-4">
                    <label for="formFile" class="form-label text-gray-700 font-medium">Default file input example</label>
                    <input class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" type="file" id="formFile">
                </div>
                <div class="mb-4">
                    <label for="formSelect" class="form-label text-gray-700 font-medium">Select option</label>
                    <select class="form-select rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" aria-label="Default select example" id="formSelect">
                        <option selected>Open this select menu</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary rounded-lg px-4 py-2 shadow-md">Submit</button>
            </form>
        </section>

        <!-- Utilities Section -->
        <section id="utilities" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">4. Utility Classes</h2>

            <!-- Typography -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.1 Typography</h3>
            <p class="h1 text-blue-700 mb-2">h1. Bootstrap heading</p>
            <p class="h2 text-green-700 mb-2">h2. Bootstrap heading</p>
            <p class="h3 text-purple-700 mb-2">h3. Bootstrap heading</p>
            <p class="lead text-lg text-gray-700 mb-2">This is a lead paragraph, indicating a more prominent text element.</p>
            <p class="text-muted text-gray-500 mb-2">This text is muted.</p>
            <p class="font-bold mb-2">This text is bold using Tailwind's font-bold.</p>
            <p class="text-decoration-underline mb-8">This text is underlined.</p>

            <!-- Spacing (Margin & Padding) -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.2 Spacing</h3>
            <div class="bg-blue-100 p-4 mb-4 rounded-md">
                <div class="bg-blue-300 p-2 m-4 rounded-md">
                    <p class="text-blue-900">This div has `m-4` margin from Tailwind.</p>
                </div>
            </div>
            <div class="bg-green-100 p-4 mb-8 rounded-md">
                <div class="bg-green-300 py-3 px-5 rounded-md">
                    <p class="text-green-900">This div has `py-3 px-5` padding from Tailwind.</p>
                </div>
            </div>

            <!-- Colors -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.3 Colors</h3>
            <div class="flex flex-wrap gap-4 mb-8">
                <div class="p-4 rounded-md text-white bg-primary shadow-md">Primary Color</div>
                <div class="p-4 rounded-md text-white bg-secondary shadow-md">Secondary Color</div>
                <div class="p-4 rounded-md text-white bg-success shadow-md">Success Color</div>
                <div class="p-4 rounded-md text-white bg-danger shadow-md">Danger Color</div>
                <div class="p-4 rounded-md text-dark bg-warning shadow-md">Warning Color</div>
                <div class="p-4 rounded-md text-white bg-info shadow-md">Info Color</div>
                <div class="p-4 rounded-md text-dark bg-light shadow-md border">Light Color</div>
                <div class="p-4 rounded-md text-white bg-dark shadow-md">Dark Color</div>
                <div class="p-4 rounded-md text-white bg-gradient-to-r from-pink-500 to-red-500 shadow-md">Custom Gradient</div>
            </div>

            <!-- Shadows -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.4 Shadows</h3>
            <div class="flex flex-wrap gap-6 mb-8">
                <div class="p-6 bg-white rounded-lg shadow-sm">Small Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-md">Medium Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-lg">Large Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-xl">Extra Large Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-2xl">2XL Shadow</div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-8 mt-12 rounded-t-lg shadow-inner">
        <p class="text-sm">&copy; 2024 Bootstrap Showcase. All rights reserved.</p>
        <p class="text-xs opacity-75 mt-2">Built with Bootstrap and Tailwind CSS</p>
    </footer>

    <!-- Bootstrap JavaScript Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" xintegrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```
{% endraw %}

</details>

<details>
  <summary>
    Bootstrap template Rendered
  </summary>

```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap & Tailwind CSS Showcase</title>
    <!-- Inter font from Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" xintegrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f9fa; /* Light gray background */
        }
        .section-header {
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
            font-weight: 600;
            color: #343a40;
        }
        .card {
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-radius: 0.75rem; /* More rounded corners */
            overflow: hidden;
            transition: transform 0.2s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .btn-custom {
            background-image: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
            border: none;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            color: white; /* Ensure text remains white on hover */
        }
        /* Custom styles for better spacing and aesthetics */
        .container-fluid {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .container {
            padding-top: 3rem;
            padding-bottom: 3rem;
        }
    </style>
</head>
<body>

    <!-- Navbar Section -->
    <nav class="navbar navbar-expand-lg bg-white shadow-sm py-3 px-4">
        <div class="container-fluid">
            <a class="navbar-brand text-lg font-bold text-gray-800" href="#">Bootstrap Showcase</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto space-x-4">
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" aria-current="page" href="#layout">Layout</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#components">Components</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#forms">Forms</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-700 hover:text-blue-600 font-medium" href="#utilities">Utilities</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-blue-600 to-purple-700 text-white py-20 px-4 text-center rounded-b-lg shadow-lg">
        <div class="container mx-auto">
            <h1 class="text-5xl font-extrabold mb-4">Explore Bootstrap's Power</h1>
            <p class="text-xl mb-8 opacity-90">A comprehensive template showcasing essential Bootstrap features and responsive design.</p>
            <button class="btn btn-lg btn-custom shadow-md hover:shadow-xl">Get Started</button>
        </div>
    </div>

    <main class="container mx-auto mt-12 px-4 md:px-0">

        <!-- Layout Section -->
        <section id="layout" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">1. Layout & Grid System</h2>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-blue-100 border border-blue-300 rounded-md text-blue-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 1 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-green-100 border border-green-300 rounded-md text-green-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 2 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="p-4 bg-yellow-100 border border-yellow-300 rounded-md text-yellow-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Column 3 (col-md-6 col-lg-4)</p>
                    </div>
                </div>
                <div class="col-md-12">
                    <div class="p-4 bg-purple-100 border border-purple-300 rounded-md text-purple-800 h-full flex items-center justify-center">
                        <p class="text-lg font-medium">Full Width Column (col-md-12)</p>
                    </div>
                </div>
            </div>
            <p class="mt-6 text-gray-700">Demonstrates Bootstrap's responsive grid system, adapting columns for different screen sizes.</p>
        </section>

        <!-- Components Section -->
        <section id="components" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">2. Core Components</h2>

            <!-- Cards -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.1 Cards</h3>
            <div class="row g-4 mb-8">
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/FF5733/ffffff?text=Image+1" class="card-img-top w-full h-48 object-cover" alt="Card Image 1">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title One</h5>
                            <p class="card-text text-gray-700">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="#" class="btn btn-primary bg-blue-500 hover:bg-blue-600 border-none rounded-md px-4 py-2">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/33FF57/ffffff?text=Image+2" class="card-img-top w-full h-48 object-cover" alt="Card Image 2">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title Two</h5>
                            <p class="card-text text-gray-700">Another example card with a slightly longer content to show card height consistency.</p>
                            <a href="#" class="btn btn-success bg-green-500 hover:bg-green-600 border-none rounded-md px-4 py-2">Learn more</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="card h-full">
                        <img src="https://placehold.co/600x400/5733FF/ffffff?text=Image+3" class="card-img-top w-full h-48 object-cover" alt="Card Image 3">
                        <div class="card-body">
                            <h5 class="card-title text-xl font-semibold mb-2">Card Title Three</h5>
                            <p class="card-text text-gray-700">This card demonstrates an image at the top and standard body content.</p>
                            <a href="#" class="btn btn-warning bg-yellow-500 hover:bg-yellow-600 border-none rounded-md px-4 py-2">View details</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Buttons -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.2 Buttons</h3>
            <div class="flex flex-wrap gap-3 mb-8 items-center">
                <button type="button" class="btn btn-primary rounded-lg px-4 py-2 shadow-md">Primary</button>
                <button type="button" class="btn btn-secondary rounded-lg px-4 py-2 shadow-md">Secondary</button>
                <button type="button" class="btn btn-success rounded-lg px-4 py-2 shadow-md">Success</button>
                <button type="button" class="btn btn-danger rounded-lg px-4 py-2 shadow-md">Danger</button>
                <button type="button" class="btn btn-warning rounded-lg px-4 py-2 shadow-md">Warning</button>
                <button type="button" class="btn btn-info rounded-lg px-4 py-2 shadow-md">Info</button>
                <button type="button" class="btn btn-light rounded-lg px-4 py-2 shadow-md">Light</button>
                <button type="button" class="btn btn-dark rounded-lg px-4 py-2 shadow-md">Dark</button>
                <button type="button" class="btn btn-link rounded-lg px-4 py-2">Link</button>
                <button type="button" class="btn btn-outline-primary rounded-lg px-4 py-2">Outline Primary</button>
                <button type="button" class="btn btn-custom rounded-lg px-4 py-2">Custom Gradient</button>
            </div>

            <!-- Alerts -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.3 Alerts</h3>
            <div class="mb-8 space-y-3">
                <div class="alert alert-primary rounded-lg p-3" role="alert">
                    A simple primary alert—check it out!
                </div>
                <div class="alert alert-secondary rounded-lg p-3" role="alert">
                    A simple secondary alert—check it out!
                </div>
                <div class="alert alert-success rounded-lg p-3" role="alert">
                    A simple success alert—check it out!
                </div>
                <div class="alert alert-danger rounded-lg p-3" role="alert">
                    A simple danger alert—check it out!
                </div>
                <div class="alert alert-warning rounded-lg p-3" role="alert">
                    A simple warning alert—check it out!
                </div>
                <div class="alert alert-info rounded-lg p-3" role="alert">
                    A simple info alert—check it out!
                </div>
            </div>

            <!-- Modals -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">2.4 Modals</h3>
            <button type="button" class="btn btn-primary rounded-lg px-4 py-2 shadow-md" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Launch demo modal
            </button>

            <!-- Modal Structure -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog rounded-lg">
                    <div class="modal-content rounded-lg shadow-lg">
                        <div class="modal-header border-b border-gray-200">
                            <h5 class="modal-title text-xl font-semibold" id="exampleModalLabel">Modal title</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body text-gray-700">
                            This is a sample modal content. You can put any HTML content here, such as forms, images, or text.
                        </div>
                        <div class="modal-footer border-t border-gray-200">
                            <button type="button" class="btn btn-secondary rounded-lg px-4 py-2" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary rounded-lg px-4 py-2">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Forms Section -->
        <section id="forms" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">3. Forms</h2>
            <form>
                <div class="mb-4">
                    <label for="exampleInputEmail1" class="form-label text-gray-700 font-medium">Email address</label>
                    <input type="email" class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="exampleInputEmail1" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text text-sm text-gray-500 mt-1">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-4">
                    <label for="exampleInputPassword1" class="form-label text-gray-700 font-medium">Password</label>
                    <input type="password" class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="exampleInputPassword1">
                </div>
                <div class="mb-4 form-check">
                    <input type="checkbox" class="form-check-input rounded-sm" id="exampleCheck1">
                    <label class="form-check-label text-gray-700" for="exampleCheck1">Check me out</label>
                </div>
                <div class="mb-4">
                    <label for="formControlTextarea1" class="form-label text-gray-700 font-medium">Example textarea</label>
                    <textarea class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" id="formControlTextarea1" rows="3"></textarea>
                </div>
                <div class="mb-4">
                    <label for="formFile" class="form-label text-gray-700 font-medium">Default file input example</label>
                    <input class="form-control rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" type="file" id="formFile">
                </div>
                <div class="mb-4">
                    <label for="formSelect" class="form-label text-gray-700 font-medium">Select option</label>
                    <select class="form-select rounded-md p-2 border border-gray-300 focus:ring focus:ring-blue-200" aria-label="Default select example" id="formSelect">
                        <option selected>Open this select menu</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary rounded-lg px-4 py-2 shadow-md">Submit</button>
            </form>
        </section>

        <!-- Utilities Section -->
        <section id="utilities" class="mb-12 bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-3xl section-header mb-8">4. Utility Classes</h2>

            <!-- Typography -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.1 Typography</h3>
            <p class="h1 text-blue-700 mb-2">h1. Bootstrap heading</p>
            <p class="h2 text-green-700 mb-2">h2. Bootstrap heading</p>
            <p class="h3 text-purple-700 mb-2">h3. Bootstrap heading</p>
            <p class="lead text-lg text-gray-700 mb-2">This is a lead paragraph, indicating a more prominent text element.</p>
            <p class="text-muted text-gray-500 mb-2">This text is muted.</p>
            <p class="font-bold mb-2">This text is bold using Tailwind's font-bold.</p>
            <p class="text-decoration-underline mb-8">This text is underlined.</p>

            <!-- Spacing (Margin & Padding) -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.2 Spacing</h3>
            <div class="bg-blue-100 p-4 mb-4 rounded-md">
                <div class="bg-blue-300 p-2 m-4 rounded-md">
                    <p class="text-blue-900">This div has `m-4` margin from Tailwind.</p>
                </div>
            </div>
            <div class="bg-green-100 p-4 mb-8 rounded-md">
                <div class="bg-green-300 py-3 px-5 rounded-md">
                    <p class="text-green-900">This div has `py-3 px-5` padding from Tailwind.</p>
                </div>
            </div>

            <!-- Colors -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.3 Colors</h3>
            <div class="flex flex-wrap gap-4 mb-8">
                <div class="p-4 rounded-md text-white bg-primary shadow-md">Primary Color</div>
                <div class="p-4 rounded-md text-white bg-secondary shadow-md">Secondary Color</div>
                <div class="p-4 rounded-md text-white bg-success shadow-md">Success Color</div>
                <div class="p-4 rounded-md text-white bg-danger shadow-md">Danger Color</div>
                <div class="p-4 rounded-md text-dark bg-warning shadow-md">Warning Color</div>
                <div class="p-4 rounded-md text-white bg-info shadow-md">Info Color</div>
                <div class="p-4 rounded-md text-dark bg-light shadow-md border">Light Color</div>
                <div class="p-4 rounded-md text-white bg-dark shadow-md">Dark Color</div>
                <div class="p-4 rounded-md text-white bg-gradient-to-r from-pink-500 to-red-500 shadow-md">Custom Gradient</div>
            </div>

            <!-- Shadows -->
            <h3 class="text-2xl font-semibold mb-4 text-gray-800">4.4 Shadows</h3>
            <div class="flex flex-wrap gap-6 mb-8">
                <div class="p-6 bg-white rounded-lg shadow-sm">Small Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-md">Medium Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-lg">Large Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-xl">Extra Large Shadow</div>
                <div class="p-6 bg-white rounded-lg shadow-2xl">2XL Shadow</div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-8 mt-12 rounded-t-lg shadow-inner">
        <p class="text-sm">&copy; 2024 Bootstrap Showcase. All rights reserved.</p>
        <p class="text-xs opacity-75 mt-2">Built with Bootstrap and Tailwind CSS</p>
    </footer>

    <!-- Bootstrap JavaScript Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" xintegrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```

</details>


### Markdown, Jekyll and Ruby<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

#### What is Markdown?

Markdown is a lightweight markup language for formatting text using plain text syntax. It's designed to be easy to read and write, and is widely used for documentation, README files, and static site generators.

**Basic Markdown Syntax:**
- Headings: `# Heading 1`, `## Heading 2`, ..., up to `###### Heading 6`
- Bold: `**bold text**` or `__bold text__`
- Italic: `*italic text*` or `_italic text_`
- Lists:  
  - Unordered: `- item` or `* item`
  - Ordered: `1. item`
- Links: `[link text](https://example.com)`
- Images: `![alt text](image-url)`
- Code:  
  - Inline: `` `code` ``
  - Block:  
    ```
    code block
    ```
- Blockquote: `> quoted text`

**Differences with HTML:**
- Markdown is simpler and more readable in raw form.
- HTML is more powerful and flexible, but more verbose.
- Markdown can be converted to HTML, but not all HTML features are available in Markdown.

For a full reference, see [Markdown Guide](https://www.markdownguide.org/basic-syntax/).

#### Jekyll and Ruby

[Jekyll](https://jekyllrb.com/) is a static site generator that converts Markdown files into HTML websites. It is the engine behind GitHub Pages, allowing you to publish documentation or blogs directly from a GitHub repository for free. Jekyll is written in the Ruby programming language.

#### This Website

This website is built using the [just-the-docs](https://just-the-docs.github.io/) theme, which is a Jekyll-based theme designed for documentation sites.




---

## 🎨 Web Design School: How to Create a Website People Will Love<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### Introduction to Web Design<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Web design is about more than just writing clean code—it’s about crafting a visual and emotional experience that speaks to your users. A successful design invites people in, tells a story, and guides them effortlessly toward a goal. In this guide, we explore the four pillars of effective web design: **Color Theory, Typography, User Interface (UI), and User Experience (UX)**. Once you've mastered these, you'll be equipped to create beautiful, human-centered websites.

---

### 🎨 Understanding Color Theory<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Color isn't just decoration—it conveys meaning, influences mood, and can even affect behavior. Here are key principles:

- **Consistency is key**: Avoid clashing colors. Instead, choose palettes that align with your brand and message.
- **Tell a story with color**:
  - 🔴**Red**: passion, energy, urgency—great for action-driven brands.
> *Example:* <a href="https://www.coca-cola.com/" target="_blank">Coca-Cola</a>
<img src="cocacola.png" alt="cocacola thumbnail" width="50%" style="display: block; margin: auto;">
> *Why it works:* Coca-Cola’s brand is all about excitement, fun, and refreshment. The bold red color sparks energy and urgency, making it feel dynamic and iconic.
  - 🟡**Yellow**: optimism, intellect, attention—effective for grabbing interest but avoid using it for large backgrounds.
> *Example:* <a href="https://www.mcdonalds.com/" target="_blank">McDonald’s</a>
<img src="mcdonalds.png" alt="mcdonalds thumbnail" width="50%" style="display: block; margin: auto;">  
> *Why it works:* McDonald's uses yellow to grab attention and convey a sense of happiness and friendliness. It’s especially effective in logos and accents, not overwhelming the background.
  - 🟢 **Green**: freshness, safety—ideal for eco or food-related businesses.
> *Example:* <a href="https://www.wholefoodsmarket.com/" target="_blank">Whole Foods Market</a> 
<img src="wholefoods.png" alt="wholefoods thumbnail" width="50%" style="display: block; margin: auto;">  
> *Why it works:* Whole Foods emphasizes health, nature, and sustainability. Green reinforces their commitment to fresh, organic food and environmentally conscious practices.
  - 🔵 **Blue**: trust, calm—popular with finance and tech firms.
> *Example:* <a href="https://www.paypal.com/" target="_blank">PayPal</a>   
<img src="paypal.png" alt="paypal thumbnail" width="50%" style="display: block; margin: auto;"> 
> *Why it works:* Blue is the dominant color in PayPal’s design, evoking trust, security, and professionalism—critical for a financial service provider. 
  - 🟣 **Purple**: royalty, femininity—often used in luxury and beauty products.
> *Example:* <a href="https://www.cadbury.co.uk/" target="_blank">Cadbury</a>  
<img src="cadbury.png" alt="cadbury thumbnail" width="50%" style="display: block; margin: auto;">  
> *Why it works:* Cadbury uses a rich purple to reflect luxury and indulgence. The color also helps distinguish its products and adds a sense of premium quality.

- **Use scientific palettes**:
  - **Analogous**: harmonious, side-by-side colors on the color wheel.
  <img src="analogous-wheel.jpg" alt="analogous palettes" width="30%" style="display: block; margin: auto;">  
  - **Complementary**: opposite on the wheel—eye-catching, but best for accents, not text.
  <img src="complimentary-wheel.jpg" alt="complimentary palettes" width="30%" style="display: block; margin: auto;">   
  - **Triadic and Square palettes**: well-balanced and vibrant.
    <div style="display: flex; justify-content: center; gap: 20px;">
      <img src="triangular-wheel.jpg" alt="triangular palettes" width="30%">
      <img src="rectangular-wheel.jpg" alt="rectangular palettes" width="30%">
    </div>



- **Use professional tools**:
  - <a href="https://color.adobe.com/" target="_blank">Adobe Color</a>: for creating colour themes and transfer into content
  - <a href="https://coolors.co/" target="_blank">Coolors</a>: preset colour palets
  - <a href="https://colorhunt.co" target="_blank">Color Hunt</a>: preset colour palets

Choose color combinations that reflect your website’s purpose. A good palette makes your design feel intentional, coherent, and memorable.

---

### ✍️ Understanding Typography<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Typography guides the reader’s journey. Great typography brings clarity and mood to your content.

- **Choose readable fonts**: Prioritize legibility across all screen sizes.
- **Limit to 2–3 font families**: Too many can overwhelm and distract. 
  - <strong>Serif fonts</strong> (like <span style="font-family: 'Georgia', serif;">Georgia</span> or <span style="font-family: 'Times New Roman', serif;">Times New Roman</span>) have small decorative strokes, or "feet," at the ends of their letterforms, giving them a traditional and elegant feel often used in print.<br>
  - <strong>Sans-serif fonts</strong> (like Arial) lack these decorative strokes, offering a clean, modern, and minimalist look that is highly legible, especially on digital screens.<br>
  - The choice between them often depends on the medium (print vs. digital) and the desired mood (classic vs. modern).
- **Establish hierarchy**:
  - Use size, weight (bold vs. regular), and spacing to indicate importance.
  - Pair serif fonts (<span style="font-family: 'Georgia', serif;">classic, established</span>) with sans-serif (modern, clean) for contrast.
- **Consider your brand tone**: A <span style="font-family: 'Times New Roman', serif;">serif font</span> conveys tradition, while a bold sans-serif feels tech-forward. Use script for more <span style="font-family: 'Dancing Script', cursive;">personal</span> or <span style="font-family: 'Great Vibes', cursive;">elegant</span>. 

Design is communication—your font choices should help users absorb your message, not fight against it.

---

### 👁️ Managing Attention with UI Design<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Your users don’t read—they scan. UI design is about guiding their attention where it matters most.

#### ✅ Hierarchy
- Bigger and bolder elements get noticed first.
- Use **color contrast** and **<span style="font-size: larger;">size</span>** to show what matters—like a green "Buy Now" button on a grayscale layout.

#### 🧱 Layout
- Break up text blocks with images and whitespace.
- Ideal line length: **40–60 characters** for easy reading.
- Avoid overwhelming walls of text like those found on Wikipedia.

#### 📐 Alignment
- Align elements to create structure.
- Reduce the number of alignment points—uniformity makes your layout feel more professional.

#### 🌌 White Space
- Emptiness adds elegance. High-end designs (think Apple) use white space to suggest value and clarity.
- Don’t cram your content—let each element breathe.

#### 🧑‍🎨 Design for Your Audience
- A kids’ website should look different from a fintech site.
- Match color, layout, and font to your user’s expectations and desires.

When UI is done right, users won’t even notice it—they’ll just glide through your site happily.

---

### 💡 User Experience (UX) Design<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

UX is about **empathy**—designing with your user’s journey in mind. Ask yourself: Can users find what they need easily? Can they interact comfortably on all devices?

- **Make navigation intuitive**: Use familiar patterns like top navbars or hamburger menus.
- **Responsive design**: Your website should look great on phones, tablets, and desktops.
- **Test early and often**: Get feedback from real users. Watch how they interact, and iterate based on their behavior—not your assumptions.

Think of UX as invisible scaffolding—it’s not glamorous, but it holds your entire design together


---

## 🏁 Summary<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Today you learned:
- How the internet and websites work
- HTML structure and elements
- CSS styling and the box model
- How to use Bootstrap for fast, responsive design
- Key web design principles for beautiful, user-friendly sites

**Next Steps:** Try building a simple web page using HTML, style it with CSS, and experiment with Bootstrap components! You can speed up your design by using <a href="https://www.canva.com/" target="_blank">Canva</a> which alows you to design a website in your browser, publish it and then you can see its code. 
