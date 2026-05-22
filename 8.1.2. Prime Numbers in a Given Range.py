s=int(input())
e=int(input())
f=0
for n in range(s,e+1):
    if n>1:
        p=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                p=0
                break
        if p:
            print(n)
            f=1
if f==0:
    print("No primes")
