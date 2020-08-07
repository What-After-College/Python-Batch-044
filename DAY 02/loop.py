# type of loops
# 1. for
# 2. while

# for loop ----------------------

# for i in "shubham":
#     print(i,end="")

# Q. count the vowels present in a string

# st = input()
# count = 0
# for i in st:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): # do the same procedure for capital letter also
#         count+=1  # count = count + 1 count-=2=> count=count-2
# print(count)


# range(1,10)- 

# for i in range(1,9,2):
#     print(i)

# Q. write a program to print all even number upto 500.
# for i in range(2,501,2):
#     print(i)

# for i in range(9,1,-1):
#     print(i)

# for i in range(1,-150,-1):
#     print(i)


# loop control statement

# continue 
# break

# for i in range(1,11):
#     if(i==5):
#         print(i)
#         continue
        

# for i in range(1,11):
#     print(i)
#     if(i==5):
#         break


# Q. Print a design like it:
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='') 
#     print()

# 54321
# 4321
# 321
# 21
# 1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print("")


# while ------------

# i=0
# while(i<10):
#     print(i)
#     i+=1


# Q. 
# *****
# ****
# ***
# **
# *

# print('*'*6)

# numofstar=int(input())
# while(numofstar>0):
#     if(numofstar==1):
#         print(numofstar*'*',end='')
#         numofstar-=1
#         continue
#     print(numofstar*'*')
#     numofstar-=1

# git version control system


# Q. find the factor of a given number.

# n=int(input())
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

# Q find HCF of two given numbers.
# Q find LCM of two given numbers.

# n1 = int(input())
# n2 = int(input())
# if(n1>n2):
#     small=n2
# else:
#     small=n1
# for i in range(1,small+1):
#     if(n1%i==0 and n2%i==0):
#         hcf=i

# print(hcf)

# a = int(input())
# b = int(input())
# if(a>b):
#     g=a
# else:
#     g=b
# while(True):
#     if(g%a==0 and g%b==0):
#         lcm=g
#         break
#     g=g+1

# print(lcm)


# lcm  = product of number / hcf

# n1 = int(input())
# n2 = int(input())
# if(n1>n2):
#     small=n2
# else:
#     small=n1
# for i in range(1,small+1):
#     if(n1%i==0 and n2%i==0):
#         hcf=i

# lcm = (n1*n2)/hcf

# print(lcm)


# Q find the given number is prime or not

# n = int(input())
# factor=0
# for i in range(2,n):
#     if(n%i==0):
#         factor+=1
#         break
# if(factor>0):
#     print("not a prime")
# else:
#     print("the number is prime")


# Q. find the sum of first n number
# example: n= 5
# print(5+4+3+2+1)


n =  int(input())
c=0
# for i in range(1,n+1):
#     c+=i
c=n*(n+1)/2
print(c) # cntrl + /

# AP(arithmatic progression)
# n*(n+1)/2
