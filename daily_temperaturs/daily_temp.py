# https://neetcode.io/problems/daily-temperatures/question?list=neetcode150
class Solution:
    def dailyTemperatures(self, temperatures):  # List[int] -> List[int]
        result = []
        k = 0

        for i in range(len(temperatures)-1):
            for ii in range(i + 1, len(temperatures)):
                k += 1
                if temperatures[i] < temperatures[ii]:
                    result.append(k)
                    k = 0
                    break
            if k != 0:
                result.append(0)
                k = 0
        
        result.append(0)

        return result
        

k = input().split()

abs = Solution()

print(abs.dailyTemperatures(k)) #