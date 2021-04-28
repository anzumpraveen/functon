def even(list):
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i+=1
    print(a)
even([5,8,90,21,2,4,5,6,7])
