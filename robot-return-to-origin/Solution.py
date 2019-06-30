# Link - > https://leetcode.com/problems/robot-return-to-origin/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in range(len(moves)):
            
            if(moves[i] == 'L'):
                x -=1
            if(moves[i] == 'R'):
                x +=1
            if(moves[i] == 'U'):
                y +=1
            if(moves[i] == 'D'):
                y -=1
    
        return x == y == 0