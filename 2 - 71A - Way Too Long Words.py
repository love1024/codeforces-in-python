"""
Problem: http://codeforces.com/problemset/problem/71/A
"""

def solve():
    # Get total number of inputs as number
    total_numbers = int(input())

    # Loop over all given strings
    for _ in range(0, total_numbers):

        # Take the current string
        word = input()

        # If its length is strictly more than 10, then find the
        # print first and the last character and count of the other numbers in between
        if(len(word) > 10):
            print(f"{word[0]}{len(word) - 2}{word[-1]}")
        else:

            # If length is smaller than 11, just print that number
            print(word)

if __name__ == '__main__':
    solve()