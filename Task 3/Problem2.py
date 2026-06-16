str1=input().strip()
str2=input()
d=int(input())
v=[]
k=len(str1)
for i in range(len(str2)-k+1):
        c=0
        for j in range(k):
            if str1[j] != str2[i+j]:
                c+=1
            
        if c<=d:
                #v.append(str(i))
            print(str(i), end = " ")
                
