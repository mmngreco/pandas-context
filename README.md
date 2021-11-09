# pandas-context

Provides context to your data, allow you to made complex slicing around a
specific index.

Here's an example:

```python
import pandas as pd
import numpy as np

n = 1000
data = np.random.randn(n)
index = pd.date_range("19990101", periods=n)
df = pd.DataFrame(data=data, index=index)
df.context(index[50])
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

