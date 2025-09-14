"""
找到频率最高的元音和辅音
给你一个由小写英文字母（'a' 到 'z'）组成的字符串 s。你的任务是找出出现频率 最高 的元音
（'a'、'e'、'i'、'o'、'u' 中的一个）和出现频率最高的辅音（除元音以外的所有字母），并返回这两个频率之和。
注意：如果有多个元音或辅音具有相同的最高频率，可以任选其中一个。如果字符串中没有元音或没有辅音，则其频率视为 0。
一个字母 x 的 频率 是它在字符串中出现的次数。
"""

def find_freq(s):
    freq_a = {}
    freq_b = {}
    for item in s:
        if item in ["a", "e", "i", "o", "u"]:
            if item in freq_a:
                freq_a[item] += 1
            else:
                freq_a[item] = 1
        else:
            if item in freq_b:
                freq_b[item] += 1
            else:
                freq_b[item] = 1
    return (max(freq_a.values()) if freq_a else 0) + (max(freq_b.values()) if freq_b else 0)



if __name__=='__main__':
    s = "successes"
    # s = "aeiaeia"
    result = find_freq(s)
    print(f"出现的频次和为: {result}")