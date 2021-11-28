"""
最大子序列和
"""

nums = [-1,-2]
count = 0
result = 0
start = 0
end = 0
temp = nums[0]
for i in range(len(nums) - 1):
    if nums[i] >=0:
        break
    else:
        max = nums[i]
        if max < nums[i + 1]:
            max  = nums[i + 1]
            result = max
        else:
            result = max
print(result)
for i in range(len(nums)):
    count += nums[i]
    if count >= result:
        result = count
        end += 1
    if count <= 0:
        count = 0
        start = i

print(result) 
        

                     