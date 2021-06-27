import os
import numpy as np
import matplotlib as mpl

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
from tkinter import *


def get_uni():
    return np.random.uniform(-1, 1, size=1)


def get_lap():
    loc, scale = 0., 1.
    return np.random.laplace(loc, scale, 1)


def get_gum():
    loc, scale = 0., 1.
    return np.random.gumbel(loc, scale, 1)


def get_par():
    a = 1000.
    return np.random.pareto(a, 1)


def get_rey():
    scale = 0.1
    return np.random.rayleigh(scale, size=1)


def calc_avg(a):
    calc_sum = 0
    for i in range(len(a)):
        calc_sum = calc_sum + a[i]
    return calc_sum


def main():
    a = []
    for x in range(10 ** 5):
        b = calc_avg(get_par())
        a.append(b)
    plt.hist(a, bins=100)
    plt.show()


if __name__ == "__main__":
    main()
