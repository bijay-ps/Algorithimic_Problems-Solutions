/*
board =
Y [
 0 --  ['A','B','C','E'],
   X --  0   1   2   3
 1 --  ['S','F','C','S'],
   X --  0   1   2   3
 2 --  ['A','D','E','E']
   X --  0   1   2   3
]

word = SEE
*/

function wordSearch(board, word) {
  // 'count' is how many matching letters we have found
  // i is row
  // j is column
  let matchAllRemainingLetters = (board, i, j, word, count = 0) => {
    if (count === word.length) return true;
    if (
      i < 0 ||
      i >= board.length ||
      j < 0 ||
      j >= board[0].length ||
      board[i][j] !== word[count]
    )
      return false;
    let temp = board[i][j];
    board[i][j] = "";
    let found =
      matchAllRemainingLetters(board, i - 1, j, word, count + 1) ||
      matchAllRemainingLetters(board, i + 1, j, word, count + 1) ||
      matchAllRemainingLetters(board, i, j - 1, word, count + 1) ||
      matchAllRemainingLetters(board, i, j + 1, word, count + 1);
    board[i][j] = temp;
    return found;
  };

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (
        board[i][j] === word[0] &&
        matchAllRemainingLetters(board, i, j, word)
      ) {
        return true;
      }
    }
  }
  return false;
}

const board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
];

const res1 = wordSearch(board, "SEE");
const res2 = wordSearch(board, "SEA");
const res3 = wordSearch(board, "S");
const res4 = wordSearch(board, "C");
const res5 = wordSearch(board, "ABCCED");
const res6 = wordSearch(board, "ABCB");
console.log(res1);
console.log(res2);
console.log(res3);
console.log(res4);
console.log(res5);
console.log(res6);
