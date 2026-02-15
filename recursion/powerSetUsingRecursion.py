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