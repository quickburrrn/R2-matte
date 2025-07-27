import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
x = np.linspace(0, 10, 1000)
a = 1
line, = ax.plot(x, a * np.sin(x))

# Slider setup
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes((0.25, 0.1, 0.65, 0.03), facecolor=axcolor)
slider = Slider(ax_slider, 'Amplitude', 0.1, 10.0, valinit=a)

def update(val):
    amp = slider.val
    line.set_ydata(amp * np.sin(x))
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()