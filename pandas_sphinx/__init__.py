"""pandas-sphinx: render a pandas DataFrame as an opinionated table for Sphinx."""

from .constants import DATA_ROW_SEP, ELLIPSIS, LINE_SEP
from .version import __version__


def to_sphinx(df, show_index=False, number_rows=1):
    """Convert a pandas DataFrame into a Sphinx-based table ready to be added to a docstring.

    Parameters
    ----------
    df : pandas.DataFrame
        The pandas DataFrame to be converted into a Sphinx-based table.
    show_index : bool, default False
        Include the pandas DataFrame index in the output table (``True``) or not (``False``).
    number_rows : int, default 1
        The number of top rows of the pandas DataFrame to consider for the output table.

    Returns
    -------
    str
        The Sphinx-based table ready to be added to a docstring.
    """
    formatted_df = df.head(number_rows).to_markdown(tablefmt="grid", index=show_index)

    # https://github.com/gregbanks/python-tabulate/blob/master/tabulate.py#L132
    line = formatted_df.split("\n")[0]

    col_sizes = [len(col) for col in line.split(LINE_SEP) if col]
    new_cols = [f" {ELLIPSIS}".ljust(col_size) for col_size in col_sizes]

    new_data_row = f"{DATA_ROW_SEP}{DATA_ROW_SEP.join(new_cols)}{DATA_ROW_SEP}\n{line}"

    return f"{formatted_df}\n{new_data_row}"
