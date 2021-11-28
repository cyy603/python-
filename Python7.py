"""
有效的数独：
    哈希表解法：对需要查找到对象（行，列，九宫格）生成对应的哈希表，在将list中的数映射进哈希表的过程中，判断是否存在重复元素

    重点：
        如何根据单个点的坐标计算出其对应的九宫格编号，即sudu = (i // 3) * 3 + j // 3
"""
from collections import defaultdict
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a = True
row, col, sqrt = defaultdict(set), defaultdict(set), defaultdict(set)
for i in range(9):
    for j in range(9):
        if board[i][j] == ".":
            continue
        sudu = (i // 3) * 3 + j // 3
        if board[i][j] in row[i] or board[i][j] in sqrt[sudu] or board[i][j] in col[j]:
            a = False
            break
        row[i].add(board[i][j])
        col[j].add(board[i][j])
        sqrt[sudu].add(board[i][j])
print(a)