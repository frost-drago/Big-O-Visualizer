# Decided to use python instead of YAML because of the Custom Objects + Methods requirements in the project requirements
import copy

# Config objects, or, settings.
class config:
    def __init__(self, time_limit, max_num_of_data, colors, number_of_trials):
        self._time_limit = time_limit
        self._max_num_of_data = max_num_of_data
        self._colors = colors
        self._number_of_trials = number_of_trials

    def __str__(self):
        return f"""Settings: 
- Time limit:               {self._time_limit}
- Maximum number of data:   {self._max_num_of_data}
- Colors used:              {self._colors}
- Number of trials:         {self._number_of_trials}"""
    
    def get_time_limit(self):
        return self._time_limit
    def get_max_num_of_data(self):
        return self._max_num_of_data
    def get_colors(self):
        return self._colors
    def get_number_of_trials(self):
        return self._number_of_trials
    
    def set_time_limit(self, time_limit):
        try:
            if not isinstance(time_limit, (int, float)):
                raise ValueError("Time limit must be an int or a float.")
            if time_limit <= 0:
                raise ValueError("Time limit must be a positive number.")
            self._time_limit = time_limit
            return True
        except:
            return False
    def set_max_num_of_data(self, max_num_of_data):
        try:
            if not isinstance(max_num_of_data, int):
                raise ValueError("Maximum number of data must be an int.")
            if max_num_of_data <= 0:
                raise ValueError("Maximum number of data must be a positive number.")
            self._max_num_of_data = max_num_of_data
            return True
        except:
            return False
    def set_colors(self, colors):
        try:
            if not isinstance(colors, list):
                raise ValueError("Colors must be a list.")
            if len(colors) != 7:
                raise ValueError("List must be of 7 length.")
            self._colors = colors
            return True
        except:
            return False
    def set_number_of_trials(self, number_of_trials):
        try:
            if not isinstance(number_of_trials, int):
                raise ValueError("Number of trials must be an int.")
            if number_of_trials <= 0:
                raise ValueError("Number of trials must be a positive number.")
            self._number_of_trials = number_of_trials
            return True
        except:
            return False

# Preset configs
config_1 = config(0.6, 4000, ['#255568', '#007179', '#008C81', '#16A77E', '#61BF73', '#A4D763', '#EDEF5D'], 5)
config_2 = copy.deepcopy(config_1)
config_2.set_time_limit(0.04)
config_2.set_max_num_of_data(1000)

# Add more configs
# 📝 EDITABLE ON THIS LINE. Please follow convention based on above.