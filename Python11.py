"""
字母异位词：
    没啥说的，Counter类yyds，究极无脑
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a == b
