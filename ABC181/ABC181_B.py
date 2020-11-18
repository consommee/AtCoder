n=int(input())
sums = 0
for i in range(n):
  a,b=map(int, input().split())
  sums += (a+b)*(b-a+1)/2
print(int(sums))