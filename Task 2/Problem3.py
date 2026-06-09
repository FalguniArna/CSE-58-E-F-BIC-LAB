str=input()
com={
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}
rev=""
for i in reversed(str):
  rev+=com[i]
print(rev)
