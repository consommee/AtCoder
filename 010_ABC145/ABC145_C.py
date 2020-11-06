import math
import copy
 
n=int(input())
originmap=[] #appendのために宣言が必要
while True:
    try:
        originmap.append(list(map(int,input().split())))
 
    except:
        break;
        #または、quit(),os.exit()をして止める。
 
length = 0
submap = originmap.copy()
for i,j in originmap:
  del submap[0]
  for a, b in submap:
    #print(submap)
    #print(i,j,a,b)
    length += math.sqrt((i-a)**2 + (j-b)**2)
 
print(length*2/n)