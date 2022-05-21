def sumofRange(num):
    if num <= 0:
        return 0
    return num + sumofRange(num - 1)


print(sumofRange(10))
