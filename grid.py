import tkinter as tk

window = tk.Tk()
window.title("Grid Manager")

for x in range(3):
    for y in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=x, column=y, padx=5, pady=5) # Place frame in grid

        label = tk.Label(master=frame, text=f"Row {x}, Column {y}")
        label.pack() # Pack the label into the frame

window.mainloop()