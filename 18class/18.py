import pandas as pd
import numpy as np
# print(pd.DataFrame({'A': [1, 2, 3]}))

df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
}
)
print(df2)
print("-"*40)
print(df2.loc[1])
print("-"*40)
print(df2["A"])


# Hierarchical indexing (MultiIndex)


arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],

    ["one", "two", "one", "two", "one", "two", "one", "two"],
]

tuples = list(zip(*arrays))
print(tuples)
print("-"*40)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(index)
print("-"*40)

s = pd.Series(np.random.randn(8), index=index)
print(s)
print("-"*40)
print(s['bar', 'one'])
# print(s['first', 'second'])
