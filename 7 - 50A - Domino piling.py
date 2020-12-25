"""
Problem: http://codeforces.com/problemset/problem/50/A
"""

def solve():
    # Take input
    m,n = map(int, input().split())

    # See how many can we cover just using domino
    # horizontally (1 X 2)
    required = (m // 2) * n

    # If length is odd, we would have 1 column left at the end
    # Now cover this column by vertical dominio (1 X 2)
    if(m%2 != 0):
        required = required + (n // 2)
    print(required)

if __name__ == '__main__':
    solve()