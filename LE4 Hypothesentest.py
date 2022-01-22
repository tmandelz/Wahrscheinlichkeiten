# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:29:42 2021

@author: schue
Voraussetzung Scipy Version grösser 1.70
"""
from scipy.stats import binomtest
from statsmodels.stats.weightstats import ztest as ztest
from scipy import stats
from scipy.stats import mannwhitneyu
import numpy as np


def BinomialHypotestOneSample(k, x, y):
    """
    BinomialHypotestOneSample
    :param float k: number of successes
    :param float x: number of trials
    :param float y: hypothesized probability of success
    """
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    # ‘two-sided’ (default), ‘greater’, ‘less’
    result = binomtest(k, n=x, p=y, alternative='two-sided')
    print(result)


# BinomialHypotestOneSample(4, 15, 0.1)


def zTestOneSample(Vergleichswert, data):
    """
    zTestOneSample
    :param float Vergleichswert: Vergleichswert
    :param array data: Werte
    """
    # Wird angewendet bei Stichprobengrösse < 30.
    # https://www.statology.org/z-test-python/
    result = ztest(data, value=Vergleichswert)
    print(result)
    print("Der zweite Wert ist der pvalue.")


# zTestOneSample(110, [88, 92, 94, 94, 96, 97, 97, 97, 99,
    #    99, 105, 109, 109, 109, 110, 112, 112, 113, 114, 115])


def tTestOneSample(Vergleichswert, data):
    """
    tTestOneSample
    :param float Vergleichswert: Vergleichswert
    :param array data: Werte
    """
    # Wird angewendet bei Stichprobengrösse < 30.
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html
    result = stats.ttest_1samp(data, Vergleichswert)
    print(result)


# tTestOneSample(100, [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105,
    #  109, 109, 109, 110, 112, 112, 113, 114, 115])


def tTestTwoSamples(data1, data2):
    """
    tTestTwoSamples
    :param array data1: Werte 1
    :param array data2: Werte 2
    """
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
    # alternative = ‘two-sided’, ‘less’, ‘greater’
    result = stats.ttest_ind(data1, data2, alternative="two-sided")
    print(result)


# tTestTwoSamples([88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 100, 112, 100, 100, 105, 50], [
#                 88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 120, 110, 120, 112, 113, 130, 150])


def MannWhitneyUTest(data1, data2):
    """
    MannWhitneyUTest
    :param array data1: Werte 1
    :param array data2: Werte 2
    """
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    U1, p = mannwhitneyu(data1, data2, method="exact")
    print(U1, p)


# MannWhitneyUTest([88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 100, 112, 100, 100, 105, 50], [
#     88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 120, 110, 120, 112, 113, 130, 150])


def KolmogorovSmirnovTest():
    """
    KolmogorovSmirnovTest
    """
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html
    # Überprüft Übereinstimmung zweier Wahrscheinlichkeitsverteilungen

    rng = np.random.default_rng()
    x = stats.norm.rvs(loc=0.2, size=100, random_state=rng)
    result = stats.kstest(x, 'norm', alternative='less')
    print(result)


# KolmogorovSmirnovTest()


def NormalzuSollwert(m0, m1, v, n):
    """
    NormalzuSollwert
    :param float m0: ursprünglichen Mittelwert
    :param float m1: neuen Mittelwert
    :param float v: neuen Standardabweichung
    :param float n: grösse der Stichprobe
    """
    # tpg entspricht Prüfgrösse t
    tpg = (m1-m0)/(v/(n**0.5))
    print("Prüfgrösse t:", tpg)
    t = stats.t.ppf(q=.01, df=n-1)
    print("Kritische Grenze:", t)


# NormalzuSollwert(800, 840, 400, 1600)
