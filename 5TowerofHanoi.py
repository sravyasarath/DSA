def toh(N,fromm,to,aux):
    count=0
    def helper(N,fromm,to,aux):
        nonlocal count
        #basecase
        if N==1: 
            print("move disk "+str(N)+" from rod "+str(fromm)+" to rod "+str(to))
            count+=1
            return
        #recursive case    
        helper(N-1,fromm,aux,to)
        print("move disk "+str(N)+" from rod "+str(fromm)+" to rod "+str(to))
        count+=1
        helper(N-1,aux,to,fromm)
    helper(N,fromm,to,aux)    
    return count

print(toh(5,1,2,3))