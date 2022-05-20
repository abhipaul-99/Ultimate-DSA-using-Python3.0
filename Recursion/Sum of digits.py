def digiSum(n):
    assert n>=0 and int(n)==n, 'Number should be positive integer'
    if n==0:
        return 0 
    else:
        return n%10 + digiSum(n//10)

print(digiSum(92548))
