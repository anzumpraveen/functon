def max_num(num_list):
    max=0
    sec_max=0
    i=0
    while i<len(num_list):
        if num_list[i]>max:
            sec_max=max
            max=num_list[i]
        i+=1
    print("max number of list",max,sec_max)
max_num([7,3,8,12,5,8])