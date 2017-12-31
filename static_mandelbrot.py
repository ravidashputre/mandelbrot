import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class Static_mandelbrot:

    def mandelbrot(self,c,iterations):
        self.z=[0]
        for i in np.arange(iterations):
            self.next_z = self.z[i]**2+c
            self.z = np.append(self.z, self.next_z)
        return self.z

    def decide_point(self,c,iterations,max_value):
        self.z_vals = self.mandelbrot(c, iterations)
        if(abs(self.z_vals[iterations])<max_value):
            return True

        else:
            return False

    def all_points(self):
        self.mandelbrot_x = []
        self.mandelbrot_y = []
        for i in np.arange(-2,1.01,0.01):
            for l in np.arange(-2,1.01,0.01):
                c = complex(i,l)
                if(self.decide_point(c,25,100)):
                    self.mandelbrot_x=np.append(self.mandelbrot_x, c.real)
                    self.mandelbrot_y=np.append(self.mandelbrot_y, c.imag)
        self.mandelbrot_set = (self.mandelbrot_x, self.mandelbrot_y)
        return [(self.mandelbrot_x),(self.mandelbrot_y)]

    def window_zoom(self,x_min,x_max,y_min,y_max):
        self.mandelbrot_x = []
        self.mandelbrot_y = []
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis([y_min,y_max,x_min,x_max])
        for i in np.arange(x_min,x_max+0.01,0.01):
            for l in np.arange(x_min,y_max+.01,0.01):
                c = complex(i,l)
                if(self.decide_point(c,25,100)):
                    self.mandelbrot_x=np.append(self.mandelbrot_x, c.real)
                    self.mandelbrot_y=np.append(self.mandelbrot_y, c.imag)
        ax.scatter(self.mandelbrot_x,self.mandelbrot_y,s=1)
        plt.show()
