# -> https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] == A[j]:
                    nTimes = A[i]
                    return A[i]