# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:17:10 2021

@author: schue
"""
import numpy


def MonteCarloNormal(mean, std, size):
    """
    MonteCarloNormal
    :param float mean: Mittelwert
    :param float std: Standardabweichung
    :param float size: Grösse der Simulation
    """
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
    my_generator = numpy.random.default_rng()
    result = my_generator.normal(mean, std, size)
    print(result)
    return result


# result = MonteCarloNormal(10, 5, 10)


def MonteCarloExponential(scale, size):
    """
    MonteCarloExponential
    :param float scale: Ausfallrate
    :param float size: Grösse der Simulation
    """
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html#numpy.random.Generator.exponential
    my_generator = numpy.random.default_rng()
    result = my_generator.exponential(scale, size)
    print(result)
    return result


# result = MonteCarloExponential(5, 100)
