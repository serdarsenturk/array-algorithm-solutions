#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = []
        sum = 0
        
        
        for k in range(len(nums)):
            for m in range(k+1, len(nums)):
                
                sum = nums[k] + nums[m]
                
                if sum == target:
                    numbers.append(k)
                    numbers.append(m)
    
                        
        return numbers