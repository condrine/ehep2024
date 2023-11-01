# script for solution to question 1 of exercise 1

# system imports
import pandas as pd

# read file
data = pd.read_csv("data/scores.csv")

# sorted values to third column
data_sorted_to_third = data.sort_values(by=['C'])
data_sorted_to_third.to_csv("results/scores_sorted_by_C.csv",index=False)   # dump to csv
print("scores sorted by third column are stored at results/scores_sorted_by_C.csv.")

# sorted values to sum
data["sum"] = data.sum(axis=1)
data_sorted_to_sum = data.sort_values(by=['sum'])
data_sorted_to_sum.to_csv("results/scores_sorted_by_sum.csv",index=False)   # dump to csv
print("scores sorted by sum are stored at results/scores_sorted_by_sum.csv.")
