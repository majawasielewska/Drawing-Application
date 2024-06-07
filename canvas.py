from shapes import Shape

class DrawingCanvas:
    """
    A class to represent a drawing canvas which can manage shapes and 
    support undo and redo operations.
    """

    def __init__(self, canvas_widget):
        """
        Initialize the DrawingCanvas.

        Parameters:
        canvas_widget (tk.Canvas): The Tkinter Canvas widget where shapes will be drawn.
        """
        self.canvas_widget = canvas_widget
        self.shapes = []  # List to store the shapes drawn on the canvas
        self.redo_stack = []  # Stack to store shapes for redo functionality

    def add_shape(self, shape: Shape):
        """
        Add a shape to the canvas and clear the redo stack.

        Parameters:
        shape (Shape): The shape to be added to the canvas.
        """
        self.shapes.append(shape)
        self.redo_stack.clear()  # Clear the redo stack when a new shape is added
        self.redraw()

    def undo(self):
        """
        Undo the last shape added to the canvas by removing it from the shapes list
        and adding it to the redo stack.
        """
        if self.shapes:
            self.redo_stack.append(self.shapes.pop())
            self.redraw()

    def redo(self):
        """
        Redo the last undone shape by removing it from the redo stack and adding it 
        back to the shapes list.
        """
        if self.redo_stack:
            self.shapes.append(self.redo_stack.pop())
            self.redraw()

    def redraw(self):
        """
        Redraw all the shapes on the canvas. This clears the canvas and draws each 
        shape in the shapes list.
        """
        self.canvas_widget.delete("all")  # Clear the canvas
        for shape in self.shapes:
            shape.draw(self.canvas_widget)  # Draw each shape on the canvas