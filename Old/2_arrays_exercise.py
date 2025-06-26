import numpy as np
monthly_exp=[2200,2350,2600,2130,2190]
total_quarter_expense=0
jan_feb_expenses=monthly_exp[1]-monthly_exp[0]
print("In Feb,{0} dollars were spent extra compared to January".format(jan_feb_expenses))
print("Total expense in first quarter (first three months) of the year is ",monthly_exp[0]+monthly_exp[1]+monthly_exp[2]  )
for i in range(3):
    total_quarter_expense=total_quarter_expense+monthly_exp[i]
print("Total expense in first quarter (first three months) of the year is {}".format(total_quarter_expense)  )
spent_mnths=[]
for i in range(len(monthly_exp)):
    if monthly_exp[i]==2000:
        spent_mnths.append(i)
    else:
        continue
if len(spent_mnths)>0:
    print("Exactly 2000 was spent in ",spent_mnths)    
else:
    print("Exactly 2000 was not spent in any month")  
print("Did I spend 2000 in any month?",2000 in monthly_exp)  
monthly_exp.append(1980)
monthly_exp.insert(len(monthly_exp),1980)
print("July month expenses added.Final Expenses list is ",monthly_exp) 
monthly_exp[3]=monthly_exp[3]-200    
print("April month expenses modified.Final Expenses list is ",monthly_exp) 

heros=['spider man','thor','hulk','iron man','captain america']
print("Length of list is :",len(heros))
heros.append('black panther')
print("New list after adding black pather at the end:",heros)
heros.pop()
print("black pather removed at the end:",heros)
heros.insert(heros.index("hulk")+1,'black panther')
print("black pather added after hulk:",heros)
#heros.remove("thor")
#heros.insert(heros.index("hulk"),"doctor strange")
#heros.remove("hulk")
heros[1:3]=["doctor strange"]
print("Final list:",heros)
heros.sort()
print("Final sorted list:",heros)

max_number=int(input("Enter max number:"))
odd=[]
for i in range(max_number):
    if i%2!=0:
        odd.append(i)
    else:
        continue
print("Odd numbers between 0 and {} are {}".format(max_number,odd))    


