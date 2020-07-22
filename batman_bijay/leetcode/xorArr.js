// https://leetcode.com/problems/xor-operation-in-an-array/

var xorOperation = function (n, start) {
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(start + 2 * i)
    }
    let bitWiseXOR = 0;
    arr.forEach(elt => {
        bitWiseXOR = bitWiseXOR ^ elt;
    });
    return bitWiseXOR;
};