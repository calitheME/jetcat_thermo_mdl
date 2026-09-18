import pandas as pd
import inspect
import thermo

# excel parameter data extraction
df = pd.read_csv("engine_parameters.csv")
data = dict(zip(df['variable name'], df['value']))

# assumptions
print("Cold-air standard preliminary thermodynamic analysis of Jetcat P100-RX:")
print("    constant specific heat,\n    air = ideal gas,\n    combustion = heat addition,\n    reversible process")

# compressor work
sig = inspect.signature(thermo.compressor_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Wc = thermo.compressor_work(**kwargs)
print(f"Compressor work: {Wc:>10.2f} kW")

# turbine work
sig = inspect.signature(thermo.turbine_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Wt = thermo.turbine_work(**kwargs)
print(f"Turbine work: {Wt:>13.2f} kW")

# combustion heat
sig = inspect.signature(thermo.combustion_heat)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Qi = thermo.combustion_heat(**kwargs)
print(f"Combustion heat: {Qi:>10.2f} kW")

# exhaust heat
sig = inspect.signature(thermo.exhaust_heat)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Qo = thermo.exhaust_heat(**kwargs)
print(f"Exhaust heat: {Qo:>13.2f} kW")

# net work
WN = thermo.net_work(Wt, Wc)
print(f"Net work: {WN:>17.2f} kW")

