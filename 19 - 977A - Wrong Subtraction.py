"""
Problem: https://codeforces.com/problemset/problem/977/A
"""

def solve():
    # Take input
    n,k = map(int, input().split())

    # Carry on all operations
    for i in range(k):

        # If its divided by 10, divide it
        if(n%10 == 0):
            n = int(n/10)
        else:
            # Else substract 1 from it
            n = n - 1
    print(n)

if __name__ == '__main__':
    solve()