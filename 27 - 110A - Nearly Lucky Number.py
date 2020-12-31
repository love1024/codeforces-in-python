"""
Problem: http://codeforces.com/problemset/problem/110/A
"""

def solve():
    # Take input
    number = input()

    # check how many digits are lucky
    total_lucky = 0
    for digit in number:
        if(digit == '4' or digit == '7'):
            total_lucky += 1

    # If lucky digits are a lucky number, then print YES
    if(total_lucky in [4,7,47]):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()