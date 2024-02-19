# -*- coding:utf-8 -*-

"""
# File       : 6_删除并获得点数.py
# Time       : 2024/2/18 15:59
# Author     : ASUS
# version    : python 3.8
# Description: 给你一个整数数组 nums ，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#
#
#
# 示例 1：
#
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 示例 2：
#
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104
"""

import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 创建 nums中的值出现的次数 mapping. Key 为 nums[i], value 为 nums[i] 出现的次数
        numsMap = collections.Counter(nums)

        # nums 的最大的数字
        maxLen = max(numsMap.keys())
        # dp 数组从 1 开始计算, 0 空出来
        dp = [0] * (maxLen + 1)

        # 1 出现的次数之和
        dp[1] = 1 * numsMap[1]

        for i in range(2, maxLen + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * numsMap[i])
        return dp[-1]
