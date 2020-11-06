n,m,k = map(int,input().split())	
point= list(map(int,input().split()))
 
temp=n*k-sum(point)
#print(temp)
if temp < 0:
  print(0)
elif temp > m:
  print(-1)
else:
  print(temp)