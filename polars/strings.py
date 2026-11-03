import polars as pl

df = pl.DataFrame(
    {
        "language": ["English", "Dutch", "Portuguese", "Finish"],
        "fruit": ["pear", "peer", "pêra", "päärynä"],
    }
)

result = df.with_columns(
    pl.col("fruit").str.len_bytes().alias("byte_count"),
    pl.col("fruit").str.len_chars().alias("letter_count"),
)
# print(result)

result = df.select(
    pl.col("fruit"),
    pl.col("fruit").str.starts_with("p").alias("starts_with_p"),
    pl.col("fruit").str.contains("p..r").alias("p..r"),
    pl.col("fruit").str.contains("e+").alias("e+"),
    pl.col("fruit").str.ends_with("r").alias("ends_with_r"),
)
print(result)

#parsing strings to date/datetime
result = df.select(
    pl.col("fruit"),
    pl.col("fruit").str.starts_with("p").alias("starts_with_p"),
    pl.col("fruit").str.contains("p..r").alias("p..r"),
    pl.col("fruit").str.contains("e+").alias("e+"),
    pl.col("fruit").str.ends_with("r").alias("ends_with_r"),
)
# print(result)


# Regex specification
df = pl.DataFrame(
    {
        "urls": [
            "http://vote.com/ballon_dor?candidate=messi&ref=polars",
            "http://vote.com/ballon_dor?candidat=jorginho&ref=polars",
            "http://vote.com/ballon_dor?candidate=ronaldo&ref=polars",
        ]
    }
)
result = df.select(
    pl.col("urls").str.extract(r"candidate=(\w+)", group_index=1),
)
print(result)