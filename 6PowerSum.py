def powSum(array,pow=1):
    sum=0
    for i in array:
        if type(i)==list:
            sum=sum+powSum(i,pow+1)
        else:
            sum=sum+i

    return sum**pow

print(powSum([1,2,[3,4],[[2]]]))            