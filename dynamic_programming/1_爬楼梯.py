# -*- coding:utf-8 -*-

"""
# File       : 1_爬楼梯.py
# Time       : 2024/2/18 10:59
# Author     : ASUS
# version    : python 3.8
# Description: 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 示例 2：
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
"""

from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        if n == 2:
            return 2

        @cache
        def dfs(i: int):
            if i < 2:
                return 1
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)
