# Richard's Cookiecutter Data Science project

- ✅ Complex pipeline support
- ✅ Newest packaging guidelines
- ✅ Publishing and linting

## Quickstart

TODO check these commands lol

```
pipx install cookiecutter # OR
uvx install cookiecutter # OR
# Just have installed cookiecutter

cookiecutter https://github.com/richard-hajek/cookiecutter-richards-datascience 
```

## Notes

This template is aimed at data science projects, ie minimal support for tests, minimal support for typing, highest support for conda, uv, pypi, semi-complex data pipelines.

This project (by itself) does not support
- dev contains
- Docker deployment

Note that it would not be difficult to support these. It just. Isn't nececssary. 

This project is opinionated
- Uses `uv`
- Uses `ruff`

However usage of `uv` and `ruff` is not rooted in affection towards Astral and I **will** jump ship the second Astral does any bullshit.
