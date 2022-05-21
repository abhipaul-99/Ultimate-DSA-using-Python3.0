def productofArr(arr):
    if len(arr)== 0:
        return 1
    return arr[0] * productofArr(arr[1:])


print(productofArr([1,2,3,4]))
