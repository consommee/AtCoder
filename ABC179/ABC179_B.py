n=int(input())
counter=0
for i in range(n):
  a,b=map(int, input().split())
  if a==b:
    counter+=1
    if counter==3:
      print("Yes")
      exit()
  else:
    counter=0
print("No")