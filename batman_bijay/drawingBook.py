# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    return min(p//2, (n-p)//2)


res1 = pageCount(6, 2)  # 1
res2 = pageCount(5, 4)  # 0
res3 = pageCount(7, 3)  # 1
res4 = pageCount(6, 4)  # 1
res5 = pageCount(53, 26)  # 13
res6 = pageCount(6, 5)  # 1

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
