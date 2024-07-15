# Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    sum_target = 0
    increment = 0
    for j in range(len(nums)):
        increment = j + 1
        while increment < len(nums):
            sum_target = nums[j] + nums[increment]
            if(sum_target == target):
                return [j, increment]
            increment += 1

print(twoSum([2,5,5,11], 10))



    

        