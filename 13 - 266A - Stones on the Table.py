"""
Problem: http://codeforces.com/problemset/problem/266/A
"""

def solve():
    # Take input
    length = int(input())
    colors = input()

    # Loop over all chracters and increase count when previous and
    # Current characters are same
    cnt = 0
    for idx in range(1, len(colors)):
        if(colors[idx] == colors[idx-1]):
            cnt = cnt + 1

    print(cnt)
if __name__ == '__main__':
    solve()