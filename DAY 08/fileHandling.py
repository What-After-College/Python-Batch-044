f = open("ex1.txt","rt", encoding="utf8")

word=""
dic = {}
lis = ['i','we','you','they','he','she','it','is','are','was','were','on','the','its','it','them','for','',' ','if','in','a','an','you','of']
lines = f.readlines()
for line in lines:
    line = line.split()
    for i in line:
        if i in lis:
            continue
        if(i.isalpha()):
            i = i.lower()
            if(i in dic):
                dic[i]+=1
            else:
                dic[i]=1

print(dic)
f.close()

for i in sorted(dic.values()):
    print(i)

# new_dict = dict([(value, key) for key, value in dic.items()])
# print(new_dict)

# for i in sorted(new_dict.keys()):
#     print(i)
