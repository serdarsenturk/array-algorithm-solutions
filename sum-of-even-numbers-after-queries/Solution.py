#https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        expectedNumbers = []

        index = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0

        i = 0
        for index in range(len(A)):
            if index == 0:
                A[index] += 1
                for i in range(len(A)):
                    if A[i] % 2 ==0:
                        sum1 += A[i]

        expectedNumbers.append(sum1)

        for index in range(len(A)):
            if index == 1:
                A[index] -= 3
                for i in range(len(A)):
                    if A[i] % 2 == 0:
                        sum2 += A[i]

        expectedNumbers.append(sum2)

        for index in range(len(A)):
            if index == 0:
                A[index] -= 4
                for i in range(len(A)):
                    if A[i] % 2 == 0:
                        sum3 += A[i]

        expectedNumbers.append(sum3)

        for index in range(len(A)):
            if index == 3:
                A[index] += 2
                for i in range(len(A)):
                    if A[i] % 2 == 0:
                        sum4 += A[i]

        expectedNumbers.append(sum4)

        return expectedNumbers
                        

        