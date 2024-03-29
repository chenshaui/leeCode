# -*- coding:utf-8 -*-

"""
# File       : 9_不同路径_带障碍.py
# Time       : 2024/2/19 13:27
# Author     : ASUS
# version    : python 3.8
# Description: 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#
#
# 示例 1：
#
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 示例 2：
#
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#
#
# 提示：
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 原矩阵版
        height, width = len(obstacleGrid), len(obstacleGrid[0])

        # 从上到下，从左到右
        for m in range(height):  # 每一行
            for n in range(width):  # 每一列
                if obstacleGrid[m][n]:  # 如果这一格有障碍物
                    obstacleGrid[m][n] = 0
                else:
                    if m == n == 0:  # 或if not(m or n)
                        obstacleGrid[m][n] = 1
                    else:
                        a = obstacleGrid[m - 1][n] if m != 0 else 0  # 上方格子
                        b = obstacleGrid[m][n - 1] if n != 0 else 0  # 左方格子
                        obstacleGrid[m][n] = a + b
        return obstacleGrid[-1][-1]
