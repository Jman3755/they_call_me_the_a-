from tkinter import Tk, Canvas

class GUI:
    def __init__(self, root, title, dimensions):
        self.root = root
        self.title = title
        self.dimensions = dimensions
        root.geometry(dimensions)

class CanvasWidget:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)

    def CreateRect(self, topLeftX, topLeftY, bottomRightX, bottomRightY, fill):
        self.canvas.create_rectangle(topLeftX, topLeftY, bottomRightX, bottomRightY, fill=fill)

if __name__ == '__main__':
    window = GUI(Tk(), 'This is Window Title', '960x540')
    canvasMain = CanvasWidget(window.root, 960, 540)
    canvasMain.canvas.pack()
    rectangleOne = canvasMain.CreateRect(0, 0, 480, 270, "green")
    rectangleTwo = canvasMain.CreateRect(480, 0, 960, 270, "red")
    rectangleThree = canvasMain.CreateRect(0, 270, 480, 540, "yellow")
    rectangleFour = canvasMain.CreateRect(480, 270, 960, 540, "purple")
    window.root.mainloop()