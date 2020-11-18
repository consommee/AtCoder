A=int(input())
NUMLIST = []
for i in range(1,10):
  for j in range(1,10):
    NUMLIST.append(i*j)
    
if A in NUMLIST:
  print('Yes')
else:
  print('No')