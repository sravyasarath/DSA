def findtheWinner(n,k):
    arr=[i+1 for i in range(n)] #Create array with n numbers
    print(arr)
    def helper(arr,start_index):
        if len(arr)==1:
            return arr[0]
        index_to_remove=(start_index+k-1)%len(arr)
        del arr[index_to_remove]
        return helper(arr,index_to_remove)
    return helper(arr,0)

def findtheWinner_2(n,k):
    def helper(n):
        if n==1:
            return 0
        else:
            return (helper(n-1)+k)%n
    return helper(n)+1


def findtheWinner_3(n,k):
    survivor=0
    for i in(2,n+1):
        survivor=(survivor+k)%i

    return survivor+1    

w=findtheWinner_3(5,3) 
print("Winner is:",w)