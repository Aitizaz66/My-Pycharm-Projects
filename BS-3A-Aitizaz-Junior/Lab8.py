# write a recursive function that take embedded list and convert it into flat list and then return the list

def embedded_to_flat(a):
    flat_list = []
    if a == []:
        return 0
    else:
        for i in a:
            if type(i) == list:
                list_in_list = embedded_to_flat(i)
                for j in list_in_list:
                    flat_list.append(j)
            else:
                flat_list.append(i)
        return flat_list


print(embedded_to_flat([1, [2, 3, [4, 5], 6, 7], 8]))
