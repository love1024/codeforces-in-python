"""
Problem: http://codeforces.com/problemset/problem/158/B
"""

def solve():
    # Take input
    n = int(input())
    children = list(map(int, input().split()))

    # Sort children groups
    children.sort()

    # Initialize variables, on the start and end of list
    i,j = 0, n-1
    require = 0

    # While start is less than or equal to end
    while(i <= j):

        # If both pointers are pointing to same item, the for sure we need a taxi
        if(i == j):
            require += 1
            break

        # If combination of biggest and smallest groups currently is less than 4,
        # then we can pack them in a taxi, and increase i to see if we can pack
        # some more small group
        # Also increase children in j by children added by i
        if(children[i] + children[j] <= 4):
            i += 1
            children[j] += children[i]
        else:
            # If sum is more than 4, then we can't pack them
            # so add a taxi for biggest group
            require += 1
            j -= 1

    print(require)

if __name__ == '__main__':
    solve()