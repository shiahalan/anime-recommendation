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

def restaurant_dictionary(lst):
    rest_dict = {}
    for restaurant in lst:
        if restaurant[0] not in rest_dict.keys():
            rest_dict[restaurant[0]] = [restaurant[1:]]
            continue
        rest_dict[restaurant[0]] += [restaurant[1:]]
    return rest_dict

if __name__ == "__main__":

    print(type_dictionary(['german', 'japanese', 'vegetarian', 'french', 'african', 'american', 'barbecue', 'czech', 'chinese', 'thai',
         'mexican', 'indian', 'cafe', 'pizza', 'italian']))

        
