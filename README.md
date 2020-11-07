# Resume Generator

A templated resume generator based on the schema of [JSON resume](https://jsonresume.org/). We strive to separate content from style by splitting the process of resume writing into distinct stages.

1. Write the *content* of the resume in `bin/resume.json`, adhering to the provided schema `bin/schema.json`.
2. Ensure that the *style* of the resume specified in `bin/template.tex` is desirable.
3. Convert the JSON specification into styled LaTeX through the template. This is accomplished with `create_resume.py`, which uses `Jinja2`.
4. Compile the output `resume.tex` into `resume.pdf`. I recommend using [latexmk](https://ctan.org/pkg/latexmk/) for this purpose.

The provided `Makefile` automates the last 2 steps of this process.
