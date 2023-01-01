#WAP to detect double spaces in a string
st=input("Enter the string/line/paragraph : ")
temp=st.find("  ")

if(temp>=0):
    print("Total %s Double spaces are present in this string."%(st.count("  ")))

else:
    print("Double spaces are not found in this string.")