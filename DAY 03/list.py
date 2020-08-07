# list are array like data structure.

# student1=50
# student2=100
# student3=

# lis = [50, 100, 80, 40, 'neeraj',[1,2,3,[5,4,8,9]]]

# print(lis[4])
# print(lis[5][1])
# print(lis[5][3][2])

# lis=[1,2,3]

# print(lis)

# lis.append(8)

# print(lis)

# lis=[1,2,3]

# print(lis)

# lis[1]=5

# print(lis)


# lis = [1,2,3,4,5]

# print(lis)

# del(lis[3])

# print(lis.pop())


# # list slicing

# lis = [0,1,2,3,4,5,6,7,8,9,10,11,12]

# # print(lis[2:10])

# # print(lis[2:-3])

# # print(lis[-1:-1])

# # print(lis[5:])

# # for i in lis:
# #     print(i)

# # functions------------


# # def iseven(n):
# #     if(n%2==0):
# #         return 2
# #     else:
# #         return False




# # n = 5
# # print(iseven(n))

# # n=4
# # print(type(iseven(n)))

# # def f_to_c(f):
# #     return (f-32)*5/9



# # f = float(input())
# # c = f_to_c(f)
# # print(c)


# # length = int(input())
# # breadth = int(input())

# # def about_rec(length, breadth):
# #     return length*breadth, 2*(length+breadth)

# # area, perimeter = about_rec(length, breadth)
# # print(area, perimeter)

# # power(2,3)


# def power(base, exp):
#     if(exp==0):
#         return 1
#     else: 
#         return base * power(base, exp-1)



# ans=power(2,4)
# print(ans)



# st = ['5','4','9']
# print(st)


# lis = [int(i) for i in st]


# print(lis)

# lis=[]
# for i in range(4):
#     tmp = int(input())
#     lis.append(tmp)
# print(lis)


line = "3 2 1 3"

lis = line.split()

print(lis)

lis = [int(i) for i in lis]

print(lis)

