"""
Problem: http://codeforces.com/problemset/problem/96/A
"""

def solve():
    # Take input and initialize variables
    positions = input()
    count = 1
    isDang = False

    # Loop over all the positions
    for pos in range(1, len(positions)):

        # Check if previous position was same as now, then increase count
        if(positions[pos] == positions[pos-1]):
            count += 1
        else:
            count = 1

        # If count reaches to 7, then its a dangerous position
        if(count == 7):
            isDang = True
            break

    print("YES" if isDang else "NO")
if __name__ == '__main__':
    solve()