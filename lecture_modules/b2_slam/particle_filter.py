import numpy as np
import matplotlib.pyplot as plt
from b2_slam import config

def plot_particles(particles, importance, title=""):
    # Belive
    plt.figure(figsize=(config.figure_width,config.figure_width/6.0))
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('bel(x)')
    plt.yticks([])
    for (p, i) in zip(particles, importance):
        plt.arrow(p, 0, 0, i, head_width=0.0)
    plt.plot([0.0, 0.0],[0.0,0.02],'w')
    plt.xlim(0.0, 12.0)
    plt.show()
    # Histogram
    plt.figure(figsize=(config.figure_width,config.figure_width/6.0))
    plt.hist(particles, 120, density=True, stacked=True, facecolor='lightblue')
    plt.xlabel('x')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
    plt.ylabel('Histogram bel(x)')
    plt.yticks([])
    # Dummy element to enforce right scale of y axis
    plt.plot([0.0, 0.0],[0.0,1.0],'w')
    plt.xlim(0.0, 12.0)
    plt.show()

def plot_p(p_z):
    x = np.arange(0.0, 12.0, step=0.01)
    z = list(map(p_z, x))
    plt.figure(figsize=(config.figure_width,config.figure_width/6.0))
    plt.ylabel('x')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
    plt.yticks([])
    plt.ylabel('p(z|x)')
    plt.plot(x,z)
    plt.plot(0.0, 0.0)
    plt.xlim(0.0, 12.0)
    # Dummy element to enforce right scale of y axis
    plt.plot([0.0, 0.0],[0.0,1.0],'w')
    plt.show()

