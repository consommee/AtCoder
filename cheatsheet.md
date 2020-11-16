# 入力

```python:input.py
n=int(input()	#1つのとき <br>
n,m=map(int, input().split())	#2つ以上の時  <br>
c=list(map(int, input().split()))	#リストの時 <br>
T = [list(map(int,input().split())) for _ in range(a)] #二次元配列の時、aは長さ <br>
```

# ライブラリ


組み合わせ　<br>

```python:permtation.py
import itertools　<br>
for v in itertools.permutations(List, n): #タプルで出力　<br>
  T = list(v)　<br>
```