"""
Problem: http://codeforces.com/problemset/problem/1/A
"""

import math

def solve():
    n,m,a = map(int, input().split())

    # Total granite which can cover the length of square
    granite_for_length = math.ceil(n / a)

    # Total granite which can cover the width of square
    granite_for_width = math.ceil(m / a)

    # Total number is equal to the multiple of both length and width
    print(granite_for_length * granite_for_width)


if __name__ == '__main__':
    solve()