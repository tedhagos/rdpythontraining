# project euler problem; 3 and 5 multiples under 1000
# This is the correct solution


def calc(end):
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


calc(1000)


# def foo(x):
#     if x % 3 == 0:
#         True
