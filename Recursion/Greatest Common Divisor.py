def gcd(x,y):
    assert int(x)==x and int(y)==y , 'Numbers should be integers.'
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(-18,48))
