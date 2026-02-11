# ============================================================
# Exercise 02: Selecting Columns and Filtering Rows
# ============================================================
# Dataset: ../data/02_students.csv
#
# This dataset has 8 students with their name, subject, score,
# and grade. You will practice picking out specific columns
# and filtering rows based on conditions.
# ============================================================

import pandas as pd

df = pd.read_csv("data/02_students.csv")


# ---- Q1 ----
# Print just the "name" column.

# YOUR CODE HERE
print(df["name"])


# ---- Q2 ----
# Print all the unique subjects in the dataset.
# (You should see: Maths, English, Science)

# YOUR CODE HERE
print(df["subject"].unique())

# ---- Q3 ----
# Turn the unique subjects into a normal Python list and print it.

# YOUR CODE HERE
print(df["subject"].unique().tolist())

# ---- Q4 ----
# Print only the rows where the subject is "Maths".
# (Hint: use .loc[] with a condition)

# YOUR CODE HERE
print(df.loc[df["subject"] == "Maths"])

# ---- Q5 ----
# Print only the rows where the score is greater than 70.

# YOUR CODE HERE
print(df.loc[df["score"] > 70])

# ---- Q6 ----
# Print only the rows where the subject is "English" AND the score
# is greater than 50.
# (Hint: you need TWO conditions joined with & and each in brackets)

# YOUR CODE HERE
print(df.loc[(df["subject"] == "English") & (df["score"] > 50)])

# ---- Q7 ----
# How many times does each grade appear?
# (Hint: check the primer under "Selecting Columns")

# YOUR CODE HERE

print(df["grade"].value_counts())
