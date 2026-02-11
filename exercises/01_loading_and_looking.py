# ============================================================
# Exercise 01: Loading and Looking at Data
# ============================================================
# Dataset: ../data/01_fruits.csv
#
# This is a tiny dataset of 5 fruits with their colour and price.
# The goal here is just to get comfortable loading a CSV file
# and using a few commands to look at what is inside it.
#
# For each question, write your code underneath the comment.
# Run this file to check your answers: python 01_loading_and_looking.py
# ============================================================

import pandas as pd

# First, load the CSV file into a variable called df
# The file is at: ../data/01_fruits.csv

# YOUR CODE HERE
df = pd.read_csv("data/01_fruits.csv")

# ---- Q1 ----
# Print the WHOLE DataFrame so you can see all the data.
# (Hint: just print the variable)


# YOUR CODE HERE
print(df)

# ---- Q2 ----
# Print only the FIRST 3 rows of the DataFrame.
# (Hint: check the primer under "Looking at Your Data")

# YOUR CODE HERE
print(df.head(3))


# ---- Q3 ----
# Print how many rows and columns the DataFrame has.
# You should see something like (5, 3)
# (Hint: this one has NO brackets)

# YOUR CODE HERE

print(df.shape)


# ---- Q4 ----
# Print the data types of each column.
# (Hint: also no brackets on this one)

# YOUR CODE HERE
print(df.dtypes)

# ---- Q5 ----
# Print a quick summary of the number columns.
# (Hint: this one DOES have brackets)


# YOUR CODE HERE
print(df.describe())

# ---- Q6 ----
# Print just the last 2 rows of the DataFrame.


# YOUR CODE HERE
print(df.tail(2))