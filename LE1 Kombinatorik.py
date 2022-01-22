# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:23:36 2021

@author: schue
"""
import math


def Variationen_mit(n, k):
    """
    Geordnete Stichprobe
    :param int n: Anzahl Elemente in der Grundmenge
    :param int k: Anzahl der Ziehungen
    """
    print(n ** k)


Variationen_mit(5, 5)


def Variationen_ohne(n, k):
    """
    Geordnete Stichprobe
    :param int n: Anzahl Elemente in der Grundmenge
    :param int k: Anzahl der Ziehungen
    """
    result = (math.factorial(n) / (math.factorial(k) *
              math.factorial(n - k))) * math.factorial(k)
    print(result)


Variationen_ohne(4, 4)


def Kombinationen_mit(n, k):
    """
    Ungeordnete Stichprobe
    :param int n: Anzahl Elemente in der Grundmenge
    :param int k: Anzahl der Ziehungen
    """
    temp = n + k - 1
    result = math.factorial(temp) / (math.factorial(k)
                                     * math.factorial(temp - k))
    print(result)


Kombinationen_mit(5, 3)


def Kombinationen_ohne(n, k):
    """
    Ungeordnete Stichprobe
    :param int n: Anzahl Elemente in der Grundmenge
    :param int k: Anzahl der Ziehungen
    """
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print(result)


Kombinationen_ohne(20, 5)


def Permutation_ohne(n):
    """
    Ungeordnete Stichprobe
    :param int n: Anzahl Elemente in der Grundmenge
    :param int k: Anzahl der Ziehungen
    """
    result = math.factorial(n)
    print(result)


Permutation_ohne(5)
