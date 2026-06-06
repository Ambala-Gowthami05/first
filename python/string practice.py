"""#Given a string, print each character on a new line
name = input("enter the name")
for ch in name:
    print(ch)
#Find the length of a string using len()
name = input("enter the string")
print(len(name))
#Find the length of a string without using len()
name = input("enter the string")
count = 0
for ch in name:
    count+=1
print(count)
#Count number of vowels in a string.
k = input("enter the name")
count = 0
for ch in k:
 if ch in "aeiouAEIOU":
    count+=1
print(count)
#Count consonants (ignore spaces).
n = input("enter the string")
count = 0
for ch in n:
   if ch not in "aeiouAEIOU":
     count+=1
print(count)
#Reverse a string using slicing
n = input("enter the name")
rev = n [::-1]
print(rev)
#Reverse a string without using slicing
n= input("enter the name")
rev = " "
for ch in n:
    rev = ch+rev
print(rev)"""
#Convert lowercase letters to uppercase .upper()
n = input("enter the name")
print(n.upper())