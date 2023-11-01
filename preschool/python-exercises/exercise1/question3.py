# script for solution to question 3 of exercise 1

# python imports
import numpy as np
import random
from itertools import islice


def numbers_with_fixed_sum(low, high, sum):
    """
       Returns array of random numbers with a fixed sum.
    """
    # check for faulty input
    if high < 2*low: 
        raise ValueError('Only ranges with max > 2*min are supported.')

    num_arr = []    # initialise array
    new_num = random.randint(low, high) # generate a new random number

    # start loop
    while sum > max(2*low, new_num+low):
        num_arr.append(new_num) # add the number to list
        sum -= new_num  # update sum
        new_num = random.randint(low, high) # generate a new random number

    if sum > high:
        new_num = random.randint(low, high-low)
        sum -= new_num

    if sum > 0: num_arr.append(sum) # append remaining value

    return num_arr  # return the number array


def batched(data, size):
    """
        Batch data into tuples of variable/fixed length. 
        The last batch may be shorter.
    """

    if isinstance(size, list):
        if len(size) < 1:
            raise ValueError('size array cannot be empty.') # check for faulty input
        # return batches
        it = iter(data)
        for arr_len in size:
            if (batch := tuple(islice(it, arr_len))): yield batch
    elif isinstance(size, int):
        if size < 1:
            raise ValueError('size cannot be less than 1.') # check for faulty input
        # return batches
        it = iter(data)
        while (batch := tuple(islice(it, size))):
            yield batch
    else:
        raise ValueError('unsupported datatype encountered for size.')  # check for faulty input
    

# open and read original file
with open("data/numbers.txt", "r") as numfile:
    numbers = np.array(numfile.readlines(), dtype=int)
    print("Read data from data/numbers.txt.")

# write 10 entries per line to file
with open("results/numbers10.txt", "+w") as numfile:
    num_10_per_row = list(batched(numbers, 10))
    numfile.write('\n'.join([" ".join(map(str, nums)) for nums in num_10_per_row]))
    print("10 entries per line written to results/numbers10.txt.")

# write random entries per line to file
with open("results/multi_numbers.txt", "+w") as num10file:
    rand_size_list = numbers_with_fixed_sum(5, 15, len(numbers))    # create an array of random sizes per line
    num_rand_per_row = list(batched(numbers, rand_size_list))
    num10file.write('\n'.join([" ".join(map(str, nums)) for nums in num_rand_per_row]))
    print("Random no. of entries per line written to results/multi_numbers.txt.")

# open and read file with random number of entries per line
with open("results/multi_numbers.txt", "r") as numfile:
    numbers = []
    lines = numfile.readlines()
    numbers = sum([list(line.split()) for line in lines], [])
    print("Read data from results/multi_numbers.txt.")

# write 10 entries per line to file
with open("results/numbers10_new.txt", "+w") as numfile:
    num_10_per_row = list(batched(numbers, 10))
    numfile.write('\n'.join([" ".join(map(str, nums)) for nums in num_10_per_row]))
    print("10 entries per line written to results/numbers10_new.txt.")
    




