import polars as pl



df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bambi", "category"]})

# writing to multiple csv files using a for loop and range
# for i in range(5):
#     df.write_csv(f"polars/data_{i}.csv")
    
    
# reading from multiple csv files into a single DataFrame.
# df = pl.read_csv(f"polars/data_*.csv")

# print(df)


# pl.scan_csv("polars/data_*.csv").show_graph(plan_stage = "ir")
# pl.scan_csv("polars/data_*.csv").show_graph(plan_stage = "physical" )



#reading and processing in parallel using glob

import glob


queries = []

for file in glob.glob("polars/data_*.csv"):
    q = pl.scan_csv(file).group_by("bar").agg(pl.len(), pl.sum("foo"))
    queries.append(q)

dataframes = pl.collect_all(queries)
print(dataframes)