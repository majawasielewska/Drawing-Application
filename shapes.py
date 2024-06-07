from abc import ABC, abstractmethod
from enum import Enum

class ShapeType(Enum):
    """
    Enum to represent different types of shapes.
    """
    CIRCLE = 1
    RECTANGLE = 2
    LINE = 3

class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def draw(self, canvas):
        """
        Abstract method to draw the shape on the given canvas.
        
        Parameters:
        canvas (tk.Canvas): The canvas on which the shape will be drawn.
        """
        pass

class Circle(Shape):
    """
    A class to represent a circle shape.
    """

    def __init__(self, x, y, radius):
        """
        Initialize the circle with center coordinates and radius.

        Parameters:
        x (int): The x-coordinate of the circle's center.
        y (int): The y-coordinate of the circle's center.
        radius (int): The radius of the circle.
        """
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas):
        """
        Draw the circle on the given canvas.

        Parameters:
        canvas (tk.Canvas): The canvas on which the circle will be drawn.
        """
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)

class Rectangle(Shape):
    """
    A class to represent a rectangle shape.
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the rectangle with the coordinates of two opposite corners.

        Parameters:
        x1 (int): The x-coordinate of the first corner.
        y1 (int): The y-coordinate of the first corner.
        x2 (int): The x-coordinate of the opposite corner.
        y2 (int): The y-coordinate of the opposite corner.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        """
        Draw the rectangle on the given canvas.

        Parameters:
        canvas (tk.Canvas): The canvas on which the rectangle will be drawn.
        """
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2)

class Line(Shape):
    """
    A class to represent a line shape.
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the line with the coordinates of its two endpoints.

        Parameters:
        x1 (int): The x-coordinate of the first endpoint.
        y1 (int): The y-coordinate of the first endpoint.
        x2 (int): The x-coordinate of the second endpoint.
        y2 (int): The y-coordinate of the second endpoint.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        """
        Draw the line on the given canvas.

        Parameters:
        canvas (tk.Canvas): The canvas on which the line will be drawn.
        """
        canvas.create_line(self.x1, self.y1, self.x2, self.y2)