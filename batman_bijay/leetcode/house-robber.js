// https://leetcode.com/problems/house-robber/
// Input: nums = [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
//              Total amount you can rob = 2 + 9 + 1 = 12.

// Constraints:
//     0 <= nums.length <= 100
//     0 <= nums[i] <= 400

/**
 * @param {number[]} nums
 * @return {number}
 */

const rob = function(nums) {
    if (nums.length === 0 || nums === null) {
        return 0;
    } else if (nums.length === 1) {
        return nums[0]
    } 
    let runningTotal = [nums[0], Math.max(nums[0], nums[1])];
    
    for (let i = 2; i < nums.length; i++) {
        runningTotal[i] = Math.max(nums[i] + runningTotal[i - 2], runningTotal[i - 1]);
    }

    return runningTotal[runningTotal.length - 1];    
};



const res = rob([2,1,1,2]);
// const res = rob([]);
console.log('res: ', res)