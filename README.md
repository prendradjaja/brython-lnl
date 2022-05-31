## What and why?
- Example of using Python in the browser using [Brython](https://brython.info/)
- Not something I'd necessarily recommend using in production, but it's cool!
- I occasionally use it for personal projects
- Use Python's standard library + JS's DOM API (.appendChild(), etc)!
- If you like vanilla JS and you like Python's standard library, you might like this.


## Also
- There are other python-in-browser projects and similar. I know nothing about them, but in no particular order here are some: PyScript, Transcrypt, Pyjs, Pyodide
- How does it work?
  - https://github.com/brython-dev/brython/wiki/How%20Brython%20works (linked from [Brython's readme](https://brython.info/))
  - tldr: On load, `brython()` (part of `brython.js`) looks for all script tags with `text/python` and compiles Python to JS.
