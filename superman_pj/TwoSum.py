
# problem : https://leetcode.com/problems/two-sum
# Function returns the indices of pair of elements whose sum is equal to the target. There can be only one such pair


# My solution : Using Python index function. Runs in O(n^2)
def twoSum(nums, target):
    for idx, val in enumerate(nums):
        try:
            target_idx = nums.index(target-val, idx+1)
            return [idx, target_idx]
        except ValueError:
            continue

    return []


# Best solution found on Internet: Using Hash tables in one pass. Runs in O(n)
def twoSum_best(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]

        seen[v] = i

    return []


arr = [2, 8, 3, 6]
print(twoSum(arr, 14))
print(twoSum_best(arr, 14))
