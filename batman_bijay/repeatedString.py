# problem : https://www.hackerrank.com/challenges/repeated-string/problem

def countAInRepeatedString(s, n):
    if s.count('a') == len(s):
        return n

    how_many_times_to_repeat_s = n // len(s)
    repeated_count = s.count('a') * (n // len(s))
    repeated_count += s[: n % len(s)].count('a')
    return repeated_count


print(countAInRepeatedString('aba', 10))
print(countAInRepeatedString('abcda', 257))
print(countAInRepeatedString('abc', 343))
print(countAInRepeatedString('abc', 50000))
print(countAInRepeatedString('a', 1000000000000))
print(countAInRepeatedString('abaca', 1000000000000000))
print(countAInRepeatedString('a', 1000000000000000))
print(countAInRepeatedString('abcac', 10))
print(countAInRepeatedString('aaa', 10))
print(countAInRepeatedString('aa', 10))
