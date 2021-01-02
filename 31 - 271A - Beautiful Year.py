"""
Problem: http://codeforces.com/problemset/problem/271/A
"""

def solve():
    year = int(input())

    while(True):
        year +=1

        different_chars = set(list(str(year)))
        if(len(different_chars) == 4):
            print(year)
            break


if __name__ == '__main__':
    solve()