n = int(input())
c = list(map(int, input().split()))
count=0
for i in range(1, n-1):
  temp = []
  temp.append(c[i-1])
  temp.append(c[i])
  temp.append(c[i+1])
  temp.sort()
  if c[i] == temp[1]:
    count += 1
    
print(count)