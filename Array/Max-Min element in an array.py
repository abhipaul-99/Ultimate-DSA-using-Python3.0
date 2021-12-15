def maxmin(arr):
    mi = arr[0]
    ma = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<mi:
            mi = arr[i]
    for j in range(1,len(arr)):
        if arr[j]>ma:
            ma = arr[j]
    print("Min:",mi)
    print("Max:",ma)



arr = [5,8,2,6,9,99,14,23]
maxmin(arr)
