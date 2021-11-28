"""
重塑矩阵
将原矩阵拍扁之后根据x%column来将一维的数组中的元素映射至对应的维度中

知识点：
初始化多维数组 multilist = [[0 for col in range(5)] for row in range(3)  5*3每项为0的数组
"""

mat = [[1,2],[3,4]]
r = 4
c = 1
m, n = len(mat), len(mat[0])
if (m * n) == (r * c):
    m, n = len(mat), len(mat[0])
    unfold = []
    for i in range(m):
        for j in range(n):
            unfold.append(mat[i][j])
    ans1 = []
    ans2 = []
    for i in range(r * c):
        ans2.append(unfold[i])
        if ((i + 1) % c) == 0:
            ans1.append(ans2)
            ans2 = []
    print(ans1)


