# -*- coding:utf-8 -*-

"""
# File       : 11_下降路径最小和.py
# Time       : 2024/2/21 10:35
# Author     : ASUS
# version    : python 3.8
# Description: 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
#
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
#
#
#
# 示例 1：
#
#
#
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：如图所示，为和最小的两条下降路径
# 示例 2：
#
#
#
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：如图所示，为和最小的下降路径
#
#
# 提示：
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
"""

from math import inf
from typing import List
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # dfs(r, c) 表示从 matrix[r][c] 出发，向上走到第一行的最小路径和
        @cache  # 记忆化搜索
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:  # 出界
                return inf
            if r == 0:  # 到达第一行
                return matrix[0][c]
            return min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]

        return min(dfs(n - 1, i) for i in range(n))  # 枚举起点，取最小值
