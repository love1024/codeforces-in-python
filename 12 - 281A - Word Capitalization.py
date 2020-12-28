"""
Problem: http://codeforces.com/problemset/problem/281/A
"""

def solve():
    # Take input string
    ""
    string = input()

    # Capitalize first letter and take rest of the string as same
    newString = string[0].upper() + string[1:]

    print(newString)

if __name__ == '__main__':
    solve()