# 入力

```python:input.py
n=int(input())	#1つのとき
n,m=map(int, input().split())	#2つ以上の時
c=list(map(int, input().split()))	#リストの時
T = [list(map(int,input().split())) for _ in range(a)] #二次元配列の時、aは長さ
```

# Tips
**計算** <br>
べき乗
```python:exp.py
import math
math.pow(n,m) #n^m
```

ルート <br>

```python:root.py
import math
math.sqrt(n)
```

約数の列挙<br>

```python:
#nを約分したい数とする
i=1
table=[]
while i*i<=n:
  if n%i == 0:
    table.append(i)
    table.append(n//i)
  i+=1
table = list(set(table))
table.sort()
```

**組み合わせ** <br>
参考：https://note.nkmk.me/python-math-factorial-permutations-combinations/<br>

順列の全列挙　<br>

```python:permtation.py
import itertools
for v in itertools.permutations(List, n): #タプルで出力
  T = list(v)
```