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
x_bounds = [-2,1]
y_bounds = [-1.5,1.5]
num_points = len(x_points)
speed_factor = 100
num_frames = ((num_points-num_points%speed_factor)/speed_factor)+1
ln, = plt.plot([],[], 'k,', animated = True)
def init():
    global x_bounds
    global y_bounds
    ax.set_xlim(x_bounds[0], x_bounds[1])
    ax.set_ylim(y_bounds[0], y_bounds[1])
    return ln,

def update(frame):

    global x_points, y_points
    ax.set_xlim(x_bounds[0], x_bounds[1])
    ax.set_ylim(y_bounds[0], y_bounds[1])
    it_x = x_points[frame*100+frame:(frame+1)*100+frame]
    it_y = y_points[frame*100+frame:(frame+1)*100+frame]
    global x_update
    global y_update
    x_update = np.append(x_update, it_x)
    y_update = np.append(y_update, it_y)
    ln.set_data(x_update, y_update)

    return ln,

def on_click(event):
    global click_x, click_y
    global x_bounds, y_bounds
    click_x, click_y = event.xdata, event.ydata
    print(complex(click_x,click_y))
    #get.window_zoom(click_x-.25, click_x+.25, click_y-.25, click_y+.25, 30, 0.005)
    #x_points, y_points = get.window_zoom(x_bounds[0],x_bounds[1],y_bounds[0],y_bounds[1],30,0.005)
    x_bounds = [click_x-.125, click_x+.125]
    y_bounds = [click_y-.125, click_y+.125]

cid = fig.canvas.mpl_connect('button_press_event', on_click)
anim = animation.FuncAnimation(fig, update, frames=num_frames,init_func=init, save_count = 100, interval=100,blit=True, repeat=True)
plt.show()
