// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

// Input: candies = [2,3,5,1,3], extraCandies = 3
// Output: [true,true,true,false,true] 
// Explanation: 
// Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
// Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
// Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
// Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
// Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 

// Approach I
var kidsWithCandies = function (candies, extraCandies) {
    var max = candies.reduce(function (a, b) {
        return Math.max(a, b);
    });
    const resArr = [];
    candies.forEach(candy => {
        if (candy === max || (max - candy) <= extraCandies) {
            resArr.push(true)
        } else {
            resArr.push(false)
        }
    })
    return resArr;
};

// Approach II
var kidsWithCandiesII = function (candies, extraCandies) {
    const max = Math.max(...candies);
    let result = [];

    for (let i = 0; i < candies.length; i++) {
        let cv = candies[i];

        result.push(cv + extraCandies >= max);
    }

    return result;
}

const arr1 = [1, 2, 3];
const arr2 = [2, 3, 5, 1, 3];
const res1 = kidsWithCandies(arr1, 2);
const res2 = kidsWithCandies(arr2, 3);
console.log('res1: ', res1);
console.log('res2: ', res2);