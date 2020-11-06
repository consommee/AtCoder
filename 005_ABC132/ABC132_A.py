import sys
 
str = str(input())
list = []
for c in str:
  list.append(c)
list.sort()
 
if list[0] == list[2]:
    print("No")
    sys.exit()
if list[0] == list[1]:
  if list[2] == list[3]:
    print("Yes")
    sys.exit()
print("No")