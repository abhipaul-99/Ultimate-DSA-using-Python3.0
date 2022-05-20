def power(base,expo):
    assert expo>=0 and int(expo)==expo , 'Expo should be positive integer only!'    #Unintentional case
    if expo==0:                  #Base case
        return 1
    if expo==1:                  #Base case
        return base
    else:
        return base * power(base,expo-1)   # Recursive case

print(power(5,3))
