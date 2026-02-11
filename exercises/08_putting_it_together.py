# ============================================================
# Exercise 08: Putting It All Together
# ============================================================
# Dataset: ../data/06_store_weekly.csv
#
# This is the final exercise. It uses a bigger dataset with
# a full week of sales for a clothing/accessories shop.
# The data has one missing value and one zero-sale row.
#
# You will combine everything you have learned:
#   - Loading and inspecting
#   - Dates
#   - New columns
#   - Filtering
#   - Groupby
#   - Cleaning
#   - Sorting
#
# Take it step by step. Check your output after each question.
# ============================================================

import pandas as pd

df = pd.read_csv("../data/06_store_weekly.csv")


# ---- Q1 ----
# Print the shape of the data and the first 5 rows.

# YOUR CODE HERE


# ---- Q2 ----
# Check for missing values in each column.

# YOUR CODE HERE


# ---- Q3 ----
# Convert the "date" column to datetime format.
# The dates are in DD/MM/YYYY format. Use errors="coerce".

# YOUR CODE HERE


# ---- Q4 ----
# Check for missing values again (the date conversion might
# have created new NaT values if any dates were bad).
# Then drop any rows with missing values.
# Store the clean data back into df.
# Print the new shape.

# YOUR CODE HERE


# ---- Q5 ----
# Create three new columns:
#   "revenue" = sell_price * qty_sold
#   "cost"    = cost_price * qty_sold
#   "profit"  = revenue - cost
# Print the first 5 rows showing all columns.

# YOUR CODE HERE


# ---- Q6 ----
# What is the total revenue for the entire week?
# Print just the number.

# YOUR CODE HERE


# ---- Q7 ----
# What is the total revenue for EACH category?
# Group by category, sum revenue, and print the result.

# YOUR CODE HERE


# ---- Q8 ----
# What is the total profit for each product_id?
# Group by product_id, sum profit, then sort by profit
# from highest to lowest.
# Print the result.

# YOUR CODE HERE


# ---- Q9 ----
# Show daily revenue trends:
# Group by date, sum revenue, sort by date.
# Print the result. This is what you would use to draw
# a line chart of revenue over time.

# YOUR CODE HERE


# ---- Q10 ----
# Filter to only "Footwear" items.
# Use .copy() to make a safe copy.
# Then group the footwear data by date and sum the qty_sold.
# Sort by date and print.

# YOUR CODE HERE


# ---- Q11 ----
# Which single day had the highest total profit across
# ALL products? Print the date and the profit amount.
# (Hint: group by date, sum profit, sort descending, head(1))

# YOUR CODE HERE
