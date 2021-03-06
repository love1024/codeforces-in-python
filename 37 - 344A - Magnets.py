"""
Problem: http://codeforces.com/problemset/problem/344/A
"""

def solve():
    n = int(input())

    previous = input()
    groups = 1
    for i in range(n-1):
        magnet = input()
        if(magnet[0] == previous[1]):
            groups += 1
        previous = magnet

    print(groups)


if __name__ == '__main__':
    solve()