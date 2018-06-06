# project euler problem; 3 and 5 multiples under 1000
# This is the correct solution


def calc_decl(end):
    numlist = range(1, end)
    # find all the multiples of 3 < 1000
    list_3 = list(filter(lambda x: x % 3 == 0, numlist))
    # find all the multiples of 5 < 1000
    list_5 = list(filter(lambda x: x % 5 == 0, numlist))

    # now, we need to combine the two lists above, but ensure
    # that there are no duplicates
    combined_list = list_3 + [i for i in list_5 if i not in list_3]
    print(combined_list)
    print(sum(combined_list))


def calc_imp(end):
    numlist = range(1, end)
    list_3 = list(filter(lambda x: x % 3 == 0, numlist))
    list_5 = list(filter(lambda x: x % 5 == 0, numlist))
    temp_list = []

    for i in list_5:
        if i not in list_3:
            temp_list.append(i)

    combined_list = list_3 + temp_list
    print(combined_list)
    print(sum(combined_list))


# calc_decl(1000)
calc_imp(1000)

