# ============================================================
# Exercise 04: Creating New Columns from Calculations
# ============================================================
# Dataset: ../data/03_orders.csv (same as exercise 03)
#
# You will practice creating new columns by doing maths
# on existing columns. This is how you calculate things like
# revenue, cost, and profit.
# ============================================================

import pandas as pd

df = pd.read_csv("data/03_orders.csv")


# ---- Q1 ----
# Create a new column called "total_cost" that is quantity * unit_price.
# Then print the whole DataFrame to see your new column.

# YOUR CODE HERE
new_column = df["total_cost"] = df["quantity"] * df["unit_price"]
print(new_column)

# ---- Q2 ----
# Print the total_cost column on its own.

# YOUR CODE HERE


# ---- Q3 ----
# What is the total of ALL orders combined?
# Print just the number.
# (Hint: use .sum() on your new column)

# YOUR CODE HERE


# ---- Q4 ----
# Create another new column called "vat" which is 20% of the total_cost.
# (Hint: multiply total_cost by 0.2)

# YOUR CODE HERE


# ---- Q5 ----
# Create a column called "total_with_vat" which is total_cost + vat.
# Print the DataFrame to see all your new columns.

# YOUR CODE HERE


# ---- Q6 ----
# What is the average order value (mean of total_cost)?
# Print the number.

# YOUR CODE HERE


# ---- Q7 ----
# What is the most expensive single order (max of total_cost)?
# And the cheapest (min)?
# Print both.

# YOUR CODE HERE
