import pandas as pd
import inspect
import thermo

# excel parameter data extraction
df = pd.read_csv("engine_parameters.csv")
data = dict(zip(df['variable name'], df['value']))

# compressor work
sig = inspect.signature(thermo.compressor_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Wc = thermo.compressor_work(**kwargs)
print(Wc)