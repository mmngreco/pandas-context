# pandas-context

Provides context to your data, allowing you to make complex slicing around a
specific index.

Here's an example:

```python
>>> import pandas as pd
... import numpy as np
... import pandas_context
... n = 1000   # long data
... data = np.random.randn(n)
... index = pd.date_range("19990101", periods=n)
... df = pd.DataFrame(data=data, index=index)
... date = index[50]

>>> date
Timestamp('1999-02-20 00:00:00', freq='D')

>>> df.context(date)
                   0
1999-02-18  1.086181
1999-02-19  0.174156
1999-02-20 -0.762305  # <-----
1999-02-21 -0.110677
1999-02-22 -0.766751

>>> df.context(date, around=1)
                   0
1999-02-19  0.174156
1999-02-20 -0.762305  # <-----
1999-02-21 -0.110677

>>> df.context(date, pre=3, post=1)
                   0
1999-02-17 -0.809791
1999-02-18  1.086181
1999-02-19  0.174156
1999-02-20 -0.762305  # <-----
1999-02-21 -0.110677

```

## Installation

```bash
pip install git+https://github.com/mmngreco/pandas-context
```

### Developers

```bash
git clone https://github.com/mmngreco/pandas-context
pip install -e ./pandas-context
```
