from ._version import get_versions
import pandas as pd

__version__ = get_versions()['version']
del get_versions


def context(
    pdobj, loc=None, iloc=None, around=2, pre=None, post=None, method="nearest"
):
    """Slicing with a date as reference.

    Parameters
    ----------
    loc : index-like
    iloc : int
    around : int
    pre : int
    post : int
    method : str

    Returns
    -------
    out : pandas-like

    Examples
    --------
    >>> import numpy as np
    ... import pandas_context
    ... n = 1000
    ... data = np.random.randn(n)
    ... index = pd.date_range("19990101", periods=n)
    ... df = pd.DataFrame(data=data, index=index)

    >>> date = index[50]

    >>> date
    Timestamp('1999-02-20 00:00:00', freq='D')

    >>> df.context(date)
                       0
    1999-02-18  1.086181
    1999-02-19  0.174156
    1999-02-20 -0.762305
    1999-02-21 -0.110677
    1999-02-22 -0.766751

    >>> df.context(date, around=1)
                       0
    1999-02-19  0.174156
    1999-02-20 -0.762305
    1999-02-21 -0.110677

    >>> df.context(date, pre=3, post=1)
                       0
    1999-02-17 -0.809791
    1999-02-18  1.086181
    1999-02-19  0.174156
    1999-02-20 -0.762305
    1999-02-21 -0.110677
    """

    if loc is not None:
        idx = pdobj.index.get_loc(loc, method=method)
    elif iloc is not None:
        idx = iloc
    else:
        raise ValueError

    if pre is None:
        pre = around
    if post is None:
        post = around
    if pre > idx:
        pre = idx
    ini = idx - pre
    end = idx + post + 1
    return pdobj.iloc[ini:end]


pd.core.frame.NDFrame.context = context
