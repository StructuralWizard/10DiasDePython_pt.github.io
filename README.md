# 10 Days of Code with AI

This repository contains the course notes and code examples of the course [10 Days of Python with AI]. The course is aimed for curious Vibe coders with no programming background who want to have a wholistic view of coding and ai technologies and the skills to debug, specify and scrutinise code that is mainly produced with AI. 

The course is mainly produce to use [Visual Studio Code] and [Github Copilot]; and a big part of it uses python for automatization, API calls, web programming, AI programming and more. 

The course notes themselves may be found in [10 Days of Code with AI course notes] and the code examples in [git hub code examples]. Once [Visual Studio Code] and [python] are installed in your machine, you can run the examples by simply typing in your terminal: 

```python
python <filename>.py
```

## Cloning the Repository

If you wish you could install git on your vs code and clone this repository in your local machine.

### Installing Bash in Visual Studio Code

If you're on Windows and want to use Bash in VS Code, you can install [Git for Windows](https://git-scm.com/download/win), which includes Git Bash.

1. Download and install Git for Windows.
2. After installation, open VS Code.
3. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and type `Terminal: Select Default Profile`.
4. Choose `Git Bash` from the list.

Now, when you open a new terminal in VS Code, it will use Bash.

> **Note:** Installing Git for Windows will also install Git Bash. You do not need to install Git separately—Git Bash is included as part of the Git installation package.

### Create a virtual environmenta and activate
A **virtual environment** in Python is an isolated workspace that allows you to install and manage packages separately from your global Python installation. This means each project can have its own dependencies, versions, and settings without interfering with other projects or the system Python.

**Why use a virtual environment?**

- Isolation: Keeps project dependencies separate, avoiding conflicts between packages required by different projects.
- Reproducibility: Makes it easier to share your project with others, since you can specify exactly which packages and versions are needed.
Safety: Prevents accidental changes to system-wide Python packages.

Typical workflow:
- Create a virtual environment for your project.
- Activate it before working.
- Install packages using pip—these go only into the virtual environment.
- Deactivate when done.

This approach is especially useful in collaborative or production settings, ensuring consistency and minimizing dependency issues.

To create a Python virtual environment, run the following command in your terminal:

```bash
python -m venv venv
```

This will create a new directory called `venv` containing the virtual environment.

To activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux/bash terminal:
  ```bash
  source venv/bin/activate
  ```

Once activated, you can install packages using `pip` and they will be isolated to this environment.

To deactivate the Python virtual environment, simply run:

```bash
deactivate
```

This will return your terminal to the global Python environment.


### Clone this repository

To clone this repository to your local machine, open your terminal and run:

```bash
git clone https://github.com/StructuralWizard/10DaysOfCode.github.io.git
```

This will create a local copy of the repository in your current directory.

### Install the dependencies of this repository
To install the dependencies listed in `requirements.txt`, make sure your virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```

This will install all the required Python packages for the project.

### Run site in local server
This site has been created using [Just the Docs] theme and the hosted in [GitHub Pages]. You can [Browse our documentation] for more information.

To visualise the github site in the browser rather than editing its markdown you can run `bundle exec jekyll serve` from the main 10DaysOfCode folder where you have the _config.yml file.

Assuming [Jekyll] and [Bundler] are installed on your computer:

1.  Change your working directory to the root directory of your site.

2.  Run `bundle install`.

3.  Run `bundle exec jekyll serve` to build your site and preview it at `localhost:4000`.

    The built site is stored in the directory `_site`.


Note: If you are using a Jekyll version less than 3.5.0, use the `gems` key instead of `plugins`.



----

[Visual Studio Code]: https://code.visualstudio.com/
[Github Copilot]: https://code.visualstudio.com/docs/copilot/overview
[python]: https://www.python.org/downloads/
[Jekyll]: https://jekyllrb.com
[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[Bundler]: https://bundler.io
[10 Days of Python with AI]: https://youtube.com/@10daysofpythonwithai?si=3wobcw1e11B7dlZI
[Structural Wizard]: https://github.com/StructuralWizard/ 
[10 Days of Code with AI course notes]: https://structuralwizard.github.io/10DaysOfCode.github.io/
[git hub code examples]: https://github.com/StructuralWizard/10DaysOfCode.github.io/tree/main/_python_code
