#WAP to sum a list with 4 numbers
l=[]
n=int(input("How much numbers you want to enter ? : "))
for i in range(n):
    ele=int(input("Enter the integer  :"))
    l.append(ele)

sum=0
for i in range(len(l)):
    temp=l[i]
    sum+=temp
print("Total sum = {}".format(sum))