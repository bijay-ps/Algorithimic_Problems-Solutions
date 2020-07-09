function bonAppetit(bill, k, b) {
  const bill_copy = [...bill];
  bill_copy.splice(k, 1);
  const actual_bill = bill_copy.reduce((acc, cur_val) => acc + cur_val) / 2;
  if (b - actual_bill > 0) {
    console.log(`${b - actual_bill}`);
  } else {
    console.log(`Bon Appetit`);
  }
}

const billArr = [3, 10, 2, 9];
const index = 1;
const billPaid1 = 12;
const billPaid2 = 7;

bonAppetit(billArr, index, billPaid1);
bonAppetit(billArr, index, billPaid2);
