# https://www.hackerrank.com/challenges/drawing-book/problem
import math


def pageCount(n, p):
    # Sol 1:
    # p//2 gives the no. of pages required to be turned to reach p when going forward.
    # (n-p)//2 gives the above result when going backward. when total pages is odd, the last page will be printed on both sides.
    # when total pages is even, the last page will be printed on single side. so it will take one additional turn so we round up the result of (n-p)//2 to higher integer

    # start = p // 2
    # end = math.ceil((n-p) / 2) if n % 2 == 0 else (n-p) // 2
    # return min(start, end)

    # Sol 2: elegant solution
    # we can find a page by going forward and backward. each turn of pages we read two pages. so when going forward, p//2 gives the no. of pages turns required from front.
    # similarly when going backwards, you subtract it from the total no. of possible pages turn. so n//2 - p//2 gives the no. of page turns required from backwards.
    # min of these two will is the solution
    return min(p//2, (n//2) - (p//2))


res1 = pageCount(6, 2)  # 1
res2 = pageCount(5, 4)  # 0
res3 = pageCount(7, 3)  # 1
res4 = pageCount(6, 4)  # 1
res5 = pageCount(53, 26)  # 13
res6 = pageCount(6, 5)  # 1
res7 = pageCount(5, 3)  # 1


print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
