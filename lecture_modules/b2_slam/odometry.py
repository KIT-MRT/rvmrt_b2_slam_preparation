import math
import matplotlib.pyplot as plt
from b2_slam import config

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

class Pose(Position):
    def __init__(self, x, y, theta):
        Position.__init__(self, x, y)
        self.theta = theta

def pose_distance(x, y):
    """distance between two positions"""
    return math.sqrt(math.pow(x.x - y.x, 2) + math.pow(x.y - y.y, 2))

def plot_odom(pose, particles, color, next_pose, next_particles, next_color):
    plt.figure(figsize=(config.figure_width,config.figure_width))
    plt.plot([-1,1], [-1,1],'w')
    #plt.arrow(pose.x, pose.y,  0.01 * math.sin(pose.theta), 0.01 * math.cos(pose.theta), color=color)
    for p in particles:
        plt.arrow(p.x, p.y, 0.01 * math.sin(p.theta), 0.01 * math.cos(p.theta), color=color, width=0.0002)
    #plt.arrow(next_pose.x, next_pose.y,  0.01 * math.sin(next_pose.theta), 0.01 * math.cos(next_pose.theta), color=next_color)
    for p in next_particles:
        plt.arrow(p.x, p.y, 0.01 * math.sin(p.theta), 0.01 * math.cos(p.theta), color=next_color, width=0.0002)
    plt.arrow(pose.x, pose.y,  next_pose.x - pose.x, next_pose.y - pose.y, color='g')
    plt.show()
