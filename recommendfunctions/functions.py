def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left_list = [word for word in lst if word < pivot]
    right_list = [word for word in lst if word > pivot]
    left_sorted = quick_sort(left_list)
    right_sorted = quick_sort(right_list)
    return left_sorted + [pivot] + right_sorted

def type_dictionary(lst):
    counter = {}
    for type in lst:
        if type[0] in counter.keys():
            counter[type[0]] += [type]
        else:
            counter[type[0]] = [type]
    return counter

if __name__ == "__main__":

    print(type_dictionary(['german', 'japanese', 'vegetarian', 'french', 'african', 'american', 'barbecue', 'czech', 'chinese', 'thai',
         'mexican', 'indian', 'cafe', 'pizza', 'italian']))

        
