"""Development script for the pandas-sphinx package."""

import tarfile
from zipfile import ZipFile

import pandas as pd

from pandas_sphinx import __version__, to_sphinx

if __name__ == "__main__":
    print(__version__)

    # Source: https://github.com/gregbanks/python-tabulate#readme
    df = pd.DataFrame(
        [["spam", 42], ["eggs", 451], ["bacon", 0]], columns=["item", "qty"]
    )

    print(df.to_markdown(tablefmt="grid"))

    formatted_df = to_sphinx(df)

    print(formatted_df)
    print(repr(formatted_df))
    print(type(formatted_df))

    # Source:
    # - https://stackoverflow.com/a/32924572
    # - https://docs.python.org/3.7/library/zipfile.html#zipfile.ZipFile.open
    whl_path = f"dist/pandas_sphinx-{__version__}-py3-none-any.whl"
    with ZipFile(whl_path) as myzip:
        whl_names = myzip.namelist()
    print("\nwheel:", *whl_names, sep="\n")

    # Source:
    # - https://stackoverflow.com/a/19667113
    # - https://docs.python.org/3.7/library/tarfile.html
    sdist_path = f"dist/pandas_sphinx-{__version__}.tar.gz"
    with tarfile.open(sdist_path, "r") as tar:
        sdist_names = tar.getnames()
    print("\nsdist:", *sdist_names, sep="\n")
