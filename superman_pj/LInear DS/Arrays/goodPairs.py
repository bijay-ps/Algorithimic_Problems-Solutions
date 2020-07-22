# https://leetcode.com/problems/number-of-good-pairs/
def numIdenticalPairs(nums: list) -> int:
    hash_nums = {i: nums.count(i) for i in nums if nums.count(i) > 1}
    pair = 0
    if hash_nums == {}:
        return pair
    for count in hash_nums.values():
        pair += combinations(count, 2)
    return pair


def combinations(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return combinations(n-1, k-1) + combinations(n-1, k)


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(nums))
    print(numIdenticalPairs([1, 2, 3]))
    print(numIdenticalPairs([1, 1, 1, 1]))
