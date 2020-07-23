function singleNumber(nums) {
  let obj = {};
  let outputArr = [];
  for (const num of nums) {
    const temp = obj[num];
    if (temp || temp === 0) {
      obj[num] += 1;
    } else {
      obj[num] = 1;
    }
  }
  for (const [key, value] of Object.entries(obj)) {
    if (value === 1) {
      outputArr.push(key);
    }
  }

  return outputArr;
}

const res1 = singleNumber([1, 2, 1, 3, 2, 5]);
console.log(res1);
