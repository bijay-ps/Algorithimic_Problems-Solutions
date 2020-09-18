// https://leetcode.com/problems/create-target-array-in-the-given-order/
// Given two arrays of integers nums and index. Your task is to create target array under the following rules:

// Initially target array is empty.
// From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
// Repeat the previous step until there are no elements to read in nums and index.
// Return the target array.

// It is guaranteed that the insertion operations will be valid.

/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
const createTargetArray = function (nums, index) {
    const target = [];
    index.forEach((num, i) => {
        console.log(`index[${i}]: ${num} and nums[${i}]: ${nums[i]}`);
        target.splice(num, 0, nums[i]);
    })
    return target;
};

console.log(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]));