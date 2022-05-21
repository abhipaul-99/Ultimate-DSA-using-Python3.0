def flattenfun(arr):
    resultarr= []
    for item in arr:
        if type(item) is list:
            resultarr.extend(flattenfun(item))
        else:
            resultarr.append(item)
    return resultarr

print(flattenfun([1,2,3,[4,5,6],[[[[7]]]]]))
