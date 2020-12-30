"""
Problem: http://codeforces.com/problemset/problem/122/A
"""

def solve():
    # Take input
    n = int(input());

    # If no number can divide n, then we print "NO", otherwise "YES"
    # Remember if it can divide, then n%i = 0, so all operator will return false
    print('NO' if all([n%i for i in[4,7,47,74,447,474,477,747,774]]) else 'YES')

if __name__ == '__main__':
    solve()