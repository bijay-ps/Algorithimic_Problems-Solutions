# https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums: list, n: int) -> list:
    if n == 0:
        return nums
    shuffle_nums = []
    for i in range(0, n):
        shuffle_nums.append(nums[i])
        shuffle_nums.append(nums[i+n])
    return shuffle_nums


# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
def kidsWithCandies(candies: list, extraCandies: int) -> list:
    result = []
    greatestCandies = max(candies)
    for i in candies:
        result.append(True if i + extraCandies >= greatestCandies else False)
    return result


def busyStudent(startTime: list, endTime: list, queryTime: int) -> int:
    students = 0
    for i in range(0, len(startTime)):
        if startTime[i] <= queryTime <= endTime[i]:
            students += 1

    return students


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    print(shuffle(nums, 4))
    print(kidsWithCandies(nums, 2))
    print(busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))

    def exist():
        seen = []
        match_board_idxs = []
        word = "AAB"
        match_word_idx = 0
        board = [["C", "A", "A"],
                 ["A", "A", "A"],
                 ["B", "C", "D"]]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[match_word_idx] == board[i][j]:
                    match_board_idxs.append((i, j))
        temp_idx = 0
        for a, b in match_board_idxs:
            seen.append(match_board_idxs[temp_idx])
            match_word_idx = 1
            i = a
            j = b
            while match_word_idx < len(word):
                found_match = (-1, -1)
                adjacentIdxs = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
                for x, y in adjacentIdxs:
                    if 0 <= x < len(board) and 0 <= y < len(board[x]) and word[match_word_idx] == board[x][y] and (x, y) not in seen:
                        found_match = (x, y)
                        break
                # How to handle when there are more than one match
                if found_match == (-1, -1):
                    break
                i, j = found_match
                match_word_idx += 1
                seen.append((i, j))
            if match_word_idx == len(word):
                return True
            seen.clear()
            temp_idx += 1

        return False

    print(exist())
