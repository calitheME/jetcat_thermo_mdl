import pandas as pd
import inspect
import thermo

# excel parameter data extraction
df = pd.read_csv("engine_parameters.csv")
data = dict(zip(df['variable name'], df['value']))

# assumptions
print("Cold-air standard preliminary thermodynamic analysis of Jetcat P100-RX:")
print("    *constant specific heat,\n    *air = ideal gas,\n    *combustion = heat addition,\n    *exhaust = heat rejection,\n    *reversible process")

# compressor work
sig = inspect.signature(thermo.compressor_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Wc = thermo.compressor_work(**kwargs)
data['Wc'] = Wc
print(f"Compressor work: {Wc:>10.2f} kW")

# turbine work
sig = inspect.signature(thermo.turbine_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Wt = thermo.turbine_work(**kwargs)
data['Wt'] = Wt
print(f"Turbine work: {Wt:>13.2f} kW")

# combustion heat
sig = inspect.signature(thermo.combustion_heat)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Qi = thermo.combustion_heat(**kwargs)
data['Qi'] = Qi
print(f"Combustion heat: {Qi:>10.2f} kW")

# exhaust heat
sig = inspect.signature(thermo.exhaust_heat)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Qo = thermo.exhaust_heat(**kwargs)
data['Qo'] = Qo
print(f"Exhaust heat: {Qo:>13.2f} kW")

# net work
sig = inspect.signature(thermo.net_work)
kwargs = {k: data[k] for k in sig.parameters.keys()}
WN = thermo.net_work(**kwargs)
data['WN'] = WN
print(f"Net work: {WN:>17.2f} kW")

# jet power
print(f"Jet power: {data['Qoa']:>16.2f} kW")

# power ratio
sig = inspect.signature(thermo.power_ratio)
kwargs = {k: data[k] for k in sig.parameters.keys()}
PR = thermo.power_ratio(**kwargs)
data['PR'] = PR
print(f"Power ratio: {PR:>14.2f} (jet power to net work)")

# wasted energy
sig = inspect.signature(thermo.wasted_energy)
kwargs = {k: data[k] for k in sig.parameters.keys()}
Qw = thermo.wasted_energy(**kwargs)
data['Qw'] = Qw
print(f"Wasted energy: {Qw:>12.2f} kW")

# energy ratio
sig = inspect.signature(thermo.energy_ratio)
kwargs = {k: data[k] for k in sig.parameters.keys()}
ER = thermo.energy_ratio(**kwargs)
data['ER'] = ER
print(f"Energy ratio: {ER:>13.2f} (jet power to waste heat)")

