#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# problem : https://www.hackerrank.com/challenges/migratory-birds/problem
# Function returns the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number


def migratoryBirds(arr):
    freq_list = Counter(arr)
    max_count = max(freq_list.values())
    most_common_birds = []

    for freq in freq_list.items():
        if freq[1] == max_count:
            most_common_birds.append(freq[0])

    return min(most_common_birds)


if __name__ == '__main__':
    temp = [int(x) for x in input(
        "Please enter list of numbers without any space: ") if x != ' ']
    print(f"Input: {temp}")
    print(f"Output: {migratoryBirds(temp)}")
