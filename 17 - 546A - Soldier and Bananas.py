"""
Problem: https://codeforces.com/problemset/problem/546/A
"""

def solve():
    # Take input
    k,n,w = map(int, input().split())

    # he needed following money for buying
    # 1k + 2k + 3k .... wk = k * w * (w+1) / 2
    needed = int(k * w * (w + 1) / 2)

    # if needed is greater than he has, print (needed - n) else print n
    print(0 if needed < n else (needed - n))

if __name__ == '__main__':
    solve()