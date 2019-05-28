def sort (list):
    if len(list)==1:
        return list

    list_t=list
    i=len(list)-1

    while i>0:
        if list[i]<list[i-1]:
            list.insert(i-1, list.pop(i))
        i-=1

    if list==list_t:
        return list
    else:
        li = sort (list[1:])
        del list[-1:0:-1]

        for k in range (0, len(li)):
            list.append(li[k])

        return list

list=[]

print("Ваш отсортированный список:", sort(list), sep="\n")
