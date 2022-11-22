import matplotlib.pyplot as plt
import numpy as np
from b2_slam import config
from matplotlib.widgets import Slider

z_max = 5.0
distance_in_map = 4.0

# sum of w_i has to be 1.0
w_max, w_hit, w_rand, w_short = 0.1, 0.8, 0.1, 0.0
lambda_short = 0.01
sigma_hit = 0.05

def plot_perception(p):
    global fig, ax_lambda, ax_sigma, s_lambda, s_sigma, plot_prob, plot_dist_map, plot_z_max, \
        ax_z_max, ax_dist_map, s_z_max, s_dist_map, ax_short, ax_rand, ax_hit, ax_max, s_short, s_rand, s_hit, s_max, \
        p_all
    p_all = p
    fig, ax = plt.subplots(figsize=(config.figure_width,config.figure_width/3.0))
    plt.subplots_adjust(left=0.25, bottom=0.65)
    distance = np.arange(0.01, z_max + 0.5, step=0.01)
    probability = list(map(p, distance))
    plot_prob, = plt.plot(distance, probability)
    plot_dist_map, = plt.plot([distance_in_map, distance_in_map], [0.0, 1.0],'g')
    plot_z_max, = plt.plot([z_max, z_max], [0.0, 1.0],'r')
    plt.plot([0,z_max+ 0.5], [0,1],'w')

    ax_z_max = plt.axes([0.25, 0.1, 0.65, 0.03])
    ax_dist_map = plt.axes([0.25, 0.15, 0.65, 0.03])
    ax_lambda = plt.axes([0.25, 0.5, 0.65, 0.03])
    ax_sigma = plt.axes([0.25, 0.55, 0.65, 0.03]) 
    ax_short = plt.axes([0.25, 0.3, 0.65, 0.03])
    ax_rand = plt.axes([0.25, 0.25, 0.65, 0.03])
    ax_hit = plt.axes([0.25, 0.35, 0.65, 0.03])
    ax_max = plt.axes([0.25, 0.4, 0.65, 0.03])
    s_z_max = Slider(ax_z_max, 'z_max', 0.1, 6.0, valinit=z_max)
    s_dist_map = Slider(ax_dist_map, 'distance_in_map', 0.1, 6.0, valinit=distance_in_map)
    s_lambda = Slider(ax_lambda, 'lambda_short', 0.001, 1.0, valinit=lambda_short)
    s_sigma = Slider(ax_sigma, 'sigma_hit', 0.001, 1.0, valinit=sigma_hit)
    s_short= Slider(ax_short, 'w_short', 0.001, 1.0, valinit=w_short)
    s_rand= Slider(ax_rand, 'w_rand', 0.001, 1.0, valinit=w_rand)
    s_hit = Slider(ax_hit, 'w_hit', 0.001, 1.0, valinit=w_hit)
    s_max = Slider(ax_max, 'w_max', 0.001, 1.0, valinit=w_max)
    s_z_max.on_changed(update_perception_plot)
    s_dist_map.on_changed(update_perception_plot)
    s_lambda.on_changed(update_perception_plot)
    s_sigma.on_changed(update_perception_plot)
    s_short.on_changed(update_perception_plot)
    #s_rand.on_changed(update_perception_plot)
    s_hit.on_changed(update_perception_plot)
    s_max.on_changed(update_perception_plot)
    plt.show()

def update_perception_plot(val):
    global z_max, distance_in_map, plot_prob, plot, dist_map, plot_z_max, p_all, lambda_short, sigma_hit, \
        w_short, w_hit, w_max, w_rand
    if s_short.val + s_hit.val + s_max.val < 1.0:
        w_short = s_short.val
        w_hit = s_hit.val
        w_max = s_max.val
        w_rand = 1.0 - (w_short + w_hit + w_max)
        s_rand.set_val(w_rand)
    else:
        pass
        #ax_rand.set_facecolor('r')
    lambda_short = s_lambda.val
    sigma_hit = s_sigma.val
    z_max = s_z_max.val
    distance_in_map = s_dist_map.val
    distance = np.arange(0.01, z_max + 0.5, step=0.01)
    probability = map(p_all, distance)
    plot_prob.set_xdata(distance)
    plot_prob.set_ydata(probability)
    plot_dist_map.set_xdata([distance_in_map, distance_in_map])
    plot_z_max.set_xdata([z_max, z_max])
    fig.canvas.draw_idle()
