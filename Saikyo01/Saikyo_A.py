a,b=map(int, input().split()) 
count=0
for i in range(2,a+1):
  for j in range(2,b+1):
    daylist = list(str(j))
    day1 = int(daylist[0])
    if len(daylist) != 1 :
      day2 = int(daylist[1])
      #print(day1 * day2)
      if i == day1 * day2:
        if day1 !=1:
          if day2 !=1:
            #print(str(i)+str(" ")+str(day1)+str(" ")+str(day2))
            count += 1
print(count)