str = input()
k=int(input())
freq={}
for i in range(len(str)-k+1):
  patt=str[i:i+k]
  freq[patt]=freq.get(patt,0)+1

mx_c=max(freq.values())
res=[patt for patt, count in freq.items() if count==mx_c]
print(*res)
