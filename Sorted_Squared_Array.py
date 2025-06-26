def sorted_squared_array(array):
    n=len(array)
    i=0
    j=n-1
    result_array=[0]*n
    print(result_array)
    for k in reversed(range(n)):
        if array[i]**2>array[j]**2:
            result_array[k]=array[i]**2
            i=i+1
        else:
            result_array[k]=array[j]**2
            j=j-1
    print(result_array)       

sorted_squared_array([-11,2,3,4])

