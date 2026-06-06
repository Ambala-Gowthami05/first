"""# 1.Find last digit 
n = int(input("enter the number"))
m = n % 10
print(m)
#Remove last digit--1234 → 123
n = int(input("enter the number"))
print(n//10)
#Find last 2 digits--12345 → 45
n = int(input("enter the number"))
print(n%100)
#Find last 3 digits---987654 → 654
n = int(input("enter the number"))
print(n%1000)
#Check if number is even or odd
n = int(input("enter the number"))
if (n%2==0):
    print("even number")
else:
    print("odd number")
#Find first digit--- 4567 → 4
n = int(input("enter the number"))
while n>10:
    n=n//10
print(n)
#Count number of digits----4567 → 4
n = int(input("enter the number"))
count = 0
while n>0:
    n=n//10
    count+=1
print(count)
#Sum of digits--- 123 → 6
n = int(input("enter the number"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
#Product of digits---123 → 6
n = int(input("enter the number"))
product = 1
while n >0:
    digit = n%10
    product*=digit
    n=n//10
print(product)
#Reverse a number---123 → 321
n = int(input("enter the number"))
rev=0
while n>0:
    digit= n%10
    rev=rev*10+digit
    n=n//10
print(rev)
#Reverse last 2 digits------ 12345 → 12354
n = int(input("enter the number"))
first = n%10  #5
second = (n//10)%10  #4
last = n//100  #123
print(last*100+first*10+second)
#Swap first and last digit----1234 → 4231
n = int(input("enter the number"))
last = n%10   #4
first = n//1000 #1
middle = (n//10)%100  #1234//10 ---123%100--23
print(last*1000+middle*10+first)
#Remove first digit------ 1234 → 234
n= int(input("enter the number"))
m=n%1000
print(m)
#Extract middle digit (for 3-digit)------- 456 → 5
n= int(input("enter the number"))
middle=(n//10)%10# 5
print(middle)
# Check if number is 3-digit
n= int(input("enter the number"))
print(100<=n<=999)
#Check if number is n-digit
n = int(input("enter the number"))
count = 0
while n > 0:
    n=n//10
    count+=1
print(count)
#Check if first digit is even
n = int(input("enter the n"))
while n >= 10:
    n = n//10
if n%2==0:
    print("even")
else:
    print("odd")
#Check if last digit is 5
n= int(input("enter the number"))
if(n%10==5):
    print("true")
else:
    print("false")"""
#Check if sum of digits is even or odd
n = int(input("enter the number"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
if sum%2==0:
    print("even")
else:
    print("odd")


