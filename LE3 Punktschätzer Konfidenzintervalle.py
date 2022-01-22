# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:30:30 2021

@author: Patrick Schürmann
"""

import numpy as np
import scipy.stats as st


def Punktschätzer_Mittelwert(data):
    """
    Punktschätzer Mittelwert
    :param array data: Werte
    """
    print("Punktschätzer Mittelwert")
    print(round(np.mean(data), 3))


# Punktschätzer_Mittelwert([1.9, 3.4, 4.9, 4.4, 5.5])


def Punktschätzer_Standardabweichung(data):
    """
    Punktschätzer Standardabweichung
    :param array data: Werte
    """
    print("Punktschätzer Standardabweichung")
    # https://spaces.technik.fhnw.ch/multimediathek/file/parameterschatzung-skript
    print("Varianz:", round(np.var(data, ddof=1), 3))
    print("Standardabweichung:", round(np.std(data, ddof=1), 3))

# Punktschätzer_Standardabweichung([1.9, 3.4, 4.9, 4.4, 5.5])


def Mittelwert_Intervall_kleine_Stichprobe(m, v, n, ki):
    """
    Konfidenzintervall Mittelwert kleine Stichprobe
    :param float m: Mittelwert
    :param float v: Standardabweichung
    :param float n: Anzahl
    :param float ki: Konfidenzintervall
    """
    # https://statologie.de/konfidenzintervall/
    zscore = st.norm.ppf(ki)
    print(zscore)
    # ZScore könnte hier überschrieben werden:
    # zscore = 1.96
    intervall = zscore * (v / (n ** 0.5))
    print(m - intervall, m + intervall)


# Mittelwert_Intervall_kleine_Stichprobe(300, 18.5, 25, 0.95)


def Mittelwert_Intervall_grosse_Stichprobe(p, n, ki):
    """
    Konfidenzintervall Mittelwert grosse Stichprobe
    :param float p: Wahrscheinlichkeit
    :param float n: Anzahl
    :param float ki: Konfidenzintervall
    """
    zscore = st.norm.ppf(ki)
    print(zscore)
    intervall = zscore * (((p * (1-p))/n) ** 0.5)
    print(p - intervall, p + intervall)


# Mittelwert_Intervall_grosse_Stichprobe(86/123, 12, 0.975)


def Punktschätzer_relHäufigkeit(data):
    print("Punktschätzer relative Häufigkeit")
    # https://welt-der-bwl.de/Punktschätzung
    print(round(np.mean(data), 3))


# Punktschätzer_relHäufigkeit([10, 20, 18, 15, 17])
