str1=input()
str2=input()
l=[]
for i in range(len(str1)-len(str2)+1):
    if set(str1[i:i+len(str2)])==set(str2):
        l.append(i)
print(l)