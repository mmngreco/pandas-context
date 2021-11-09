import pandas as pd
import pandas_context  # noqa


def test_dataframe_has_context():
    assert hasattr(pd.DataFrame, "context")


def test_series_has_context():
    assert hasattr(pd.Series, "context")


def test_around():
    s = pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5])
    obtained = s.context(3, around=2)
    expected = pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5])
    pd.testing.assert_series_equal(obtained, expected)


def test_pre_post():
    s = pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5])
    obtained = s.context(3, pre=2, post=1)
    expected = pd.Series([1, 2, 3, 4], index=[1, 2, 3, 4])
    pd.testing.assert_series_equal(obtained, expected)
