def convertTO_binary(x):
    ans=''
    while x!=1:
        if x%2==1:
            ans+='1'
        else:
            ans+='0'
        x=x//2
    ans+='1'
    return ans[::-1]
def convertTO_decimal(n):

    leng=len(n)
    ans=0
    p2=1
    for i in range(leng-1,-1,-1):
        if n[i]=='1':
            ans += p2
        p2=2*p2
    return ans
n=32
print(convertTO_decimal(convertTO_binary(n)))
