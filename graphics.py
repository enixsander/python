from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# %matplotlib notebook

# create lists for the x and y data
data_limit = 50
x = [i for i in range(data_limit)]
y = [0]*data_limit

# create the figure and axes objects
fig, ax = plt.subplots()
line, = ax.plot([])     # A tuple unpacking to unpack the only plot


def init_animate():
    ax.set_xlim([0, data_limit])
    ax.set_ylim([0, 10])
    line.set_data((x, y))
    return line,


# function that draws each frame of the animation
def animate(i, y_data):
    pt = randint(1, 9)  # grab a random integer to be the next y-value in the animation
    y.append(pt)

    if len(y) > data_limit:
        y.pop(0)

    # ax.clear()
    # ax.plot(x[-5:], y[-5:]) # plot the last 5 data points
    # ax.plot(x, y)

    line.set_ydata(y)
    return line,


# run the animation
ani = FuncAnimation(fig, animate, init_func=init_animate, fargs=(y,), interval=100, blit=True)
plt.show()
