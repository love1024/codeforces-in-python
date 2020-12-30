"""
Problem: http://codeforces.com/problemset/problem/58/A
"""

def solve():
    # Take input
    string = iter(input())

    # Declare hello string and found characters = 0
    hello = "hello"
    found = 0

    # Check if we can find all characters of hello
    # Remember if we found some character the iterator of string
    # Will go to next char and will not check the previous characters
    for c in hello:
        if(c in string):
            found += 1

    # If all five characters were found print yes
    if(found == 5):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()