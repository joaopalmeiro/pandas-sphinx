"""Sphinx configuration for documentation."""

from pandas_sphinx import __version__

# https://github.com/cjolowicz/cookiecutter-hypermodern-python/blob/main/%7B%7Bcookiecutter.project_name%7D%7D/docs/conf.py
# https://cjolowicz.github.io/posts/hypermodern-python-05-documentation/#creating-documentation-with-sphinx

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "pandas-sphinx"
author = "João Palmeiro"
copyright = f"2022, {author}"
version = __version__
release = __version__

extensions = [
    # https://www.sphinx-doc.org/en/master/usage/extensions/duration.html
    "sphinx.ext.duration",
    # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
    "sphinx.ext.autodoc",
    # https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
    "sphinx.ext.napoleon",
    # https://github.com/executablebooks/sphinx-copybutton
    "sphinx_copybutton",
]

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization
language = "en"

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://github.com/readthedocs/sphinx_rtd_theme
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# https://github.com/readthedocs/sphinx_rtd_theme/issues/529
# https://stackoverflow.com/a/62904217
html_theme = "sphinx_rtd_theme"
html_context = {
    "display_github": True,
    "github_user": "joaopalmeiro",
    "github_repo": "pandas-sphinx",
    "github_version": "main/docs/",
}

# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_google_docstring = False
napoleon_numpy_docstring = True

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
# autodoc_member_order = "bysource"
