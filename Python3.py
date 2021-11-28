'''
两数之和
从头开始，以第一个数为起点向后选取数列（因为需要的是数列中两数的和，因此不存在缺漏的情况）
在之后的目标序列中若存在与target和起点元素之差相等的元素即为另外一个所需的数

主要感觉在考察对python各种函数的使用
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        for i in range(1,len(nums)):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j>=0:
            return [j,i]