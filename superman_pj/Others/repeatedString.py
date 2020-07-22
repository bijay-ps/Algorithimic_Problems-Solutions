# problem : https://www.hackerrank.com/challenges/repeated-string/problem

# Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.
# There are no loops, but complexity of count function and substring function is O(n). Not sure of overall time complexity
def repeatedString(s, n):

    if s.count('a') == len(s):
        return n

    seq_count = n // len(s)
    repeat_count = s.count('a') * seq_count
    repeat_count += s[: n % len(s)].count('a')

    return repeat_count


print(repeatedString('abaca', 1000000000000000))
print(repeatedString('aaa', 15))
