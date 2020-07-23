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
*/

function wordSearch(board, word) {
  const given_word = word;
  const indices = findIndices(given_word[0], board);
  // console.log("indices: ", indices);
  findAdjacent(word[0], indices, board);
}

function findIndices(char, board) {
  let indices = [];
  board.forEach((subArr, index) => {
    subArr.forEach((e, i) => {
      if (e === char) {
        let temp = { [index]: i };
        indices.push(temp);
      }
    });
  });
  return indices;
}

function findAdjacent(X, xIndices, board) {
  let adjLetters = [];
  console.log("line 35", xIndices);
  const Yaxis = Object.keys(xIndices);
  console.log("line 37", Yaxis);
  Yaxis.forEach((e) => {});
}

const board = [
  ["A", "B", "C", "E"],

  ["S", "F", "C", "S"],

  ["A", "D", "E", "E"],
];

wordSearch(board, "S");
// wordSearch(board, "E");
