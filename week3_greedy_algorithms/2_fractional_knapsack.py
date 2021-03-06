# Uses python3
# Problem Introduction
# A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of
# items assuming that any fraction of a loot item can be put into his bag.

# Problem Description:

# Task:
#   The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format:
#   The first line of the input contains the number π of items and the capacity π of a knapsack.
#   The next π lines define the values and weights of the items. The π-th line contains integers π£π and π€πβthe value
#   and the weight of π-th item, respectively.
# Constraints:
#   1β€πβ€103,0β€π β€2Β·106;0β€π£π β€2Β·106,0<π€π β€2Β·106 forall1β€πβ€π.Allthe numbers are integers.
# Output Format:
#   Output the maximal value of fractions of items that fit into the knapsack.

import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    rates = []
    for i in range(len(weights)):
        rates.append((i, values[i] / weights[i]))
    items_order = [item[0] for item in sorted(rates, key=lambda  x: x[1], reverse=True)]
    i = 0

    while capacity > 0 and i < len(weights):
        n_item = items_order[i]
        m = min(capacity, weights[n_item])
        value += m * values[n_item] / weights[n_item]
        capacity -= m
        i += 1

    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
