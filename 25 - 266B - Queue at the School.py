"""
Problem: http://codeforces.com/problemset/problem/266/B
"""

def solve():
    # Take input
    n, t = map(int, input().split())
    string = input()

    # During every second, replace BG with GB
    for i in range(t):
        string = string.replace("BG","GB")

    print(string)

if __name__ == '__main__':
    solve()