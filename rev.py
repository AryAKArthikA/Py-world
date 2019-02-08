p=int(input("enter the number"))
r=0
while (p>0):
    s=int(p%10)
    r=r*10+s
    p=int(p/10)
print(r)
