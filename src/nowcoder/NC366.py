#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/4/4 16:11
# @author: Mrwhite
# @File:NC366.py
# @DESC:

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型一维数组
#
class Solution:
    def sortedArray(self , nums):
        # write code here
        return sorted(num*num for num in nums)

solution=Solution()
res=solution.sortedArray([1,2,4])
print(res)