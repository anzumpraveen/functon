def add(a,b):
    x=a+b
    return x
def sub(c,d): 
    y=c-d
    return y
def mul(e,f):
    z=e*f
    return z
def div(g,h):
    m=g/h
    return m   
def opr_fun():
    if opr=="+":
        print(add(n,num))
    elif opr=="-":
        print(sub(n,num))
    elif opr=="*":
        print(mul(n,num))
    elif opr=="/":
        print(div(n,num))
    else:
        print("quit")
n=int(input("enter the num"))
num=int(input("enter the num"))
opr=input("enter the opr")
opr_fun()



