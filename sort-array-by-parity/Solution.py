# -> https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1
        even = 0
        
        result = [1]*len(A)
        
        for number in A:
            if number % 2 == 0:
                result[even] = number
                
                even += 2
                
            else:
                result[odd] = number
                odd += 2
                        

        return result
                
        