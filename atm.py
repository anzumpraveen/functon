trn=["withdrawl","deposit","checking balance","quit"] 
balance=10000
def main_fun():
    print("welcom")
    print("insert your card card") 
def printopt_fun():
    i=0
    while i<len(trn):
        print(i+1,trn[i])
        i+=1
def option_fun(opt):
    if opt==1:
        withdral_fun()
    elif opt==2:
        deposit_fun()
    elif opt==3:
        checking_fun()            
    elif opt==4:
        quit_fun()       
def withdral_fun():
    amt=int(input("enter the amount"))
    pin=int(input("enter the pin"))
    if pin==1234:
        x=balance-amt
        print("collact your case")
        print("in your bank",x,"is left")
    else:
        print("wrong pin")
   
def deposit_fun():
    amt1=int(input("how much you want to deposit"))
    pin=int(input("enter the pin"))
    if pin==1234:
        y=balance+amt1
        print("your deposit is successful")
        print("now your balance is",y)
    else:
        print("wrong pin")
def checking_fun():
    pin=int(input("enter the pin"))
    if pin==1234:
        print("your balance is",balance)
    else:
        print("wrong pin")
def quit_fun():
    print("quit")
main_fun()
lan=input("enter the language")
opt=int(input("enter any option"))
option_fun(opt)









