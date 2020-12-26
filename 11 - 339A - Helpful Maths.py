"""
Problem: http://codeforces.com/problemset/problem/339/A
"""

def solve():
    # Get the number line
    line = input()

    # Split line using + as separator
    numbers = line.split("+")

    # Now sort the list of strings (or numbers)
    numbers.sort()

    # Now join these numbers again with +
    print("+".join(numbers))


if __name__ == '__main__':
    solve()