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