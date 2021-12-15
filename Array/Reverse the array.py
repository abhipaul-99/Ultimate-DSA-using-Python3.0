#Using Python List slicing
arr = [1,2,3,4,5]
print(arr[::-1])


#Iterative-method
def reverse(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1 
        end -=1 
    return arr

arr=[1,2,3,4,5]
print(reverse(arr))


#Recursive-method
def reverse(arr,start,end):
    if start >=end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr,start+1,end-1)

arr=[1,2,3,4,5]
reverse(arr,0,4)
print(arr)

#Using reverse()
arr = [1,2,3,4,5]
arr.reverse()
print(arr)
