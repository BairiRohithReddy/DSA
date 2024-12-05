# print from 1 to n without incrementing usign BACKTRACKING
def backtrack(i, n):
    if i < 1:
        return
    backtrack(i-1, n)
    print(i)
    
a = backtrack(5,5)