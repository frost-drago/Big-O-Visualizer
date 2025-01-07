# A program to run your custom algorithm and store the time complexity in a JSON file.
# ONLY EDIT ON "EDITABLE 📝📝"!!!

import modules.commons as commons
import modules.settings as settings
import modules.sorting_algorithms as sorting
import msgspec
import time


# Load settings
time_limit = settings.config_1.get_time_limit()
max_num_of_data = settings.config_1.get_max_num_of_data()
data_range_list = commons.num_of_data_range_generator(settings.config_1.get_max_num_of_data())
number_of_trials = 5

# Datasets
result = {
    'data_nums':data_range_list[:],
    'average_result':[]
}

for trial_num in range(number_of_trials):
    result[f'result_{trial_num}'] = []

for num_of_data in data_range_list:
    print(num_of_data, end=" data \n")

    all_current_result = []
    for trial_num in range(number_of_trials):

        ########## EDITABLE 📝📝 ##########
        ########## Editable start ##########

        # generate something (for example, an unsorted list of numbers. See more on commons.)
        data_to_process = commons.random_list_generator_nonrepeating(num_of_data)

        # track time (DO NOT EDIT)
        time_start = time.time()

        # run an algorithm (for example, a sorting algorithm (or make your own). See more on sorting_algorithms.py.)
        sorting.bubble_sort(data_to_process)

        ########## EDITABLE 📝📝 ##########
        ########## Editable end   ##########

        time_end = time.time()
        time_diff = time_end - time_start
        
        result[f'result_{trial_num}'].append(time_diff)
        all_current_result.append(time_diff)

    # Calculate average
    average_current_results = commons.average_of_a_list(all_current_result)
    result['average_result'].append(average_current_results)

    if average_current_results > time_limit:
        result['data_nums'] = commons.get_list_until_number(data_range_list, num_of_data)
        break

# Put into file
file_object = open("data\\your_algorithm.json", "wb")
encoded = msgspec.json.encode(result)
file_object.write(encoded)
file_object.close()
