var_1 = int(input("Enter The First Number:"))
var_2 = int(input("Enter The Second Number:"))
print("1.for Addition +")
print("2.for Subtraction -")
print("3.for Multiplication X ")
print("4.for Division /")
print("5. for Exit/")
ch = int(input("Enter Your Choice:"))
choice = 0 
while ch != 5 or choice != 5  : 
    if ch == 1 :
        print("Addition of",var_1,"&",var_2,"is",var_1+var_2)
        #break
        
    elif ch == 2 :
        print("Substraction of",var_1,"&",var_2,"is",var_1-var_2)
        #break
        
    elif ch == 3 :
        print("Multiplication of",var_1,"&",var_2,"is",var_1*var_2)
        #break
        
    elif ch == 4 :
        print("Division of",var_1,"&",var_2,"is",var_1/var_2)
        #break
        
    else:
        print("Please Select Right Option")
    ch = int(input("Enter Your Choice Again:"))
    choice = ch 
print("Thanks For Using This.!")