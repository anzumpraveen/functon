def unique_list1(a):
    i=0
    x=[]
    while i<len(a):
        if a[i] not in x:
            x.append(a[i])
        i=i+1
    print('unique list is',x)
unique_list1([5,5,7,3,9,9,2,5,5,4,9,4,4,2,2,2,7,6,6])