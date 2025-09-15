"""
键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。
给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；
另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。
"""


def typed_words(text, brokenLetters):
    # 1.对text按照空格进行分割
    words = text.split()
    count = 0
    # 遍历 words
    for word in words:
        flag = False
        for letter in brokenLetters:
            if letter in word:
                flag = True
                break
        if not flag:
            count += 1
    return count


if __name__=='__main__':
    text = "hello world"
    brokenLetters = "ad"
    result = typed_words(text, brokenLetters)
    print(f"可以输入的text单词个数: {result}")