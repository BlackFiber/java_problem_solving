#WAP to count the numbers of zero in the tuple a=(7,0,8,0,0,9)
a=(7,0,8,0,0,9)
print("Numbers of zero in the tuple = ",a.count(0))


#     OR you can also use the code written below

num_of_zero=0
for i in range(len(a)):
    temp=a[i]
    if temp==0:
        num_of_zero+=1

print("Total numbers of zero = ",num_of_zero)
