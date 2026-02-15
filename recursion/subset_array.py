"""
Question: 74: Subset
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

def solve(nums,op,res):
    if len(nums)==0:
        res.append(op)
        return 
    op1 = op
    op2 = op[:]
    op1.append(nums[0])
    solve(nums[1:],op1,res)
    solve(nums[1:],op2,res)
def subsets(nums):
    res=[]
    solve(nums,[],res)
    return res
print(subsets([1,2,3]))
