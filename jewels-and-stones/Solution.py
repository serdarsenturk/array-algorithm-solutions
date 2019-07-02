#link -> https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        newLetter = []
        for k in range(len(J)):
            for m in range(len(S)):
                if J[k] == S[m]:
                    newChar = J[k]
                    newLetter.append(newChar)

        
        return len(newLetter)