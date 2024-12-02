import matplotlib.pyplot as plt
import numpy as np

def temperature_mer(t, T):
    return 5.45*np.sin(2*np.pi*t/T - np.pi/2) + 18.25 + 273

def temperature_douce(t, T):
    return 8.5*np.sin(2*np.pi*t/T - np.pi/2) + 18 + 273

def temperature_relachee(c_ed, c_em, T_mer, T_douce):
    return (c_ed*T_douce + c_em*T_mer)/(c_ed + c_em)

T = 365*24*3600
X = np.linspace(0, T, 100000)
T_douce = temperature_douce(X, T)
T_mer = temperature_mer(X, T)
c_ed = 4185
c_em = 4185
T_relachee = temperature_relachee(c_ed, c_em, T_mer, T_douce)
plt.plot(X, T_relachee)
plt.show()