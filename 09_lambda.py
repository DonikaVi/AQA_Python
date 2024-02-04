"""
Hometask 14 lambda.

# Given: list of integers/floats with lambda function
#  as one of the element inside list
# Write function that will produce new list by applying
#  lambda to all integers and floats

"""

l1 = [lambda a: a + 2, 9, 3, 1, 0]
l2 = [9, 2, 3, lambda a: a / 2.0, 1, 0]


def func_list_lambda(data_list):
    """Do new list without lambda."""
    int_and_float = [el for el in data_list if type(el) in (int, float)]
    # find lambda in list (comparing the new list with the old one)
    for _, el in enumerate(data_list):
        if el not in int_and_float:
            lambda_el = el
    # using this lambda element to make new list
    output_list = [lambda_el(el) for el in int_and_float]
    return output_list


print(func_list_lambda(l1))
print(func_list_lambda(l2))
