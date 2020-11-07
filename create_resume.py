"""
Render resume JSON into LaTeX.

Copyright 2020. Siwei Wang.
"""
from os import path
from json import load
from jsonschema import validate  # type: ignore
from jinja2 import Environment, FileSystemLoader, Template


def get_resume(resume_path: str, schema_path: str) -> dict:
    """Load and validate resume with schema."""
    with open(path.join('bin', resume_path)) as res_fp:
        resume = load(res_fp)
    assert isinstance(resume, dict), 'Resume JSON must be object.'
    with open(path.join('bin', schema_path)) as sch_fp:
        schema = load(sch_fp)
    validate(resume, schema)
    return resume


def get_template(template_path: str) -> Template:
    """Create environment and get template."""
    env = Environment(
        block_start_string=r'\BLOCK{',
        block_end_string=r'}',
        variable_start_string=r'\VAR{',
        variable_end_string=r'}',
        comment_start_string=r'\#{',
        comment_end_string=r'}',
        line_statement_prefix=r'%%',
        line_comment_prefix=r'%#',
        trim_blocks=True,
        autoescape=False,
        loader=FileSystemLoader('bin')
    )
    return env.get_template(template_path)


def main():
    """Render resume JSON into LaTeX."""
    resume = get_resume('resume.json', 'schema.json')
    template = get_template('template.tex')
    template.stream(resume).dump('resume.tex')


if __name__ == '__main__':
    main()
