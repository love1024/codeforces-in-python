"""
Problem: http://codeforces.com/problemset/problem/160/A
"""

def solve():
    # Take input
    n = int(input())
    coins = list(map(int,input().split()))

    # Sort given coins in descending order
    coins.sort(reverse=True)

    # Initalize total sum and current sum = 0
    total_sum = sum(coins)
    cur_sum = 0

    # Go over all the coins
    for i in range(n):

        # Add current coin to the sum we are counting
        cur_sum += coins[i]

        # If current sum becomes greater than the rest of coins' sum
        # then break
        if(cur_sum > (total_sum - cur_sum)):
            print(i+1)
            break

if __name__ == '__main__':
    solve()