from ._version import get_versions
import pandas as pd

__version__ = get_versions()['version']
del get_versions


def context(
    pdobj, loc=None, iloc=None, around=2, pre=None, post=None, method="nearest"
):

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
