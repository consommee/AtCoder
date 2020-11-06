n=int(input())
text=str(input())
half=int(n/2)
text1 = text[0:half]
text2 = text[half:n]
if text1 == text2:
  print("Yes")
else:
  print("No")