"""
赎金信：
    法一：
        使用哈希表储存杂志中的字符串，并记录个数
        在赎金信中查找存在的字符串，找到一个个数减一
ransomNote ="aa"
magazine = "aab"        
dict = {}
a = True
for i in range(len(magazine)):
    if magazine[i] in dict:
        dict[magazine[i]] += 1
    else:
        dict[magazine[i]] = 1
     
for i in range(len(ransomNote)):
    if ransomNote[i] in dict and dict[ransomNote[i]] != 0:
        dict[ransomNote[i]] -= 1
    else:
        a = False
print(a)
    法二（究极简单）：
        使用python内部自带的Counter类
        将两个字符串储存在counter类中
        利用其自带的交集查找方法，返回对应布尔值
        但是注意，使用Counter类前应导入
        From collection import Counter
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        if (a & b) == a:
            return True
        else:
            return False
#更简单的写法 return (a & b) == a