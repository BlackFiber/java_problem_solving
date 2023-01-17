#WAP to store seven fruits in a list entered by the user.
fruits=[]
for i in range(7):
    if(i<1):
        n=input("Enter the fruit's name : ")
        fruits.append(n)

    else:
        n=input("Enter the next fruit's name : ")
        fruits.append(n)

print("Now the fruit's list is : ",fruits)
