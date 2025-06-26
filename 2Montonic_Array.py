def monotonic_array_a(array):
   n=len(array)
   first=array[0]
   last=array[n-1]
   if n==0: return True
   if first<last:  #MI or not monotonic
      for k in range(n-1):
         if array[k]>array[k+1]: return False
         
   elif first==last: #constant same numbers or not monotonic
      for k in range(n-1):
         if array[k]!=array[k+1]: return False
   else:
      #MD or not monotonic
      for k in range(n-1):
         if array[k]<array[k+1]: return False
   return True




#Brute Force Method

def monotonic_array_b(array):
   x=array.copy()
   y=array.copy()
   x.sort()
   y.sort(reverse=True)
   if array==x or array==y :
      print("True")
   else:
      print("False")


def monotonic_array(array):
    #write code here
   flag=([all(array[i]<=array[i+1] for i in range(len(array)-1))]) or ([all(array[i]<=array[i+1] for i in range(len(array)-1))])
   print(flag)  
  

monotonic_array_a([21,2,23,4])
