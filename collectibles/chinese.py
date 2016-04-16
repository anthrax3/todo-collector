# coding: utf-8
"""Import this file if you want your collectibles to be Chinese characters."""

import random

from collectible import Collectible

# Approximately ten thousand Chinese characters, by frequency.
# Source: http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php
with open('collectibles/chinese-data.txt', 'r') as fi:
    CHINESE_STRING = fi.read().strip()

chinese_array = []
for line in CHINESE_STRING.split('\n'):
    split_line = line.split('\t')
    split_line[0] = int(split_line[0])
    split_line[2] = int(split_line[2])
    split_line[3] = float(split_line[3])
    chinese_array.append(split_line)

def get_cdf_at(index):
    return chinese_array[index][3] / 100.0

def binary_search(value):
    """Return the greatest index r such that value < array[r]."""
    return binary_search_helper(0, len(chinese_array) - 1, value)

def binary_search_helper(i, j, value):
    """Return the greatest index r such that value < array[r], constrained
    to search within i <= r < j."""
    # Invariant: value < array[j]
    if i == j:
        return i
    mid = (i + j) / 2
    midval = get_cdf_at(mid)

    if value < midval:
        return binary_search_helper(i, mid, value)
    else:
        return binary_search_helper(mid+1, j, value)


class Chinese(Collectible):
    def display_many(self, indices):
        return " ".join(chinese_array[i][1] for i in indices)

    def pick_a_thing(self):
        random_value = random.random()
        return binary_search(random_value)

    def display_one(self, index):
        _, character, frequency, cdf, pinyin, description = chinese_array[index]
        output = ("Here's your next character: " + character +
                  "\nIts pinyin: " + pinyin +
                  "\nDescription: " + description)
        return output
