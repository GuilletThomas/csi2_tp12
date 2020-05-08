def listSum(l):
    if len(l) == 0 :
        return 0
    elif len(l) ==1 :
        return l[0]
    else :
        n = l[0] + l[len(l)-1]  # additionne le dernier et le premier
        l[0] = n  # remplace le premier par l'addition des deux
        del l[len(l) - 1]  # supprime le dernier
        return listSum(l)





print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11