"""
Problem: http://codeforces.com/problemset/problem/41/A
"""

def solve():
    # Take both strings
    string1 = input()
    string2 = input()

    # Reverse second string
    string2 = string2[::-1]

    # If both strings are same, print yes else print no
    print("YES" if string1 == string2 else "NO")

if __name__ == '__main__':
    solve()