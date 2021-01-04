"""
Problem: http://codeforces.com/problemset/problem/677/A
"""

def solve():
    n,h = map(int, input().split())
    heights = list(map(int, input().split()))

    width = 0
    for height in heights:
        if(height > h):
            width += 2
        else:
            width += 1

    print(width)

if __name__ == '__main__':
    solve()