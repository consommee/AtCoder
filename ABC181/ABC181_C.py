import itertools
 
n=int(input())
Points = [list(map(int,input().split())) for _ in range(n)]
for p in itertools.permutations(Points, 3): #タプルで出力
  T = list(p)
  #print(T)
  if (T[0][0]-T[2][0])*(T[1][1]-T[2][1]) == (T[1][0]-T[2][0])*(T[0][1]-T[2][1]):
    print("Yes")
    exit()
print("No")