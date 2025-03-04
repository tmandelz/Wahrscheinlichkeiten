# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:30:30 2021

@author: Patrick Schürmann
"""

def Punktschätzer_Mittelwert():
    print("Punktschätzer Mittelwert")
    # https://spaces.technik.fhnw.ch/multimediathek/file/parameterschatzung-skript
    import numpy as np
    data = [1.9, 3.4, 4.9, 4.4, 5.5]
    # print(round(np.mean(data), 3))
    
Punktschätzer_Mittelwert()

def Punktschätzer_Standardabweichung():
    print("Punktschätzer Standardabweichung")
    # https://spaces.technik.fhnw.ch/multimediathek/file/parameterschatzung-skript
    import numpy as np
    data = [1.9, 3.4, 4.9, 4.4, 5.5]
    print("Varianz:", round(np.var(data, ddof=1), 3))
    print("Standardabweichung:", round(np.std(data, ddof=1), 3))
    
# Punktschätzer_Standardabweichung()

def Punktschätzer_relHäufigkeit():
    print("Punktschätzer relative Häufigkeit")
    # https://welt-der-bwl.de/Punktschätzung
    import numpy as np
    data = [10, 20, 18, 15, 17]
    print(round(np.mean(data), 3))

# Punktschätzer_relHäufigkeit()


def Mittelwert_Intervall_kleine_Stichprobe():
    import scipy.stats as st
    # https://statologie.de/konfidenzintervall/
    # m entspricht dem Mittelwert
    m = 300
    # v entspricht der Standardabweichung
    v = 18.5
    # n = Anzahl
    n = 25  
    # ki = Konfidenzintervall
    ki = 0.95
    zscore = st.norm.ppf(ki)
    print(zscore)
    # ZScore könnte hier überschrieben werden:
    # 1.96
    intervall = zscore * (v / (n ** 0.5))
    print(m - intervall, m + intervall)
    
Mittelwert_Intervall_kleine_Stichprobe()

  
def Mittelwert_Intervall_grosse_Stichprobe():
    import scipy.stats as st
    # p = Wahrscheinlichkeit
    p = 86/123
    # n = Anzahl
    n = 12
    # ki = Konfidenzintervall
    ki = 0.975
    zscore = st.norm.ppf(ki)
    print(zscore)
    intervall = zscore * (((p * (1-p))/n) ** 0.5)
    print(p - intervall, p + intervall)
    
# Mittelwert_Intervall_grosse_Stichprobe()