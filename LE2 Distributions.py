
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import expon
from scipy.stats import norm


def Binominalverteilung(n, p, k):
    """
    Binominalverteilung
    :param int n: Anzahl Versuche
    :param float p: Erfolgswahrscheinlichkeit
    :param float k: entspricht Anzahl Treffer
    """
    print("Binominalverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    std = binom.std(n, p, loc=0)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:",
          round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    print("Wahrscheinlichkeit für k: PMF:", binom.pmf(k, n, p, loc=0))
    print("Wahrscheinlichkeit bis und mit k: CDF:", binom.cdf(k, n, p, loc=0))


# Binominalverteilung(12, 1/2, 4)


def Poissonverteilung(mu, k):
    """
    Poissonverteilung
    :param float mu: erwartete Anzahl Eintreten
    :param float k: entspricht Anzahl Treffer
    """
    print("Poissonverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html#scipy.stats.poisson
    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    std = poisson.std(mu, loc=0)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:",
          round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    print("Wahrscheinlichkeit für k: PMF:", poisson.pmf(k, mu, loc=0))
    print("Wahrscheinlichkeit bis und mit k: CDF:", poisson.cdf(k, mu, loc=0))


# Poissonverteilung(4/10, 2)


def Exponentialverteilung(lamba, x):
    """
    Exponentialverteilung
    :param float lamba: der durchschnittlichen Wartezeit
    :param float x: Beobachtungszeitraum
    """
    print("Exponentialverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html#scipy.stats.expon
    mean, var, skew, kurt = expon.stats(loc=0, scale=lamba, moments='mvsk')
    std = expon.std(loc=0, scale=lamba)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:",
          round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    print("Wahrscheinlichkeit bis und mit k: CDF:",
          expon.cdf(x, loc=0, scale=lamba))


# Exponentialverteilung(20, 60)


def Normalverteilung(n, p, m, x, q):
    """
    Normalverteilung
    :param int n: Grundgesamtheit
    :param float p: Wahrscheinlichkeit
    :param float m: Mittelwert
    :param float x: gewünschten Zahl
    :param float q: definierter Wahrscheinlichkeit (1 = 100%)
    """
    print("Normalverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm
    v = round((n * p * (1-p)) ** 0.5, 2)
    mean, var, skew, kurt = norm.stats(loc=m, scale=v, moments='mvsk')
    std = norm.std(loc=m, scale=v)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:",
          round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    print("Wahrscheinlichkeit für k: PDF:", norm.pdf(x, loc=m, scale=v))
    print("Wahrscheinlichkeit bis und mit k: CDF:", norm.cdf(x, loc=m, scale=v))
    print("Wert bei definierter Wahrscheinlichkeit:",
          norm.ppf(q, loc=m, scale=v))


Normalverteilung(400000, 0.02, 8000, 8100, 0.95)
