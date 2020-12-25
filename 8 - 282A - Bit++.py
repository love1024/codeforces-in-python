"""
Problem: http://codeforces.com/problemset/problem/282/A
"""

def solve():
    # Get count of total operations
    total_operations = int(input())

    # Initialize the value to 0
    val = 0

    # Loop over all operations
    for _ in range(0,total_operations):

        # Get current operation
        operation = input()

        # If operation is X++ or ++X then increment
        if("++" in operation):
            val = val + 1
        # If operation is X-- or --X then decrement
        elif("--" in operation):
            val = val - 1

    print(val)


if __name__ == '__main__':
    solve()