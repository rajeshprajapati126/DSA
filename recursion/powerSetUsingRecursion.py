# Power Set Using Recursion

"""
Difficulty: EasyAccuracy: 47.78%Submissions: 46K+Points: 2
You are given a string. You need to return the power-set (in any order) of the string.
Note: The string s contains lowercase letter of alphabet.

Examples:

Input: s = a
Output: ["","a"]
Explanation: empty string and "a" are only sets.
Input: s = abc
Output: ["", "a", "ab", "abc", "ac", "b", "bc", "c"]
Explanation: empty string, a, ab, abc, ac, b, bc, c are the sets.
Constraints:
1 ≤ s.length() ≤ 10
"""
def solve(ip,op,i,res):
    if i==len(ip):
        res.append(op)
        return res
    op1 = op + ip[i]
    op2 = op
    i+=1
    solve(ip,op1,i,res)
    solve(ip,op2,i,res)
    return res
def powerSet( s):
    #code here
    res = []
    
    return solve(s,'',0,res)
print(powerSet('abc'))