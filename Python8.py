"""
矩阵置零：
    首先查找一个矩阵中0的位置
    在对每个矩阵中的0所在的行列进行置零操作
要点：
    将表示位置的list中每个值对应的索引映射到对应点的标号上。
    即：i == zeros[2*k - 2] or j == zeros[2*k - 1]:
"""
matrix = [[1,1,1],[1,0,1],[1,1,1]]
zeros = []
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            zeros.append(i)
            zeros.append(j)
for k in range(1,len(zeros)//2 + 1):
    for i in range(m):
        for j in range(n):
            if i == zeros[2*k - 2] or j == zeros[2*k - 1]:
                matrix[i][j] = 0
print(matrix)