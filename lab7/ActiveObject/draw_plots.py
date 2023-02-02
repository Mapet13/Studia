from dataclasses import dataclass
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd

def get_id_of_char(s, target):
    for i, c in enumerate(s):
        if c == target:
            return i
    return -1

def id_of_digit(s):
    for i, c in enumerate(s):
        if c.isdigit():
            return i
    return -1

def get_number_from(s):
    return s[id_of_digit(s):]

@dataclass
class Run_parameters:
    buffer_hard_work_amount: int 
    threads_count: int

    @classmethod
    def from_str(cls, s):
        just_data = s[get_id_of_char(s, '[') + 1 : get_id_of_char(s, ']')]
        numbers = map(lambda x: int(get_number_from(x)), just_data.split(','))
        parameters = list(numbers)
        return Run_parameters(parameters[0], parameters[1])
        

@dataclass
class Measure_data:
    run_parameters: Run_parameters
    ao_average_work_count: float
    ao_average_iterations: float
    ao_average_time_saved: float
    sync_average_work_count: float
    sync_average_iterations: float

    def as_list(self):
        return [
            self.run_parameters.buffer_hard_work_amount, 
            self.run_parameters.threads_count, 
            self.ao_average_work_count,
            self.ao_average_iterations,
            self.ao_average_time_saved,
            self.sync_average_work_count,
            self.sync_average_iterations
        ]

with open("pomiar_1.txt") as f:
    lines = [line[:-1] for line in f]

measure_split_line = "--------------------------------------------------------"

measures = []
current_measure = []
for line in filter(lambda l: len(l) > 0, lines[1:]):
    if line == measure_split_line:
        measures.append(current_measure)
        current_measure = []
    else:
        current_measure.append(line)
measures.append(current_measure)
    
measures_data = []
for measure in measures:
    parameters = Run_parameters.from_str(measure[0])
    ao_average_work_count = float(get_number_from(measure[1]))
    ao_average_iterations = float(get_number_from(measure[2]))
    ao_average_time_saved = float(get_number_from(measure[3]))
    sync_average_work_count = float(get_number_from(measure[4]))
    sync_average_iterations = float(get_number_from(measure[5]))
    measures_data.append(Measure_data(parameters, ao_average_work_count, ao_average_iterations, ao_average_time_saved, sync_average_work_count, sync_average_iterations).as_list())



dataframe = pd.DataFrame(measures_data, columns=["hard work amount", "threads per type", "ao_wc", "ao_iter", "ao_ts", "s_wc", "s_iter"]) 
dataframe["diff_wc"] = dataframe["ao_wc"] / dataframe["s_wc"]
dataframe["diff_iter"] = dataframe["ao_iter"] - dataframe["s_iter"]


piv = pd.pivot_table(dataframe, values="ao_ts",index=["hard work amount"], columns=["threads per type"], fill_value=0)

ax = sns.heatmap(piv, annot=True, cmap="coolwarm", vmax = 1.2, center = 1, square=True, fmt=".1f")
plt.setp( ax.xaxis.get_majorticklabels(), rotation=90 )
plt.title("Time saved (in ms) by Active Object's clients")
plt.tight_layout()
plt.show()