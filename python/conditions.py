num = int(input("enter the num"))
if num%2 == 0:
    print("even number")
else:
    print("odd number")
#elif statement
num = int(input("enter the number"))
if num<0:
    print("invalid")
elif num%2 ==0:
    print("even number")
else:
    print("odd number")
#is instance( , )---check type of variable
num = 10
print(isinstance(num, int))
