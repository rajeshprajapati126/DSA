# Prime factorisation of a Number
# You are given an integer array queries of length n.
# Return the prime factorization of each number in array queries in sorted order.

# Example 1
# Input : queries = [2, 3, 4, 5, 6]

# Output : [ [2], [3], [2, 2], [5], [2, 3] ]
# Explanation : The values 2, 3, 5 are itself prime numbers.
# The prime factorization of 4 will be --> 2 * 2.
# The prime factorization of 6 will be --> 2 * 3.
# Example 2
# Input : queries = [7, 12, 18]
# Output : [ [7], [2, 2, 3], [2, 3, 3] ]

# Explanation : The value 7 itself is a prime number.

# The prime factorization of 12 will be --> 2 * 2 * 3.

# The prime factorization of 18 will be --> 2 * 3 * 3.

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