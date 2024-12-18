

# How to use this tool

## Standard usage:

1. Run `pure_runner.py` to get the time complexity results of pure algorithms in your computer.
2. Edit `algorithm_runner.py` and run it to get the time complexity results of your custom algorithm in your computer.
3. Choose a visualizer:
   1. Matplotlib visualizer (run `matplotlib.py`)
   2. Plotly visualizer (run `plotly.py`, dump the terminal after you've finished and want to run this again to avoid errors. The library is not robust.)

## "I don't want to recalculate the whole thing, just my algorithm"

1. Follow steps in **[Standard usage]**, starting from no. 2

## Custom colors, number of data to test, time limit, or number of trials to get average

1. Edit the config in `modules\settings.py`.
2. Edit `pure_runner.py` and `algorithm_runner.py` if necessary.
3. Follow steps in **[Standard usage]** again.
