n=str(input())
length = len(n)
 
ans=0
for i in range(length//2):
  if n[i]==n[-i-1]:
    ans+=0
  else:
    ans+=1
print(ans)