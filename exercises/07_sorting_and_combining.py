# ============================================================
# Exercise 07: Sorting Data and Chaining Operations
# ============================================================
# Dataset: ../data/05_electronics.csv
#
# You will practice sorting data and combining multiple
# pandas operations together in sequence.
# ============================================================

import pandas as pd

df = pd.read_csv("../data/05_electronics.csv")


# ---- Q1 ----
# Sort the DataFrame by qty_sold from smallest to largest.
# Print the first 5 rows.

# YOUR CODE HERE


# ---- Q2 ----
# Sort by qty_sold from LARGEST to smallest.
# Print the first 5 rows.

# YOUR CODE HERE


# ---- Q3 ----
# Sort by category first, then by qty_sold (largest first).
# Print the result.
# (Hint: sort_values can take a list of columns and a list
#  of ascending values:
#  df.sort_values(["col1", "col2"], ascending=[True, False]) )

# YOUR CODE HERE


# ---- Q4 ----
# Chain it together: create revenue and profit columns, group
# by category, sum them, then sort by profit largest first.
# Do this step by step:
#   1. df["revenue"] = sell_price * qty_sold
#   2. df["profit"] = revenue - (cost_price * qty_sold)
#   3. group by category, sum revenue and profit
#   4. sort the result by profit, descending
# Print the final result.

# YOUR CODE HERE


# ---- Q5 ----
# Which single product_id had the highest total qty_sold
# across all 6 days?
# Steps:
#   1. Group by product_id, sum qty_sold
#   2. Sort by qty_sold descending
#   3. Print the first row
# (Hint: after sort, use .head(1) to get just the top row)

# YOUR CODE HERE


# ---- Q6 ----
# Convert the date column to datetime, then sort the whole
# DataFrame by date.
# Print the first 10 rows to confirm it is in date order.

# YOUR CODE HERE
