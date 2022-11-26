import pandas as pd

from pandas_sphinx import __version__, to_sphinx

if __name__ == "__main__":
    print(__version__)

    # Source: https://github.com/gregbanks/python-tabulate#readme
    df = pd.DataFrame(
        [["spam", 42], ["eggs", 451], ["bacon", 0]], columns=["item", "qty"]
    )

    formatted_df = to_sphinx(df)

    print(formatted_df)
    print(repr(formatted_df))
    print(type(formatted_df))
