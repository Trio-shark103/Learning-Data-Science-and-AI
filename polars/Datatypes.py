from datetime import date
import polars as pl

df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            date(1997, 1, 10),
            date(1985, 2, 15),
            date(1983, 3, 22),
            date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)

#---HEAD-----
print(df.head(3))# print the first 3 rows of the DataFrame

# ---GLIMPSE-----
print(df.glimpse(return_type="string"))# print a summary glimpse of the DataFrame in string format
print(df.glimpse(return_type="frame"))# print a summary glimpse of the DataFrame in DataFrame format    
print(df.glimpse(return_type="self"))# print a summary glimpse of the DataFrame in self format


# ---TAIL-----
print(df.tail(3))# print the last 3 rows of the DataFrame

# ---SAMPLE-----
pl.set_random_seed(42)  # For reproducibility.

print(df.sample(2))

#--Describe the DataFrame--
#compute summary statistics for all columns of your dataframe
print(df.describe())