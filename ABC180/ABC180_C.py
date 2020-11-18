n=int(input())
 
i=1
table=[]
while i*i<=n:
  if n%i == 0:
    table.append(i)
    table.append(n//i)
  i+=1
table = list(set(table))
table.sort()
for i in table:
  print(i)