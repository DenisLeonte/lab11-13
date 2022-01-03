def sort(lista, criteriu):
    for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if criteriu(i,j):
                    lista[i],lista[j]=lista[j],lista[i]