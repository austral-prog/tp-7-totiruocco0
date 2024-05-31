def index_of_by_index(word, lista, index):

    lista1= lista[index::]
    lista2= lista[:index:]
    lista= lista2+lista1
    for i,e in enumerate(lista1):
        if e==word:
            for o,e in enumerate(lista2):
                if e==word:
                    del lista2[o]
                    lista2.insert(i,"")
                    lista=lista2+lista1
    for u,e in enumerate (lista):
        if e==word and word in lista1:
            return u
    return -1
def index_of_empty(lista):
    for i,e in enumerate(lista):
        if e=="":
            return  i
    return -1
def index_of(word, lista):
    for i,e in enumerate(lista):
        if e==word:
            return i
    return -1
def put(word, lista):
    for i,e in enumerate(lista):
        if e=="":
            del lista[i]
            lista.insert(i,word)
            return i
    return -1
def remove(word, lista):
    nueva=[]
    for i,e in enumerate(lista):
        if e==word:
            del lista[i]
            lista.insert(i,"")
            nueva+=[""]
    return len(nueva)
