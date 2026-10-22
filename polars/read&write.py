#Polars supports reading and writing for common file formats (e.g., csv, json, parquet), cloud storage (S3, Azure Blob, BigQuery) and databases 
# (e.g., postgres, mysql). Below, we create a small dataframe and show how to write it to disk and read it back.
import polars as pl
import datetime as dt

df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            dt.date(1997, 1, 10),
            dt.date(1985, 2, 15),
            dt.date(1983, 3, 22),
            dt.date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)


# df.write_csv("polars/output.csv")
# df_csv = pl.read_csv("polars/output.csv", try_parse_dates=True)
# print(df_csv)


#Expressions and contexts
 #1. "select" allows you to select and manipulate columns from a dataframe.
# result = df.select(
#     pl.col("name"),
#     pl.col("birthdate").dt.year().alias("birth_year"), # alias() allows you to rename the column in the output
#     (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
# )
# print(result)


# with "with_columns" you can add new columns to a dataframe. The new columns can be derived from existing columns.

result = df.with_columns(
    birth_year=pl.col("birthdate").dt.year(),
    bmi=pl.col("weight") / (pl.col("height") ** 2),
)
print(result)