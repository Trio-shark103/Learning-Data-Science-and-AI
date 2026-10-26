# Streaming
# One additional benefit of the lazy API is that it allows queries to be executed in a streaming manner. Instead of processing all the data at once, Polars can execute the query in batches allowing you to process datasets that do not fit in memory. Besides memory pressure, the streaming engine also is more performant than Polars' in-memory engine.

# To tell Polars we want to execute a query in streaming mode we pass the engine="streaming" argument to collect:


import polars as pl

q1 = (
    pl.scan_csv("docs/assets/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .group_by("species")
    .agg(pl.col("sepal_width").mean())
)
df = q1.collect(engine="streaming")