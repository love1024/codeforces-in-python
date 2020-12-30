"""
Problem: http://codeforces.com/problemset/problem/59/A
"""

def solve():
    # Take input
    string = input()

    # Count uppercase and lowercase letters
    uppercase = 0
    lowercase = 0
    for c in string:
        if(c.isupper()):
            uppercase += 1
        else:
            lowercase += 1

    # If uppercase are more, then print string in uppercase, else in lowercase
    if(uppercase > lowercase):
        print(string.upper())
    else:
        print(string.lower())

if __name__ == '__main__':
    solve()