import itertools
 
a,b=map(int, input().split())
node = [list(map(int,input().split())) for _ in range(a)]
 
counter =0 
city = list(range(2,a+1))
for v in itertools.permutations(city, a-1):
  route = list(v)
  route.insert(0,1)
  route.append(1)
  #print(route)
  #print(node[route[0]][route[1]])
  sum=0
  for i in range(a):
    #print([route[i]-1],[route[i+1]-1],node[route[i]-1][route[i+1]-1])
    sum += node[route[i]-1][route[i+1]-1]
  #print(sum)
  if sum == b:
    counter += 1
        
print(counter)