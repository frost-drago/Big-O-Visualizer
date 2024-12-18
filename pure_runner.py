# A program to run pure algorithms and store the time complexity in a JSON file.

import modules.pure_algorithms as pure_algorithms
import modules.commons as commons
import modules.settings as settings
import msgspec

# Load settings
time_limit = settings.config_1.get_time_limit()
number_of_trials = settings.config_1.get_number_of_trials()
data_range_list = commons.num_of_data_range_generator(settings.config_1.get_max_num_of_data())

# Datasets
result = {
    'data_nums':[],

    'data_num_0':0, 'result_0':[],
    'data_num_1':0, 'result_1':[],
    'data_num_2':0, 'result_2':[],
    'data_num_3':0, 'result_3':[],
    'data_num_4':0, 'result_4':[],
    'data_num_5':0, 'result_5':[],
    'data_num_6':0, 'result_6':[]
}

# Run the algorithms
cutoff = [0, 0, 0, 0, 0, 0, 0, 0]  # 1/True = Cutoff; 0/False = Run.
for i in data_range_list:
    print("Number of data:", i)

    # Generate a list
    my_list = list(range(1, i))

    # Put it in the list of data numbers
    result['data_nums'].append(i)

    if not cutoff[0]:
        sample_results = []
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_n_factorial(my_list))
        result_0 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_0'].append(result_0)
        # If over the time limit, stop calculation
        if result_0 > time_limit:
            result['data_num_0'] = i
            cutoff[0] = 1

    if not cutoff[1]:
        sample_results = []
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_2_to_the_power_of_n(my_list))
        result_1 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_1'].append(result_1)
        # If over the time limit, stop calculation
        if result_1 > time_limit:
            result['data_num_1'] = i
            cutoff[1] = 1

    if not cutoff[2]:
        sample_results = []
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_n_to_the_power_of_2(my_list))
        result_2 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_2'].append(result_2)
        # If over the time limit, stop calculation
        if result_2 > time_limit:
            result['data_num_2'] = i
            cutoff[2] = 1

    if not cutoff[3]:
        sample_results = []
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_n_times_log_n(my_list))
        result_3 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_3'].append(result_3)
        # If over the time limit, stop calculation
        if result_3 > time_limit:
            result['data_num_3'] = i
            cutoff[3] = 1

    if not cutoff[4]:
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_n(my_list))
        result_4 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_4'].append(result_4)
        # If over the time limit, stop calculation
        if result_4 > time_limit:
            result['data_num_4'] = i
            cutoff[4] = 1

    if not cutoff[5]:
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_log_n(my_list))
        result_5 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_5'].append(result_5)
        # If over the time limit, stop calculation
        if result_5 > time_limit:
            result['data_num_5'] = i
            cutoff[5] = 1

    if not cutoff[6]:
        for j in range(number_of_trials):
            sample_results.append(pure_algorithms.pure_1(my_list))
        result_6 = commons.average_of_a_list(sample_results)
        # Put it into dataset
        result['result_6'].append(result_6)
        # If over the time limit, stop calculation
        if result_6 > time_limit:
            result['data_num_6'] = i
            cutoff[6] = 1


# Put into file
file_object = open("data\\pure_algorithms.json", "wb")
encoded = msgspec.json.encode(result)
file_object.write(encoded)
file_object.close()
