# pandas-sphinx

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

Render a [pandas](https://pandas.pydata.org/) DataFrame as an opinionated table for [Sphinx](https://www.sphinx-doc.org/).

## References

- https://github.com/yehoshuadimarsky/bcpandas#quickstart
- https://github.com/yehoshuadimarsky/bcpandas/blob/master/bcpandas/main.py#L309
- https://github.com/Zsailer/pandas_flavor
- https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables
- https://github.com/astanin/python-tabulate#table-format
- https://en.wikipedia.org/wiki/Ellipsis
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html
- https://github.com/pandas-dev/pandas/blob/v1.1.0/pandas/core/frame.py#L2240
- https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_markdown.html

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
  - `hatch shell` + `python dev.py` + `exit`
  - `hatch version minor` or `hatch version patch`
- https://pycqa.github.io/isort/docs/configuration/black_compatibility.html
