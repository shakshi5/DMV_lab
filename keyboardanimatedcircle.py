import matplotlib.pyplot as plt
import numpy as np

# Initial circle properties
x, y = 0, 0
radius = 1

fig, ax = plt.subplots()
plt.xlim(-10, 10)
plt.ylim(-10, 10)

theta = np.linspace(0, 2*np.pi, 100)
circle_line, = ax.plot([], [])

def draw_circle():
    circle_x = x + radius * np.cos(theta)
    circle_y = y + radius * np.sin(theta)
    circle_line.set_data(circle_x, circle_y)
    fig.canvas.draw_idle()

def on_key(event):
    global x, y, radius
    if event.key == 'up':
        y += 0.5
    elif event.key == 'down':
        y -= 0.5
    elif event.key == 'left':
        x -= 0.5
    elif event.key == 'right':
        x += 0.5
    elif event.key == '+':
        radius += 0.2
    elif event.key == '-':
        radius = max(0.2, radius - 0.2)

    draw_circle()

fig.canvas.mpl_connect('key_press_event', on_key)

draw_circle()
plt.title("Interactive Animated Circle (Use Arrow Keys, +/-)")
plt.show()