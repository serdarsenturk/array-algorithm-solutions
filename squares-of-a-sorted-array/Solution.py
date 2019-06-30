class Solution(object):
    """
    This algoritm solves the following problem from LeetCode:
    https://leetcode.com/problems/squares-of-a-sorted-array/
    """
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        for index in range(len(A)):
            A[index] = A[index]**2
        
        for i in range(len(A)):
            for j in range(len(A)-1):
                if A[j] > A[j+1]:
                    temp = A[j+1]
                    A[j+1] = A[j]
                    A[j] = temp
                    
        return A
    