// https://leetcode.com/problems/shuffle-the-array/

// Input: nums = [2,5,1,3,4,7], n = 3
// Output: [2,3,5,4,1,7] 
// Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]

const shuffleArray = function (nums, n) {
    const arr1 = nums.slice(0, n)
    const arr2 = nums.slice(n)
    const shuffledArr = [];
    for (let i = 0; i < arr1.length; i++) {
        shuffledArr.push(arr1[i]);
        shuffledArr.push(arr2[i]);
    }
    return shuffledArr;
}

const res1 = shuffleArray([1, 2, 3, 4, 5, 6], 3);

console.log('res1: ', res1);