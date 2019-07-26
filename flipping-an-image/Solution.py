# link -> https://leetcode.com/problems/flipping-an-image/

class Solution(object):
    def flipAndInvertImage(self, A):
        
        lenA = len(A)
        lenSubA = len(A[0])
        
        for i in range(0, lenA):
  
            A[i] = A[i][::-1]
    
            for j in range(0, lenSubA):
                if(A[i][j] == 0):
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        
        return A