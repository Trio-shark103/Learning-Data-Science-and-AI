import polars as pl

df = pl.read_csv("polars/output.csv") # read_csv() reads a CSV file into a Polars DataFrame. The try_parse_dates=True argument attempts to parse date columns automatically.
df_small = df.filter(pl.col("weight") > 5)
df_agg = df_small.group_by("weight").agg(pl.col("height").mean())
print(df_agg)


q = (
    pl.scan_csv("polars/output.csv")
    .filter(pl.col("weight") > 5)
    .group_by("weight")
    .agg(pl.col("height").mean())
)

df = q.collect()
print(df)
print(q.explain())

schema = pl.Schema(
    {
        "int_1": pl.Int16,
        "int_2": pl.Int32,
        "float_1": pl.Float64,
        "float_2": pl.Float64,
        "float_3": pl.Float64,
    }
)

print(
    pl.LazyFrame(schema=schema)
    .select((pl.col(pl.Float64) * 1.1).name.suffix("*1.1"))
    .explain()
)