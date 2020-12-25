"""
Problem: http://codeforces.com/problemset/problem/263/A
"""

def solve():
    # First find the index of i and j of 1 in the matrix
    # or the position of the 1 in matrix
    i,j = 0,0
    while(True):
        # Get current line and convert its numbers into a list
        numbers = map(int, input().split())
        j = 0
        found = False

        # Loop over all numbers in the current row and try to find 1
        for num in numbers:

            # If 1 found, then break from for and while loop
            if(num == 1):
                found = True
                break
            j = j + 1
        if(found):
            break

        # Move onto next row if 1 is not found in this row
        i = i + 1

    # Now simply find the  difference from the middle cell
    print(abs(2 - i) + abs(2 - j))

if __name__ == '__main__':
    solve()