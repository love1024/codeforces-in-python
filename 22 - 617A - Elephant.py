"""
Problem: http://codeforces.com/problemset/problem/617/A
"""

def solve():
    # take coordinates of friends house
    friends_house = int(input())

    # If it is multiple of 5, then take only 5 steps, if not, then first take 5 steps, then take 1 extra step
    print(friends_house // 5 if friends_house%5==0 else friends_house // 5 + 1)

if __name__ == '__main__':
    solve()