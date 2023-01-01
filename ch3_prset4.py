#Replace the double spaces from any string
st=input("Enter the string/line/paragraph : ")
if(st.count("  ")>0):
    print(st.replace("  "," "))

else:
    print(st)