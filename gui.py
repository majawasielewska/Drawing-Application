import tkinter as tk
from tkinter import filedialog, messagebox
from shapes import Circle, Rectangle, Line, ShapeType
from canvas import DrawingCanvas
from io_manager import IOManager
import threading

class DrawingApp:
    """
    A class to represent the drawing application.
    """

    def __init__(self, root):
        """
        Initialize the DrawingApp.

        Parameters:
        root (tk.Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Drawify")
        self.canvas_widget = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas_widget.pack()
        self.drawing_canvas = DrawingCanvas(self.canvas_widget)

        self.create_menu()

        self.current_shape = ShapeType.CIRCLE
        self.start_x = self.start_y = 0
        self.temp_shape_id = None  # To keep track of the temporary shape

        self.canvas_widget.bind("<Button-1>", self.on_mouse_click)
        self.canvas_widget.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas_widget.bind("<ButtonRelease-1>", self.on_mouse_release)

    def create_menu(self):
        """
        Create the menu for the application with options for file operations, 
        shape selection, and edit operations.
        """
        menubar = tk.Menu(self.root)
        
        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.load_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Shapes menu
        shapemenu = tk.Menu(menubar, tearoff=0)
        shapemenu.add_command(label="Circle", command=lambda: self.set_shape(ShapeType.CIRCLE))
        shapemenu.add_command(label="Rectangle", command=lambda: self.set_shape(ShapeType.RECTANGLE))
        shapemenu.add_command(label="Line", command=lambda: self.set_shape(ShapeType.LINE))
        menubar.add_cascade(label="Shapes", menu=shapemenu)

        # Edit menu
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="Redo", command=self.redo)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.root.config(menu=menubar)

    def set_shape(self, shape_type):
        """
        Set the current shape to be drawn.

        Parameters:
        shape_type (ShapeType): The type of shape to be drawn.
        """
        self.current_shape = shape_type

    def on_mouse_click(self, event):
        """
        Handle mouse click event to start drawing a shape.

        Parameters:
        event (tk.Event): The event object containing the coordinates of the click.
        """
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        """
        Handle mouse drag event to preview the shape being drawn.

        Parameters:
        event (tk.Event): The event object containing the coordinates of the drag.
        """
        end_x, end_y = event.x, event.y
        
        # Remove the previous temporary shape if it exists
        if self.temp_shape_id:
            self.canvas_widget.delete(self.temp_shape_id)

        # Draw the temporary shape
        if self.current_shape == ShapeType.CIRCLE:
            radius = ((end_x - self.start_x) ** 2 + (end_y - self.start_y) ** 2) ** 0.5
            self.temp_shape_id = self.canvas_widget.create_oval(
                self.start_x - radius, self.start_y - radius,
                self.start_x + radius, self.start_y + radius,
                outline="gray", dash=(2, 2)
            )
        elif self.current_shape == ShapeType.RECTANGLE:
            self.temp_shape_id = self.canvas_widget.create_rectangle(
                self.start_x, self.start_y, end_x, end_y,
                outline="gray", dash=(2, 2)
            )
        elif self.current_shape == ShapeType.LINE:
            self.temp_shape_id = self.canvas_widget.create_line(
                self.start_x, self.start_y, end_x, end_y,
                fill="gray", dash=(2, 2)
            )

    def on_mouse_release(self, event):
        """
        Handle mouse release event to finalize the drawing of a shape.

        Parameters:
        event (tk.Event): The event object containing the coordinates of the release.
        """
        end_x, end_y = event.x, event.y
        shape = None

        # Remove the temporary shape
        if self.temp_shape_id:
            self.canvas_widget.delete(self.temp_shape_id)
            self.temp_shape_id = None

        if self.current_shape == ShapeType.CIRCLE:
            radius = ((end_x - self.start_x) ** 2 + (end_y - self.start_y) ** 2) ** 0.5
            shape = Circle(self.start_x, self.start_y, radius)
        elif self.current_shape == ShapeType.RECTANGLE:
            shape = Rectangle(self.start_x, self.start_y, end_x, end_y)
        elif self.current_shape == ShapeType.LINE:
            shape = Line(self.start_x, self.start_y, end_x, end_y)
        
        if shape:
            self.drawing_canvas.add_shape(shape)

    def undo(self):
        """
        Undo the last action.
        """
        self.drawing_canvas.undo()

    def redo(self):
        """
        Redo the last undone action.
        """
        self.drawing_canvas.redo()

    def save_file(self):
        """
        Save the current drawing to a file.
        """
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            threading.Thread(target=IOManager.save_shapes, args=(self.drawing_canvas.shapes, filename)).start()

    def load_file(self):
        """
        Load a drawing from a file.
        """
        filename = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            def load_and_draw():
                shapes = IOManager.load_shapes(filename)
                self.drawing_canvas.shapes = shapes
                self.drawing_canvas.redraw()

            threading.Thread(target=load_and_draw).start()