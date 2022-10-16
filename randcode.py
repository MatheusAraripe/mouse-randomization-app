import random

#print("Randomly selecting animals and separating them into distinct groups: \n")

#n = int(input("Enter the number of animals to be used:"))

def rand_func(n, x):

    groups_list = []
    contador = 1
    while contador <= n:
        contador = contador + 1

    L1 = list(range(1, contador))

    n = random.shuffle(L1)

    #print("Grouping animals randomly: \n")
    #x = int(input("Enter the number of groups into which the animals are to be divided:"))
    splited = [L1[i::x] for i in range(x)]


    for l in splited:
        groups_list.append(l)
    return groups_list
        #return(f'Group {i+1}:{l}')

