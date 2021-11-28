
#反向比较大小
#即先比较两个数组中最大的一项（最后一项）将较大者填充在nums1数组的最后方，作为结果数组的元素。一次比较填充一个元素，而每次比较中被填充者都是较大的元素，因此对应数组的剩余元素
#m/n就应该减一以表示一次比较完成。最后当m或n为0时表示其中一个用完了。
#此时若m=0表示nums1的元素用完了，而nums2中还有剩余，此时nums2中剩余元素已经时排好序的最小序列，直接填充在nums1的头部就行
#而n=0则表示nums2用完了，此时nums1中元素保持不同就好。


#此题主要在于打破传统从前往后排序的惯例。因为后方的数组是空的，因此从后往前不需要对前面的数组操作，更为简单。

nums1 = [2,0]
nums2 = [1]
m = 1
n = 1
"""
if n != 0 and m != 0:
    for i in range(len(nums2)):
        a = 0
        for j in range(1,(len(nums1) - 1)):
            if nums2[i] >= nums1[j - 1] and nums2[i] <= nums1[j + 1]:
                nums1.insert(j,nums2[i])
                a = 1
                break
            if nums2[i] <= nums1[j - 1]:
                nums1.insert(j - 1,nums2[i])
                
        if a != 1:
            nums1.append(nums2[i])
    
"""

while m > 0 and n > 0:
    if nums1[m - 1] > nums2[n - 1]:
        nums1[m + n -1] = nums1[m - 1]
        m -= 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1

if m == 0:
    nums1[: n] = nums2[: n]


print(nums1)

