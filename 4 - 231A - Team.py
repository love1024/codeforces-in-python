"""
Problem: http://codeforces.com/problemset/problem/231/A
"""

def solve():
    # Get total number of questions given
    total_questions = int(input())

    # Questions count that will be solved
    solved = 0

    # Loop over all questions
    for question in range(0, total_questions):

        # Get for three friends, if they will solve the question or not
        a,b,c = map(int, input().split())

        # If at least 2 of them will solve it, its a plus count
        if(a + b + c > 1):
            solved = solved + 1

    print(solved)

if __name__ == '__main__':
    solve()