"""
不重复的第一个字符：
    通过使用哈希表，对遍历的字符串进行查找，如果存在重复的直接将其对应的value值设置为比长度长的任意值，并添加对应的key
    如果不存在则添加对应的key值和其对应的index
    最后查找哈希表中最小的value值，如果value值小于长度，则返回如果大于长度，返回-1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        dict = {}
        for i in range(length):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                dict[s[i]] = length + 1
        res = min(dict.values())
        if res > length:
            return -1
        else:
            return res
