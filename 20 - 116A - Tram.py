"""
Problem: https://codeforces.com/problemset/problem/116/A
"""

def solve():
    # Take input
    n = int(input())

    # Initialize passengers to 0 and max capacitiy needed to 0
    passengers = 0
    max_cap = 0

    # Loop over all stations
    for i in range(n):

        # Takd a and b of current solution
        a,b = map(int, input().split())

        # Subtract and add new passengers
        passengers -= a
        passengers += b

        # See if current capcity is maximimum than we already had
        max_cap = max(max_cap, passengers)

    print(max_cap)

if __name__ == '__main__':
    solve()