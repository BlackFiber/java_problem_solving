#WAP to accept maarks of 6 students and display them ina sorted order
marks=[]

def marks_input():
    m = int(input("Enter the student marks : "))
    marks.append(m)

for i in range(6):
    if(i<1):
        marks_input()

    else:
        marks_input()

marks=marks.reverse()

print(marks)