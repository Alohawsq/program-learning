"""
常用正则表达式
"""

import re

def get_result(pattern, text):
    result = re.search(pattern, text)
    print(result)
    if result:
        print(f"{text}的结果为: {result.group()}")

if __name__=='__main__':
    # 手机号提取
    text = "杨🐶的手机号15286984890"
    pattern = r"1[3-9]\d{9}$"
    get_result(pattern, text)

    # 邮箱提取
    text = "杨🐶的邮箱为2012264188@qq.com嘿嘿"
    # \w在某些正则引擎中会匹配中文字符，导致匹配范围过大
    pattern = r"[0-9A-Za-z_.-]+@[0-9A-Za-z_.-]+\.[0-9A-Za-z_]+"
    get_result(pattern, text)

    # 提取身份证号
    text = "兜兜的身份证号为410726199603169613"
    pattern = r"\d{17}[\dxX]"
    get_result(pattern, text)

    # 验证强密码,至少8位，同时包含大写字母、小写字母和数字。
    text = "兜兜的密码为6Ws13542323"
    # (?=...)检查当前位置之后是否存在某种模式，但侦察兵本身不消耗任何字符，也不会“占据”匹配结果
    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{8,}"
    get_result(pattern, text)
    # 密码必须有数字、字母下划线组成，大写字母开头且同时包含大写字母、小写字母和数字且长度不低于8位
    get_result(pattern, text)
    text = "Yh15286984890_"
    pattern = r"^[A-Z](?=.*[a-z])(?=.*\d)(?=..*_)[A-Za-z0-9_]{7,}"
    get_result(pattern, text)

    # 将日期格式从 yyyy-mm-dd 替换为 dd/mm/yyyy
    text = "今天的日期是2023-04-15，会议安排在2023-05-20。"
    # 限定月份在01-12之间，天数在01-31之间
    pattern = r"\b(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b"
    replacement = r"\3/\2/\1"
    result = re.sub(pattern, replacement, text)
    print(result)

    # 去除字符串首尾的空格
    text = " 你好，兜兜。   "
    pattern = r'^\s+|\s+$'
    result = re.sub(pattern, '', text)
    print([result])

    # 匹配html标签
    text = "<div> content </div>"
    pattern = "<(.*)>"
    get_result(pattern, text)
    pattern = "<(.*?)>"
    get_result(pattern, text)
    # 提取标签中的内容
    text = "<div>Hello</div><p>World</p>"
    pattern = r"<.*?>(.*?)<.*?>"
    result = re.findall(pattern, text)
    print(result)

    # 匹配引号中的内容
    text = """She said "HaHa" and he said 'HiHi'"""
    result = re.findall(r'("|\')(.*?)\1', text)
    for _, res in result:
        print(res)

    # 匹配一个特定单词，但排除另一个,匹配所有 "apple"，但要排除 "pineapple"
    result = re.findall(r"\bapple\b", "there is an apple and a pineapple, haha apple")
    print(result)

    # 匹配一个重复的单词, 匹配像 "the the" 或 "is is" 这样连续出现的重复单词
    result = re.findall(r"\b(\w+)\s*\1\b", "ha ha ha you are so cute cute !")
    print(result)

    # 验证一个数字是否在 0-255 之间（模拟IP地址的一段）
    result = re.findall(r"25[0-9]\.2[0-4]\d\.[0-1]\d{2}", "IP: 255.249.1999043")
    print(result)

    # 将字符串 "Hello, {name}! Today is {day}." 中的 {name} 和 {day} 替换为变量 name 和 day 的值
    data = {'name': 'Alice', 'day': 'Monday'}
    text = "Hello, {name}! Today is {day}."
    result = re.sub(r'\{(\w+)\}', lambda match: data.get(match.group(1), ''), text)
    print(result)

    # 匹配一个 "q"，但其后不能紧跟一个 "u"。例如在 "Iraq" 中匹配 q，但在 "Queen" 中不匹配 Q
    text = "Iraq"
    text = "Queen"
    result = re.search(f"[Qq](?!u)", text)
    print(result.group() if result else "未匹配到数据")

    #  如何匹配嵌套的括号？例如匹配 (a(b(c)d)e) 中最内层的内容 (c) 或者整个结构
    # text = "(a(b(c)d)e)"
    # result = re.search(r'\(([^()]|(?R))*\)', text)
    # print(result.group() if result else "未匹配到数据")


