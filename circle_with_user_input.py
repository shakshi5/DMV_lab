import tkinter as tk

# User input for radius
radius = int(input("Enter radius of circle: "))

# Create window
root = tk.Tk()
root.title("Animated Circle")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Create circle
x, y = 50, 200
circle = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="blue")

# Animation function
def animate():
    global x
    if x < 550:
        canvas.move(circle, 5, 0)
        x += 5
        root.after(50, animate)

animate()

root.mainloop()