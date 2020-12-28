"""
Problem: http://codeforces.com/problemset/problem/69/A
"""

def solve():
    # Take total number of fores
    total_forces = int(input())

    # Initialize vector sums as 0
    x,y,z = 0,0,0

    # Now take force in every line and to the x,y and z
    for _ in range(total_forces):
        a,b,c = map(int, input().split())
        x += a
        y += b
        z += c

    # If at last, the sum remains zero for all, then we are in equilbrium
    # Otherwise not
    if(x == 0 and y == 0 and z == 0):
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    solve()