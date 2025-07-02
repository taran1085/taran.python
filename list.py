n=int(input("how long list you want:"))
num_list=[]
for i in range(n):
    num=int(input("enter a number: "))
    num_list.append(num)


max_value=max(num_list)
min_value=min(num_list)
print("maximum values :" ,max_value)
print("minimum values :" ,min_value)




