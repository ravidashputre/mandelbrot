import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def mandelbrot(c,iterations):
    z=[0]
    for i in np.arange(iterations):
        next_z = z[i]**2+c
        z = np.append(z, next_z)
    return z

def decide_point(c,iterations,max_value):
   z_vals = mandelbrot(c, iterations)
   if(abs(z_vals[iterations])<max_value):
       return True

   else:
       return False

def all_points():
    mandelbrot_x = []
    mandelbrot_y = []
    for i in np.arange(-2,1.01,0.01):
        for l in np.arange(-2,1.01,0.01):
            c = complex(i,l)
            if(decide_point(c,10,100)):
                mandelbrot_x=np.append(mandelbrot_x, c.real)
                mandelbrot_y=np.append(mandelbrot_y, c.imag)

    fig, ax = plt.subplots()
    ax.scatter(mandelbrot_x,mandelbrot_y,s=1)
    plt.show()

def window_zoom(x_min,x_max,y_min,y_max):
    mandelbrot_x = []
    mandelbrot_y = []
    fig, ax = plt.subplots()
    plt.axis([y_min,y_max,x_min,x_max])

    for i in np.arange(x_min,x_max+0.01,0.01):
        for l in np.arange(x_min,y_max+.01,0.01):
            c = complex(i,l)
            if(decide_point(c,30,100)):
                mandelbrot_x=np.append(mandelbrot_x, c.real)
                mandelbrot_y=np.append(mandelbrot_y, c.imag)

    ax.scatter(mandelbrot_x,mandelbrot_y,s=1)
    plt.show()


#all_points()
window_zoom(-1.5,1.5,-2,1)
