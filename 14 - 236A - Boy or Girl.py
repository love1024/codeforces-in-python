"""
Problem: http://codeforces.com/problemset/problem/236/A
"""

def solve():
    # Take string input and convert to set and check even or odd
    string = input()
    if(len(set(string)) % 2 == 0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == '__main__':
    solve()