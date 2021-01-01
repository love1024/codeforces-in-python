"""
Problem: http://codeforces.com/problemset/problem/734/A
"""

def solve():
    # Take input
    _ = input()
    games = input()

    # Count number A and D
    A,D = 0,0
    for c in games:
        if(c == 'A'):
            A += 1
        else:
            D += 1

    # Print accordingly
    if(A > D):
        print("Anton")
    elif(D > A):
        print("Danik")
    else:
        print("Friendship")

if __name__ == '__main__':
    solve()