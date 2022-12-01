# pandas-sphinx

[![PyPI](https://img.shields.io/pypi/v/pandas-sphinx)](https://pypi.org/project/pandas-sphinx/)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Documentation Coverage](https://raw.githubusercontent.com/joaopalmeiro/pandas-sphinx/main/assets/interrogate_badge.svg)](https://github.com/econchick/interrogate)

Render a [pandas](https://pandas.pydata.org/) DataFrame as an opinionated table for [Sphinx](https://www.sphinx-doc.org/).

- **Documentation**: https://joaopalmeiro.github.io/pandas-sphinx/
- **Source code**: https://github.com/joaopalmeiro/pandas-sphinx
- **Python package**: https://pypi.org/project/pandas-sphinx/

## References

- https://github.com/yehoshuadimarsky/bcpandas#quickstart
- https://github.com/yehoshuadimarsky/bcpandas/blob/master/bcpandas/main.py#L309
- https://github.com/Zsailer/pandas_flavor
- Sphinx:
  - https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables
  - https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks
  - https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block
  - https://pygments.org/docs/lexers/#lexers-for-various-shells
  - https://raw.githubusercontent.com/readthedocs/sphinx_rtd_theme/master/docs/index.rst
- https://github.com/astanin/python-tabulate#table-format
- https://en.wikipedia.org/wiki/Ellipsis
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html
- https://github.com/pandas-dev/pandas/blob/v1.1.0/pandas/core/frame.py#L2240
- https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_markdown.html
- https://github.com/koaning/scikit-bloom/blob/main/setup.py
- https://github.com/scikit-hep/cookie
- Documentation:
  - https://numpydoc.readthedocs.io/en/stable/format.html + https://numpydoc.readthedocs.io/en/stable/example.html
  - https://cjolowicz.github.io/posts/hypermodern-python-05-documentation/
  - https://cjolowicz.github.io/posts/hypermodern-python-06-ci-cd/
  - https://nashpy.readthedocs.io/en/stable/contributing/discussion/darglint/index.html

## Notes

- https://hatch.pypa.io/latest/install/: `brew update` + `brew install hatch` + `hatch --version`
- Tabulate:
  - The minimum column size is 2 (+ 2 padding spaces): https://github.com/gregbanks/python-tabulate/blob/master/tabulate.py#L791
  - https://github.com/gregbanks/python-tabulate/blob/master/tabulate.py#L132
- Hatch:
  - `hatch new --init`
  - `hatch env create` (`default` environment) + `hatch shell` + `pip show pandas-sphinx` + `pip list`
  - `hatch env remove` or `hatch env remove format`
  - `hatch env create format`
  - `hatch run format:i` + `hatch run format:b`
  - `hatch env prune`
  - `hatch env show`
  - `hatch shell` + `python dev.py` + `exit` or `hatch run python dev.py`
  - `hatch version minor` or `hatch version patch`
  - `hatch version`
  - `hatch run lint:i` + `hatch run lint:ib` + `hatch run lint:d`
  - `hatch -e lint run darglint --help`
  - `rm -rf dist/` + `hatch build`
  - `hatch publish --help`
  - `hatch env create docs`
  - `hatch run docs:check`
  - `hatch -e format run rstfmt --help`
  - `hatch run docs:build` + `hatch run docs:open`
  - `hatch run docs:clean`
  - `hatch run docs:clean && hatch run docs:build && hatch run docs:open`
- https://pycqa.github.io/isort/docs/configuration/black_compatibility.html
- Check if docstrings exist with [interrogate](https://github.com/econchick/interrogate), check their format with [darglint](https://github.com/terrencepreilly/darglint)
