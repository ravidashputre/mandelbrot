import static_mandelbrot
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use('TKAgg')

fig, ax = plt.subplots()
get = static_mandelbrot.Static_mandelbrot()
mandelbrot_set=get.all_points()
x_points, y_points = mandelbrot_set
x_update, y_update = [],[]
num_points = len(x_points)
speed_factor = 100
num_frames = ((num_points-num_points%speed_factor)/speed_factor)+1
ln, = plt.plot([],[], 'ro', animated = True)

def init():
    ax.set_xlim(-2, 1)
    ax.set_ylim(-2, 2)
    return ln,

def update(frame):

    it_x = x_points[frame*100+frame:(frame+1)*100+frame]
    it_y = y_points[frame*100+frame:(frame+1)*100+frame]
    global x_update
    global y_update
    x_update = np.append(x_update, it_x)
    y_update = np.append(y_update, it_y)
    ln.set_data(x_update, y_update)
    return ln,

anim = animation.FuncAnimation(fig, update, frames=num_frames,init_func=init, save_count = 200, interval=10,blit=True)
plt.show()
