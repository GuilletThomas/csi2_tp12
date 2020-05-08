def product(a,b):
    if b == 0:
        return 0
    elif b == 1 :
        return a
    else :
        return product(a,b-1)+a


print(product(5,2)) # 10
print(product(9,3)) # 27