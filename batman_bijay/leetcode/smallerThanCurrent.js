// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

// Approach I
var smallerNumbersThanCurrent = function (nums) {
    const resArr = [];
    for (let i = 0; i < nums.length; i++) {
        const temp = nums.filter(elt => elt < nums[i]);
        resArr.push(temp.length)
    }
    return resArr;
};

const res1 = smallerNumbersThanCurrent([8, 1, 2, 2, 3]);

console.log('res1: ', res1)