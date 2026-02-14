def toh( N, from_, to, aux,count=0):
        # Your code here
        if N==0:
           
            return 0
        li=toh(N-1,from_,aux,to,count)
        print("move disk "+ str(N) +" from rod "+str(from_)+" to rod " +str(to))
        mi=toh(N-1,aux,to,from_,count)
        
        return li+mi+1
print(toh(3,1,2,3,0))