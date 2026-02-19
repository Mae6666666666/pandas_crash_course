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
print(df["total_cost"])

# ---- Q3 ----
# What is the total of ALL orders combined?
# Print just the number.
# (Hint: use .sum() on your new column)

# YOUR CODE HERE
total_all_orders = new_column.sum() 
print(total_all_orders)

# ---- Q4 ----
# Create another new column called "vat" which is 20% of the total_cost.
(Hint: multiply total_cost by 0.2)

# YOUR CODE HERE
vat = df["vat"] = df["total_cost"] * 0.2
print(vat)

# ---- Q5 ----
# Create a column called "total_with_vat" which is total_cost + vat.
# Print the DataFrame to see all your new columns.

# YOUR CODE HERE
total_with_vat = df["total_with_vat"] = df["total_cost"] + df["vat"]
print(total_with_vat)

# ---- Q6 ----
# What is the average order value (mean of total_cost)?
# Print the number.

# YOUR CODE HERE
average_oder_value = df["total_cost"].mean()
print(average_oder_value)

# ---- Q7 ----
# What is the most expensive single order (max of total_cost)?
# And the cheapest (min)?
# Print both.

# YOUR CODE HERE
most_expensive_order = df["total_cost"].max()
cheapest_order = df["total_cost"].min()
print(most_expensive_order)
print(cheapest_order)
