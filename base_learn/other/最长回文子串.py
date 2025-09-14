"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""
def longest_palindrome(s):
    n = len(s)
    if n == 1:
        return s
    dp = [[False for _ in range(n)] for _ in range(n)]
    start, max_len = 0, 1
    # 所有长度为1的子串都是回文
    for i in range(n):
        dp[i][i] = True
    # 检查长度为2的子串
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    # 检查长度大于2的子串
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    return s[start:start + max_len]


if __name__=='__main__':
    s = "babad"
    result = longest_palindrome(s)
    print(f"最长回文子串的结果为: {result}")