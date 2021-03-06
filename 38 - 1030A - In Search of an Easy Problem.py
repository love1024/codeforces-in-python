"""
Problem: http://codeforces.com/problemset/problem/1030/A
"""

def solve():
    n = int(input())
    problems = list(map(int, input().split()))

    print("HARD" if any(problems) else "EASY")

if __name__ == '__main__':
    solve()