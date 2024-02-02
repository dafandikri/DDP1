from math import *

n = 1049693509496628609480609309973408001330404205776632857240753
a = ceil(sqrt(n))
while True:
    b2 = a*a - n
    if sqrt(b2) == int(sqrt(b2)):
        b=int(sqrt(b2))
        break
    a=a+1

p=a+b
q=a-b
print(int(p))
print(int(q))
if p*q == n:
    print("True")