# Dedicated to reusable functions.

import random

def get_list_until_number(a_list, target_number):
    '''
    Returns a subset of a list prior to a target number.
    - a_list = (list) list of numbers.
    - target_number = (int) number to mark as stop. 
                      If number is 0, return the whole list. 
                      If number is not 0 and is not found, return None.

    Examples:

        get_list_until_number([1, 2, 4, 8, 16, 32, 64, 128, 256], 8)
        will generate [1, 2, 4, 8]

        get_list_until_number([1, 2, 4, 8, 16, 32, 64, 128, 256], 128)  
        will generate [1, 2, 4, 8, 16, 32, 64, 128]
    '''
    if target_number == 0:
        return a_list[:]
    if target_number not in a_list:
        return None

    searched_index = a_list.index(target_number)
    result = a_list[:(searched_index + 1)]
    return result

def average_of_a_list(a_list):
    '''
    Returns the average value of a list containing numerical elements.
    - a_list = (list).
    '''
    return sum(a_list)/len(a_list)

def random_list_generator(list_length, min_int=0, max_int=10000):
    '''
    Generates a list containing random integers.
    - list_length = (int) resulting length of list.
    - min_int, max_int = (int, int) minimum and maximum values generated.
    '''
    a_list = []
    for i in range(list_length):
        a_list.append(random.randint(min_int, max_int))
    return a_list

def random_list_generator_nonrepeating(list_length):
    '''
    Generates a list of list_length length. The numbers are non-repeated and
    are shuffled. Smallest number is 1.
    - list_length = (int) resulting length of list.
    '''
    a_list = list(range(1, list_length + 1))
    random.shuffle(a_list)
    return a_list

def num_of_data_range_generator(max_number_of_data):
    '''
    Returns a list of data ranges (int) to test.
    1-50 ~55  : Increment by 1s
    50+  ~250 : Increment by 5s
    200+ ~1100: Increment by 50s
    1000+     : Increment by 100s
    - max_number_of_data = (int) maximum number of data, e.g. 4000

    Examples:

        num_of_data_range_generator(55)
        will generate [1,2,3,...,49,50,51,52,53,54,55]

        num_of_data_range_generator(200)
        will generate [1,2,3,...,49,50, 55,60,65,70,...,190,195,200]
    '''
    
    if max_number_of_data <= 0:
        raise ValueError("Number of data must be a positive number.")
    if max_number_of_data <= 55:
        return list(range(1, max_number_of_data + 1))
    elif max_number_of_data <= 250:
        return list(range(1, 51)) + list(range(55, max_number_of_data + 1, 5))
    elif max_number_of_data <= 1100:
        return list(range(1, 51)) + list(range(55, 201, 5)) + list(range(250, max_number_of_data + 1, 50))
    else:
        return list(range(1, 51)) + list(range(55, 201, 5)) + list(range(250, 1001, 50)) + list(range(1100, max_number_of_data + 1, 100))
