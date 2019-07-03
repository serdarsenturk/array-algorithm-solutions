# link -> https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        i = 1
        
        while i < len(A):
            if A[i] > A[i -1 ]:
                i = i + 1
                
            else:
                return i - 1  #Fonksiyonun peak noktasını bulma mantığıyla yaptım