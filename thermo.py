def compressor_work(T1, r, k, m, cp):
    T2 = T1*(r**((k-1)/k))
    Wc = m*cp*(T2-T1)
    
    return Wc

def turbine_work(T4, r, k, m, cp):
    T3 = T4*(r**((k-1)/k))
    Wt = m*cp*(T3-T4)
    
    return Wt

def combustion_heat(T4, T1, r, k, m, cp):
    T2 = T1*(r**((k-1)/k))
    T3 = T4*(r**((k-1)/k))
    Qi = m*cp*(T3-T2)
    
    return Qi

def exhaust_heat(T4, T1, m, cp):
    Qo = m*cp*(T4-T1)
    
    return Qo

def net_work(Wt, Wc):
    WN = Wt - Wc
    
    return WN

def power_ratio(WN, Qoa):
    PR = Qoa / WN
    
    return PR

def wasted_energy(Qo, Qoa):
    Qw = Qo - Qoa
    
    return Qw

def energy_ratio(Qo, Qoa):
    ER = Qoa / Qo
    
    return ER