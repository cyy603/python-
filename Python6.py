"""
杨辉三角
运用杨辉三角的特性：
    1.第n行就有n个元素
    2.每行需要进行加法操作的元素个数为n-2个
    3.ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
"""


numRows = 5
ans = [[1]]
for i in range(1, numRows):
    ans.append([1])
    for j in range(1, i):
        ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
    ans[i].append(1)
print(ans)