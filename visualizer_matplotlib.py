# Visualizer in MatPlotLib

import modules.commons as commons
import modules.settings as settings
import msgspec
import matplotlib.pyplot as plt

# Load settings
colors = settings.config_1.get_colors()
number_of_trials = settings.config_1.get_number_of_trials()

# Get pure algorithm results
file_object = open("data\\pure_algorithms.json", "rb")
contents = file_object.read()
pure_result = msgspec.json.decode(contents)
file_object.close()

x0, x1, x2, x3, x4, x5, x6 = [commons.get_list_until_number(pure_result['data_nums'], pure_result[f'data_num_{num}']) for num in range(7)]
y0, y1, y2, y3, y4, y5, y6 = [pure_result[f'result_{num}'] for num in range(7)]

# Plot in pure algorithm results
plt.plot(x0, y0, label="O(n!)",       color=colors[0])
plt.plot(x1, y1, label="O(2^n)",      color=colors[1])
plt.plot(x2, y2, label="O(n^2)",      color=colors[2])
plt.plot(x3, y3, label="O(n log(n))", color=colors[3])
plt.plot(x4, y4, label="O(n)",        color=colors[4])
plt.plot(x5, y5, label="O(log(n))",   color=colors[5])
plt.plot(x6, y6, label="O(1)",        color=colors[6])

# Get custom algorithm results
file_object = open("data\\your_algorithm.json", "rb")
contents = file_object.read()
algo_result = msgspec.json.decode(contents)
file_object.close()

# Plot in custom algorithm tries
for trial_num in range(number_of_trials):
    plt.plot(algo_result['data_nums'], algo_result[f'result_{trial_num}'], marker='o', linestyle="")

# Plot in custom algorithm average
plt.plot(algo_result['data_nums'], algo_result[f'average_result'], label="Your algorithm")

# Show graph
plt.ylim(0, settings.config_1.get_time_limit())
plt.xlim(0, settings.config_1.get_max_num_of_data())
plt.style.use("Solarize_Light2")
plt.legend()
plt.xlabel("Time (seconds)", color=colors[1])
plt.ylabel("Number of data", color=colors[1])
plt.title("True to computer Big O Visualization", color=colors[0])
plt.grid(True, linestyle="--", alpha=0.2)
plt.show()