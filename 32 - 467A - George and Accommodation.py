"""
Problem: http://codeforces.com/problemset/problem/467/A
"""

def solve():
    # Take input
    n = int(input())

    # go through all the rooms
    total_avail = 0
    for _ in range(n):
        p,q = map(int, input().split())

        # if 2 or more seats are available in a room, increment count
        if(q - p >= 2):
            total_avail += 1
    print(total_avail)

if __name__ == '__main__':
    solve()