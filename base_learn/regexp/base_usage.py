"""
正则表达式基本用法
\d 匹配任何十进制数字，等价于字符类 [0-9]
\D 匹配任何非数字字符，等价于字符类 [^0-9]
\s 匹配任何空白字符，等价于字符类 [ \t\n\r\f\v]
\S 匹配任何非空白字符，等价于字符类 [^ \t\n\r\f\v]
\w 匹配任何字母与数字字符，等价于字符类 [a-zA-Z0-9_]
\W 匹配任何非字母与数字字符，等价于字符类 [^a-zA-Z0-9_]
* 匹配0次或者多次
+ 匹配1次或者多次
？匹配0次或者1次
^ 只匹配字符开头,在MULTILINE模式中可以匹配在换行符之后的字符串内的任何位置 \A
$ 只匹配字符结尾,在MULTILINE模式中可以匹配在换行符之前的字符串内的任何位置 \Z
A|B 匹配任何与 A 或 B 匹配的字符串
\bclass\b 字边界
\B 不在字边界时才匹配
match() 确定正则是否从字符串的开头匹配。
search() 扫描字符串，查找此正则匹配的任何位置。
findall() 找到正则匹配的所有子字符串，并将它们作为列表返回。
finditer() 找到正则匹配的所有子字符串，并将它们返回为一个 iterator。
group() 返回正则匹配的字符串
start() 返回匹配的开始位置
end()   返回匹配的结束位置
span()  返回包含匹配 (start, end) 位置的元组
split() 将字符串拆分为一个列表，在正则匹配的任何地方将其拆分
sub()  找到正则匹配的所有子字符串，并用不同的字符串替换它们
subn() 与 sub() 相同，但返回新字符串和替换次数
[u4e00-u9fa5] 中文
"""
import re

# groups()方法用于返回所有捕获组的匹配结果组成的元组
m = re.match("([abc])+", "abc")
# 量词+匹配多次，groups()只返回最后一次捕获的字符（'c'），而非整个序列
print(m.groups())

# (?:...)语法表示非捕获组，匹配内容但不存储结果，优化性能
m = re.match("(?:[abc])+", "abc")
print(m.groups())

# (?P=name) 表示在当前点再次匹配名为 name 的组的内容，用于查找连续的重复单词的正则表达式
p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
print(p.search('Paris in the the spring').group())

# (?=…) 肯定型前视断言,如果内部的表达式（这里用 ... 来表示）在当前位置可以匹配，则匹配成功，否则匹配失败
s = re.search(r'\d+(?=元)', "价格100元，折扣50%") # 提取带单位的数字
print(s.group())
s = re.search(r'(?=.*[A-Z]).{8,}', "Pass12345")  # 匹配8位以上且包含大写字母的字符串
print(s.group())

# (?!…) 否定型前视断言
s = re.search(r'(?<!\.)\b\d+(?!\.)', "3.14 25 100.")  # 匹配后面不接"."的数字
print(s.group())

pattern = '[a-z]+'
text = "Paris in the the spring"
pattern = re.compile(pattern)
print(pattern.search(text).group())
res = pattern.split(text)
print("split: ", res)
res = pattern.sub("*", text)
print("sub: ", res)
res = pattern.subn("*", text)
print("subn: ", res)



token = '+-*/'
res = re.match(r"[+\-*/]+(?!\d)", token)
print(res)

re.match(r'[+\-*/]+(?!\d)', token)