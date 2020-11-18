n=int(input())
i = 1
alllist = []
while i < n+1 :
  a,b=map(str, input().split())
  c = [a ,int(b),i]
  alllist.append(c)
  i += 1
alllist.sort(key=lambda x:(x[0],-x[1]),reverse=True)
alllist.reverse()
j = 0
while j < n :
  print(alllist[j][2])
  j += 1