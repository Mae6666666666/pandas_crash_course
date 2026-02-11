# ============================================================
# Exercise 03: Working with Dates and Date Ranges
# ============================================================
# Dataset: ../data/03_orders.csv
#
# This dataset has 12 orders from a stationery shop.
# Dates are in DD/MM/YYYY format. You will practice converting
# text dates into proper dates and filtering by date range.
# ============================================================

import pandas as pd

df = pd.read_csv("data/03_orders.csv")


# ---- Q1 ----
# Print the data types of all columns.
# Notice that the "date" column shows as "object" -- that means
# pandas thinks it is just text, not a real date.

# YOUR CODE HERE
# print(df.dtypes)

# ---- Q2 ----
# Convert the "date" column to a proper datetime.
# The dates are in DD/MM/YYYY format.
# Store the result back into df["date"].
# Then print df.dtypes again to confirm it changed.

# YOUR CODE HERE
# print(pd.to_datetime(df["date"], format="%d/%m/%Y"))


# ---- Q3 ----
# Print all orders from BEFORE 15/01/2025.
# (Hint: filter where df["date"] < pd.to_datetime("15/01/2025", format="%d/%m/%Y"))

# YOUR CODE HERE
# THIS IS WRONG:

# left_side = pd.to_datetime(df["date"], format="%d/%m/%Y")
# right_side =  pd.to_datetime("15/01/2025", format="%d/%m/%Y")
# filter =  left_side < right_side
# orders = df.loc[filter]
# print(orders)

# ---- Q4 ----
# Print all orders between 10/01/2025 and 20/01/2025 (inclusive).
# (Hint: you need two conditions joined with &)

# YOUR CODE HERE

my_format = "%d/%m/%Y"
# all the dates from the csv file
first_left = pd.to_datetime(df["date"], format=my_format)
# gets the 10/01/25 date
first_right = pd.to_datetime("10/01/2025", format=my_format)
# gets all the dates in the csv again
second_left = pd.to_datetime(df["date"], format=my_format)
# gets the dat with the 20/1/25
second_right = pd.to_datetime("20/01/2025", format=my_format)
# gets the dates that are higher than 10/01/25
filter1 = first_left > first_right
# gets the dates that are lower than 20/01/25
filter2 = second_left < second_right
# combines the middle point to get between 10/01/25 and 20/01/25
merged_filters = filter1 & filter2
# locate the merged filter and print it out
print(df.loc[merged_filters])





# ---- Q5 ----
# Print all orders that customer "Sam" made between 10/01/2025 and 20/01/2025 (inclusive).
# (Hint: you need the date range filter AND a customer filter)

# YOUR CODE HERE


# ---- Q6 ----
# How many orders did "Kim" place in total?
# Print just the number.
# (Hint: filter for Kim first, then use .shape[0] to count rows)

# YOUR CODE HERE
