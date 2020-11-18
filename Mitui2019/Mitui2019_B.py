n=int(input())
 
orgin=int(1+n//1.08)
orgintax= int(orgin*1.08)
 
if orgintax==n:
  print(orgin)
else:
  print(':(')