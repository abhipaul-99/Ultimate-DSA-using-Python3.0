#Using Iterative method
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




#Using Comparison
def maxmin(arr):
    maax=0
    miin = 0
    for i in range(len(arr)-1):
        z=max(arr[i],arr[i+1])
        if maax<z:
            maax=z
        x = min(arr[i],arr[i+1])
        if miin>x:
            miin=x
    print("Min:",miin)
    print("Max:",maax)


arr = [5,8,2,6,9,99,14,23]
maxmin(arr)
