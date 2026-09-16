import pandas as pd

data = pd.read_csv("engine_parameters.csv")


parameters = data.loc[0:6, ['variable name', 'value']]


parameters_dict = parameters.to_dict()
print(type(parameters_dict))
print(parameters_dict)