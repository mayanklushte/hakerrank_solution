t=int(input())
def ar(x):
    return x*(x+1)
for i in range(t):
    n =int(input())
    n -=1
    a=int(n/3)
    b=int(n/5)
    c=int(n/15)
    print(int(int(3*ar(a) + 5*ar(b) - 15*ar(c))>>1))


# my code with limitation's
"""n = int(input())
for _ in range(0, n):
    a = int(input())
c = []

for i in range(0, a):
    if i%3 == 0 or i%5==0:
        c.append(i)
    print(sum(c))
    c.clear()

"""

