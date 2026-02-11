# ============================================================
# Exercise 05: Grouping Data and Calculating Totals
# ============================================================
# Dataset: ../data/05_electronics.csv
#
# This dataset has daily sales for an electronics shop over
# 6 days, with 5 products across 4 categories. You will
# practice using groupby to get totals per category, per
# product, and per day.
#
# groupby is one of the MOST important pandas operations.
# Take your time on this one.
# ============================================================

import pandas as pd

df = pd.read_csv("../data/05_electronics.csv")


# ---- Q1 ----
# Print the unique categories in the dataset.

# YOUR CODE HERE


# ---- Q2 ----
# What is the total qty_sold for the ENTIRE dataset?
# Print just the number.

# YOUR CODE HERE


# ---- Q3 ----
# What is the total qty_sold for EACH category?
# Use groupby to group by "category" and sum the "qty_sold".
# Use as_index=False so the result looks like a normal table.

# YOUR CODE HERE


# ---- Q4 ----
# What is the total qty_sold for EACH product_id?
# Group by "product_id" and sum "qty_sold".

# YOUR CODE HERE


# ---- Q5 ----
# Now get the total qty_sold for each product on EACH day.
# (Hint: you can group by two columns at once using a list:
#  df.groupby(["date", "product_id"], as_index=False) )

# YOUR CODE HERE


# ---- Q6 ----
# Create two new columns first:
#   "revenue" = sell_price * qty_sold
#   "cost"    = cost_price * qty_sold
# Then group by "category" and get the TOTAL revenue and cost
# for each category.
# Print the result.

# YOUR CODE HERE


# ---- Q7 ----
# Using the same revenue and cost columns from Q6,
# create a "profit" column (revenue - cost).
# Then group by "category" and get the total profit per category.
# Print the result.

# YOUR CODE HERE
