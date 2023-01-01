#WAP to fill a letter template given below with name and date .
# letter = ''' Dear <name
#                       you are selected!
#                         <Date>'''

letter_template= '''Dear 
                        you are selected!
                                         '''
name=input("Pls enter the name : ")
date=input("Enter the current date : ")
print(letter_template[:4]," %s "%(name),letter_template[4:],"%s"%(date))