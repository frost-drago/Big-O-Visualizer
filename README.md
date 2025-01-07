# How to use this tool

## Standard usage:

1. Run `pure_runner.py` to get the time complexity results of pure algorithms in your computer.
2. Edit `algorithm_runner.py` and run it to get the time complexity results of your custom algorithm in your computer.
3. Choose a visualizer:
   1. Matplotlib visualizer (run `visualizer_matplotlib.py`)
   2. Plotly visualizer (run `visualizer_plotly.py`, dump the terminal after you've finished and want to run this again to avoid errors. The library is not robust. Keep rerunning and dumping the terminal because Plotly accesses random ports, some
      of which are not available)

## "I don't want to recalculate the whole thing, just my algorithm"

1. Follow steps in **[Standard usage]**, starting from no. 2

## Custom colors, number of data to test, time limit, or number of trials to get average

1. Edit the config in `modules\settings.py`.
2. Edit `pure_runner.py` and `algorithm_runner.py` if necessary.
3. Follow steps in **[Standard usage]** again.

# Dependencies (click on links)

* [msgspec](https://pypi.org/project/msgspec/ "Go to official site")
* [matplotlib](https://pypi.org/project/matplotlib/ "Go to official site")
* [plotly](https://pypi.org/project/plotly/ "Go to official site")
