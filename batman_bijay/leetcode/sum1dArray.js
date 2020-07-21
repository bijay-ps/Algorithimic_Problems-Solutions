// https://leetcode.com/problems/running-sum-of-1d-array/

const runningSum = function (nums) {
    let sumArr = [];
    if (nums.length > 0) {
        nums.forEach(item => {
            const lastElt_SumArr = sumArr[sumArr.length - 1];
            newElt = lastElt_SumArr ? lastElt_SumArr + item : item;
            sumArr = [...sumArr, newElt];
        });
    }
    return sumArr;
}

const res1 = runningSum([1, 1, 1, 1, 1]);
const res2 = runningSum([1, 2, 3, 4]);
const res3 = runningSum([3, 1, 2, 10, 1]);

console.log(`res1: ${res1}`);
console.log(`res2: ${res2}`);
console.log(`res3: ${res3}`);