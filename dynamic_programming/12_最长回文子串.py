# -*- coding:utf-8 -*-

"""
# File       : 12_最长回文子串.py
# Time       : 2024/2/22 15:04
# Author     : ASUS
# version    : python 3.8
# Description: 
"""


def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    res = 0
    left = 0
    right = 0
    for i, str_s in enumerate(s):
        l = i - 1
        r = i + 1
        # 奇数
        while (l >= 0) and (r < n) and (s[l] == s[r]):
            # 将长度设为r-l+1
            length = r - l + 1
            if length > res:
                left = l
                right = r
                res = length
            l -= 1
            r += 1
        # 偶数
        l = i
        r = i + 1
        while (l >= 0) and (r < n) and (s[l] == s[r]):
            # 将长度设为r-l+1
            length = r - l + 1
            if length > res:
                left = l
                right = r
                res = length
            l -= 1
            r += 1
    return s[left: right + 1]


longestPalindrome('babad')
