def temps(T1, r, k, Te, cp, Ve):
    T2 = T1*(r**((k-1)/k))
    T4 = ((Ve**2)/(2*cp))+Te
    T3 = T4*(r**((k-1)/k))

    return T2, T3, T4

def cpavg(Ta, Tb, cpdata):
    Tavg = (Ta + Tb) / 2
    keys = list(cpdata.keys())
    for i, key in enumerate(keys):
        if key == Tavg:
            cpavg = cpdata[key]
            break
        elif key < Tavg:
            continue
        elif key > Tavg:
            rkey = keys[i]
            lkey = keys[i-1]
            cpavg = ((cpdata[rkey] - cpdata[lkey]) / ((rkey)-(lkey))) * (Tavg - (lkey)) + cpdata[lkey]
            break
    return cpavg

def compressor_work(T1, T2, m, cp12):
    Wc = m*cp12*(T2-T1)
    
    return Wc

def turbine_work(T4, T3, m, cp):
    Wt = m*cp*(T3-T4)
    
    return Wt

def combustion_heat(T2, T3, m, cp):
    Qi = m*cp*(T3-T2)
    
    return Qi

def exhaust_heat(Te, T1, m, cp):
    Qo = m*cp*(Te-T1)
    
    return Qo

def net_work(Wt, Wc):
    WN = Wt - Wc
    
    return WN

def power_energy_ratio(Pj, Qo):
    PER = Pj / Qo
    
    return PER

def shaft_power(WN, nshaft):
    Wg = WN * nshaft
    
    return Wg

def heat_power(WN, nheat):
    Wg = WN * nheat
    
    return Wg

def KE_power(WN, nKE):
    Wg = WN * nKE
    
    return Wg

def nth(WN, Qi):
    nth = WN / Qi
    
    return nth

def Te_para_study(Tes, T1, m, cp, Qi):
    Qos = []
    nths = []
    for Te in Tes:
        Qo = m*cp*(Te-T1)
        nth = 1 - Qo/Qi
        Qos.append(Qo)
        nths.append(nth)
    return Qos, nths