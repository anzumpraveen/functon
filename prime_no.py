def prime_no(n):
    i=2
    while i<n:
        if n%i==0:
            print("not prime")
            break
        i+=1
    else:
        print("prime",n)
num=int(input("entr the number :"))
prime_no(num)

# second soulation

def even(a):
    if a%2==0:
        return a
    else:
        return a
n=int(input("enter the num"))
d=even(n)
# print(d)
def prime(d):
    i=1
    c=0
    while i<=d:
        if d%i==0:
            c+=1
        i+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
prime(d)