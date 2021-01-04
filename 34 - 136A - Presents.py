"""
Problem: http://codeforces.com/problemset/problem/136/A
"""

def solve():
    # Take inputs
    n = int(input())
    lst = map(int, input().split())

    # Now store these list as tuple, with friend as first item and its index as second
    gifts = []
    for given_to, given_by in enumerate(lst):
        gifts.append((given_by, given_to+1))

    # Sort these gifts by friend number
    gifts.sort()

    # Now print only the index of the list
    for idx,gift in enumerate(gifts):
        _,given_to = gift
        print(given_to, end=("" if idx == len(gifts) -1 else " "))

if __name__ == '__main__':
    solve()