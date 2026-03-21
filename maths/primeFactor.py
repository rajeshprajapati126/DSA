import math

class Solution:
    def find_factors(self,n):
        ans = []
        
        while n%2==0:
            ans.append(2)
            n = n // 2
        for i in range(3,int(math.sqrt(n))+1,2):

            while n%i == 0:
                ans.append(i)
                n = n // i
        if n>2:
            ans.append(n)
        return ans
    def primeFactors(self, queries):
        res = [ self.find_factors(i) for  i in queries]
        return res
print(Solution().primeFactors([2,3,5,6]))