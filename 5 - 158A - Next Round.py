"""
Problem: http://codeforces.com/problemset/problem/158/A
"""

def solve():
    # Take input
    n,k = map(int, input().split())

    #
    scores = list(map(int, input().split()))

    kth_score = scores[k-1]

    qualified = 0
    for score in scores:
        if(score > 0 and score >= kth_score):
            qualified = qualified + 1

    print(qualified)

if __name__ == '__main__':
    solve()