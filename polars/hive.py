import polars as pl 

df = pl.scan_parquet("polars/Hive/").collect


with pl.Config(tbl_rows = 99):
    print(df)