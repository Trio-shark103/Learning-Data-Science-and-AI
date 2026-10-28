# Casting
# Casting converts the underlying data type of a column to a new one. Casting is available through the function cast.

# The function cast includes a parameter strict that determines how Polars behaves when it encounters a value that cannot be converted from the source data type to the target data type. The default behaviour is strict=True, which means that Polars will thrown an error to notify the user of the failed conversion while also providing details on the values that couldn't be cast. On the other hand, if strict=False, any values that cannot be converted to the target data type will be quietly converted to null.


import polars as pl

df = pl.DataFrame(
    {
        "integers": [1, 2, 3],
        "big_integers": [10000002, 2, 30000003],
        "floats": [4.0, 5.8, -6.3],
    }
)

print(df)