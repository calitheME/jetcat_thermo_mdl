import pandas as pd
import inspect
import thermo
import matplotlib.pyplot as plt

# excel parameter data extraction
df = pd.read_csv("engine_parameters.csv")
data = dict(zip(df['variable name'], df['value']))
cpdata = dict(zip(df['temp K'], df['cp']))
Tes = df['exit temp K'].tolist()
calcs = {}

# assumptions
print("Cold-air standard preliminary thermodynamic analysis of Jetcat P100-RX:")
print("    *constant specific heat,\n    *air = ideal gas,\n    *combustion = heat addition,\n    *exhaust = heat rejection,\n    *reversible process")

# temps
sig = inspect.signature(thermo.temps)
kwargs = {k: data[k] for k in sig.parameters.keys()}
T1 = data['T1']
Te = data['Te']
T2, T3, T4 = thermo.temps(**kwargs)

# average specific heats
cp12 = thermo.cpavg(T1, T2, cpdata)
    # errors with cp23-cpe1

# compressor work
Wc = thermo.compressor_work(T1, T2, data['m'], cp12)
calcs['Wc'] = Wc
print(f"Compressor work: {Wc:>10.2f} kW")

# turbine work
Wt = thermo.turbine_work(T4, T3, data['m'], data['cp'])
calcs['Wt'] = Wt
print(f"Turbine work: {Wt:>13.2f} kW")

# combustion heat
Qi = thermo.combustion_heat(T2, T3, data['m'], data['cp'])
calcs['Qi'] = Qi
print(f"Combustion heat: {Qi:>10.2f} kW")

# exhaust heat
Qo = thermo.exhaust_heat(Te, T1, data['m'], data['cp'])
calcs['Qo'] = Qo
print(f"Exhaust heat: {Qo:>13.2f} kW")

# net work
WN = thermo.net_work(calcs['Wt'], calcs['Wc'])
print(f"Net work: {WN:>17.2f} kW")

# jet power
print(f"Jet power: {data['Pj']:>16.2f} kW")

# exhaust power to energy ratio
PER = thermo.power_energy_ratio(data['Pj'], Qo)
calcs['PER'] = PER
print(f"Power ratio: {PER:>14.2f} (jet power to exhaust heat energy)")

# shaft power
Wgshaft = thermo.shaft_power(WN, data['nshaft'])
calcs['Wgshaft'] = Wgshaft
print(f"Shaft power: {Wgshaft:>14.2f} kW")

# exhaust heat power
Wgheat = thermo.heat_power(WN, data['nheat'])
calcs['Wgheat'] = Wgheat
print(f"Exhaust heat power: {Wgheat:>7.2f} kW")

# exhuast KE power
WgKE = thermo.KE_power(WN, data['nKE'])
calcs['WgKE'] = WgKE
print(f"Exhaust KE power: {WgKE:>9.2f} kW")

# thermal eff
nth = thermo.nth(WN, Qi)
calcs['nth'] = nth
print(f"Thermal efficiency: {nth:>10.2f}")

# Power gen by method
methods = ['shaft', 'heat', 'KE']
Wg = [Wgshaft, Wgheat, WgKE]
plt.bar(methods, Wg)
plt.title('Power Generation by Method', weight='bold')
plt.xlabel('Method', weight='bold')
plt.ylabel('Power (kW)', weight='bold')
plt.show()

# Exhaust temp parametric study
Qos, nths = thermo.Te_para_study(Tes, T1, data['m'], data['cp'], Qi)
# exhaust heat plot
plt.plot(Tes, Qos)
plt.title('Exhaust Heat vs. Exhaust Temperature', weight='bold')
plt.xlabel('Exhaust Temperature (K)', weight='bold')
plt.ylabel('Exhaust Heat (kW)', weight='bold')
plt.show()
# thermal efficiency plot
plt.plot(Tes, nths)
plt.title('Thermal Efficiency vs. Exhaust Temperature', weight='bold')
plt.xlabel('Exhaust Temperature (K)', weight='bold')
plt.ylabel('Thermal Efficiency', weight='bold')
plt.show()