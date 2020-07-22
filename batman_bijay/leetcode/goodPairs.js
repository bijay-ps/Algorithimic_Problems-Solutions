// https://leetcode.com/problems/number-of-good-pairs/
// A pair (i,j) is called good if nums[i] == nums[j] and i < j

// [1,2,3,1,1,3]
//  0 1 2 3 4 5
// There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed
// Approach I - naive approach
const numIdenticalPairs = function (nums) {
    let goodPair = 0;
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (i < j && nums[i] == nums[j]) goodPair++;
        }
    }
    return goodPair;
};

// Approach II

// [1,1,1,1]
//  0 1 2 3
// n = 4
// n(n-1)/2 => 4(3)/2 = 12/2 = 6 
// [1,2,3,1,1,3]
//  0 1 2 3 4 5
// There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed
// {1:3,2:1,3:1}
// no. of pairs with 1 = (3*2)/2 = 3
// no. of pairs with 3 = (2*1)/2 = 1
// total pairs = 4

const numIdenticalPairsII = function (nums) {
    let goodPair = 0;
    let numsObj = nums.reduce((acc, cur) => {
        return {
            ...acc,
            [cur]: acc[cur] ? acc[cur] + 1 : 1,
        };
    }, {});
    for (let prop in numsObj) {
        let n = numsObj[prop]
        goodPair = goodPair + (n * (n - 1)) / 2
    }
    return goodPair;
};

const res1 = numIdenticalPairs([1, 2, 3, 1, 1, 3]);
const res2 = numIdenticalPairs([1, 1, 1, 1]);
const res3 = numIdenticalPairs([1, 2, 3]);

const res4 = numIdenticalPairsII([1, 2, 3, 1, 1, 3]);
const res5 = numIdenticalPairsII([1, 1, 1, 1]);
const res6 = numIdenticalPairsII([1, 2, 3]);

console.log(`res1: ${res1}`);
console.log(`res2: ${res2}`);
console.log(`res3: ${res3}`);

console.log(`res4: ${res4}`);
console.log(`res5: ${res5}`);
console.log(`res6: ${res6}`);
