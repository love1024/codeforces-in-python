"""
Problem: http://codeforces.com/problemset/problem/133/A
"""

def solve():
    string = input()

    if('H' in string or 'Q' in string or '9' in string):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()