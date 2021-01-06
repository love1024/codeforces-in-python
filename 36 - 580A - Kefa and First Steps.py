"""
Problem: http://codeforces.com/problemset/problem/580/A
"""

def solve():
    # take input
    n = int(input())
    money_list = map(int, input().split())

    maximum_seq = 0 # maximum sequence found till now
    current_seq = 0 # current sequence length found till now
    previous = -1 # previous element

    # Loop over all money
    for money in money_list:
        # if money is more than previous, then increase current sequence
        # Else reset current sequence to 1
        if(money >= previous):
            current_seq += 1
        else:
            current_seq  = 1

        previous = money # make current money as previous
        maximum_seq = max(maximum_seq, current_seq) # check if current sequence surpasses maximum sequence

    print(maximum_seq)

if __name__ == '__main__':
    solve()