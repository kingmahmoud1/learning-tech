arr=[1,4,7,9]
def add_num(new_p,new_num):

    arr.append(new_p)
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=new_num
    return
add_num(0,18)
print(arr)