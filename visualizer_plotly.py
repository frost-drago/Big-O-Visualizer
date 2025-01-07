# Visualizer in Plotly
# Don't forget to dump the terminal after using this, to not encounter errors. The library is not robust.
# Might need a few (re)tries to display the graph.
# The reason is that Plotly randomly generate a port number, and sometimes those ports are not available (or being used by another process).
# As of current Plotly version, there's no way around this except rewriting the entire open_html_in_browser function hardcoded in Plotly.

import modules.commons as commons
import msgspec
import modules.settings as settings
import plotly.graph_objects as go

# Load settings
colors = settings.config_1.get_colors()
number_of_trials = settings.config_1.get_number_of_trials()
 
# Get pure algorithm results
file_object = open("data\\pure_algorithms.json", "rb")
contents = file_object.read()
result = msgspec.json.decode(contents)
file_object.close()

x0, x1, x2, x3, x4, x5, x6 = [commons.get_list_until_number(result['data_nums'], result[f'data_num_{num}']) for num in range(7)]
y0, y1, y2, y3, y4, y5, y6 = [result[f'result_{num}'] for num in range(7)]

# Plot in pure algorithm results
fig = go.Figure()
fig.add_trace(go.Scatter(x=x0, y=y0, name='O(n!)',      line=dict(color=colors[0], width=2)))
fig.add_trace(go.Scatter(x=x1, y=y1, name='O(2^n)',     line=dict(color=colors[1], width=2)))
fig.add_trace(go.Scatter(x=x2, y=y2, name='O(n^2)',     line=dict(color=colors[2], width=2)))
fig.add_trace(go.Scatter(x=x3, y=y3, name='O(n log(n))',line=dict(color=colors[3], width=2)))
fig.add_trace(go.Scatter(x=x4, y=y4, name='O(n)',       line=dict(color=colors[4], width=2)))
fig.add_trace(go.Scatter(x=x5, y=y5, name='O(log(n))',  line=dict(color=colors[5], width=2)))
fig.add_trace(go.Scatter(x=x6, y=y6, name='O(1)',       line=dict(color=colors[6], width=2)))

# Get custom algorithm results
file_object = open("data\\your_algorithm.json", "rb")
contents = file_object.read()
algo_result = msgspec.json.decode(contents)
file_object.close()

# Plot in custom algorithm tries
for trial_num in range(number_of_trials):
    fig.add_trace(go.Scatter(x=algo_result['data_nums'], y=algo_result[f'result_{trial_num}'], mode='markers', name=f'trial number {trial_num + 1}'))
    
# Plot in custom algorithm average
fig.add_trace(go.Scatter(x=algo_result['data_nums'], y=algo_result[f'average_result'], name="Your algorithm", line=dict(color='#F10101', width=4)))

# Show graph
# There is something particular about the library that it fails if the update is not done this way and in this tab formatting
fig.update_layout(
        title=dict(
            text='True to computer Big O Visualization'
        ),
        xaxis=dict(
            title=dict(
                text='Number of data'
            )
        ),
        yaxis=dict(
            title=dict(
                text='Time taken (seconds)'
            )
        ),
)

fig.show()