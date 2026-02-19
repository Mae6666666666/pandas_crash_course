# ============================================================
# Exercise 06: Cleaning Messy Data
# ============================================================
# Dataset: ../data/04_shop_sales.csv
#
# This dataset has PROBLEMS on purpose:
#   - Some rows have missing values (blank cells)
#   - One row has an impossible date (32/03/2025)
#   - One row has qty_sold of 0
#
# In the real world (and in your T Level tasks) data is
# messy. You need to know how to find and handle problems.
# ============================================================

import pandas as pd

df = pd.read_csv("data/04_shop_sales.csv")


# ---- Q1 ----
# Print the whole DataFrame to see the data.
# Can you spot anything that looks wrong?

# YOUR CODE HERE
# print(df)

# ---- Q2 ----
# Use .isnull().sum() to find out how many missing values
# each column has. Print the result.

# YOUR CODE HERE
# print(df.isnull().sum())

# ---- Q3 ----
# Print the data types. Notice that "date" is still "object"
# (text). We need to convert it.

# YOUR CODE HERE
# print(df.dtypes)

# ---- Q4 ----
# Convert the "date" column to datetime using errors="coerce".
# This will turn bad dates (like 32/03/2025) into NaT instead
# of crashing the program.
# Then print df["date"] to see which row became NaT.

# YOUR CODE HERE
my_format = "%d/%m/%Y"
df["date"] = pd.to_datetime(df["date"], format=my_format, errors="coerce")
print(df["date"])
# ---- Q5 ----
# Now use .isnull().sum() again. You should see that "date"
# now has 1 missing value (the bad date we converted to NaT).

# YOUR CODE HERE


# ---- Q6 ----
# Drop all rows that have ANY missing data.
# Store the cleaned data in a new variable called df_clean.
# Print df_clean.shape to see how many rows are left.
# (Compare to the original df.shape)

# YOUR CODE HERE
df_clean = df.dropna()
# print(df_clean)
# print(df_clean.shape)

# ---- Q7 ----
# Alternative approach: instead of dropping ALL rows with
# missing data, drop only rows where "qty_sold" is missing.
# Start from the original df again (not df_clean).
# Use .dropna(subset=["qty_sold"])
# Print the shape.

# YOUR CODE HERE
df_less_clean = df.dropna(subset=["qty_sold"])
print(df_less_clean.shape)

# ---- Q8 ----
# When you filter a DataFrame and then want to change it,
# you should use .copy() to avoid warnings.
# Filter df_clean to only show "Computing" items.
# Use .copy() at the end.
# Store it in a variable called computing_items and print it.

# YOUR CODE HERE
computing_items = df_clean.loc[df["cost_price"] =="Computing"].copy()
print(computing_items)