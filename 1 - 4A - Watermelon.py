"""
Problem: http://codeforces.com/problemset/problem/4/A
"""

def solve():

    # Get the weight of watermelon
    weight_of_watermelon = int(input())
    if(weight_of_watermelon > 2):

        # We know sum of two numbers is odd, if one of the number is odd
        # So we can't split an odd number into two even numbers
        # Print "YES" if number is even, otherwise "NO"
        print("YES" if weight_of_watermelon%2==0 else "NO")
    else:

        # Remember the case of number 2, where it can only be splitted to 1-1 which are not even
        print("NO")



if __name__ == '__main__':
    solve()