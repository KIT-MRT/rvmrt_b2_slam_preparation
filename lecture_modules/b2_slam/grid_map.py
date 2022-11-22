import bresenham
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def invert_color(value):
    return 1.0 - value

def onclick(event):
    update_function((int(event.ydata), int(event.xdata)), robot_position)
    im.set_data(map(invert_color, grid_map))
    return [im]

def plot_grid_map(position, update):
    global grid_map, im, update_function, robot_position
    update_function = update
    robot_position = position
    fig, ax = plt.subplots()
    normalize = mcolors.Normalize(vmin=0.0, vmax=1.0)
    data = list(map(invert_color, grid_map))
    im = ax.imshow(data, cmap=plt.get_cmap('gray'), norm=normalize, interpolation='nearest')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

def map_distance(x, y):
    """distance between two positions"""
    return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))

def get_perceptual_field(start, end):
    return bresenham.bresenham(start[0], start[1], end[0], end[1])
