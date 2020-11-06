n=int(input())
list=list(map(int, input().split()))
 
list.sort()
 
B = int((n/2)-1)
A = int((n/2))
 
if list[B] == list[A]:
  print("0")
else:
  count = list[A] - list[B] 
  print(count)