"""
Problem: http://codeforces.com/problemset/problem/118/A
"""

def solve():
    # Take string input
    string = input()

    # Declare list of vowels
    vowels = ['a','e','i','o','u','y']

    # Replace vowel and its capital in the string with empty
    for vowel in vowels:
        string = string.replace(vowel, "")
        string = string.replace(vowel.upper(),"")

    # Now convert string to list and join using "."
    # Finally add "." at start
    print(("."+".".join(list(string))).lower())

if __name__ == '__main__':
    solve()