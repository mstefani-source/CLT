import os
import numpy as np
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
from tkinter import *

def get_set(x):
    np.random.seed(x)
    return(np.random.random(size=20))

def calc_avg(a):
    sum = 0
    for i in a:
        sum = sum + i
    return(sum/len(a))

def main():
#    fig, _ = plt.subplots()
    
    root = Tk()
    ay = []
    for x in range(20):
        a = get_set(x)
        ay.append(calc_avg(a))
    plt.plot(range(20),ay)


if __name__ == "__main__":
    main()