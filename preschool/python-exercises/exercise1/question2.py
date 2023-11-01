# script for solution to question 2 of exercise 1

# python imports
import numpy as np
import matplotlib.pyplot as plt

# throw two dice
die1_res = np.random.randint(1, 7, 10000)
die2_res = np.random.randint(1, 7, 10000)
dice_tot = die1_res + die2_res    # sum the two dice

# get frequency of dice total
unique, counts = np.unique(dice_tot, return_counts=True)

# print in terminal
print("Terminal bar graph for the dice total: ")
print("=========================================")
print(*[f"val{val}: \t {'*'*(freq//100)}" for val, freq in zip(unique, counts)], sep="\n")

# draw histogram
plt.bar(unique, counts/100)
plt.xlabel("Dice sum")
plt.ylabel("Freq (%)")
plt.savefig("results/dice_hist.png")
print("Histogram saved at results/dice_hist.png.")
plt.show()


# draw scatterplot
plt.scatter(die1_res, die2_res)
plt.xlabel("Die 1")
plt.ylabel("Die 2")
plt.savefig("results/dice_scatter.png")
print("Scatter plot saved at results/dice_scatter.png.")
plt.show()
