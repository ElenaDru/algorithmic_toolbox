# Uses python3
# Problem Description
# Task:
#   The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
# Input Format:
#   The input consists of a single integer 𝑚 3
# Constraints:
#   1 ≤ 𝑚 ≤ 10 .
# Output Format:
#   Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

def get_change(m):

    coins = [10, 5, 1]
    coins_count, i = 0, 0
    while m > 0:
        if m < coins[i]:
            i += 1
        else:
            coins_count += 1
            m -= coins[i]
    return coins_count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
