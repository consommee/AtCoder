# 入力

```python:input.py
n=int(input()	#1つのとき
n,m=map(int, input().split())	#2つ以上の時
c=list(map(int, input().split()))	#リストの時
T = [list(map(int,input().split())) for _ in range(a)] #二次元配列の時、aは長さ
```

# Tips
**計算** <br>
ルート

```python:root.py
import math
 math.sqrt(n)
```

**組み合わせ** <br>
参考：https://note.nkmk.me/python-math-factorial-permutations-combinations/　<br>

順列の全列挙　<br>

```python:permtation.py
import itertools
for v in itertools.permutations(List, n): #タプルで出力
  T = list(v)
```