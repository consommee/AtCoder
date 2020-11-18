num=int(input()) 
song=[]
length=[]
for i in range(num):
  n, m = input().split()
  song.append(n)
  length.append(int(m))
last=str(input())
songindex=song.index(last)
print(sum(length[songindex+1:num]))