"""
Problem: http://codeforces.com/problemset/problem/112/A
"""

def solve():
    # Get both strings
    string1 = input()
    string2 = input()

    # Now print according to if string 1 is lower or greater or equal
    if(string1.lower() < string2.lower()):
        print(-1)
    if(string1.lower() == string2.lower()):
        print(0)
    if(string1.lower() > string2.lower()):
        print(1)

if __name__ == '__main__':
    solve()