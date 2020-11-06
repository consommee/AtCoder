import fractions
 
a,b,c,d=map(int, input().split())
 
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
 
x =(b//c)-(((a-1)//c))
y =(b//d)-(((a-1)//d))
n =lcm(c,d)
xy=(b//n)-(((a-1)//n))
 
ans = (b-a+1) - (x+y-xy)
print(ans)