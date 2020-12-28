"""
Problem: https://codeforces.com/problemset/problem/791/A
"""

def solve():
    # Take input of a and b
    a,b = map(int, input().split())

    # Initialize years to 1
    years = 1

    # While weight is smaller carry on
    while(True):

        # if weight increases then break
        if(3**years * a > 2**years * b):
            break
        years += 1
    print(years)

if __name__ == '__main__':
    solve()