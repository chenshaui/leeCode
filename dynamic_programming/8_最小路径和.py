# -*- coding:utf-8 -*-

"""
# File       : 8_最小路径和.py
# Time       : 2024/2/19 11:14
# Author     : ASUS
# version    : python 3.8
# Description: 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if (not grid):
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]
        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
        return grid[-1][-1]
