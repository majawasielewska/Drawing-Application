import json
from shapes import Circle, Rectangle, Line, ShapeType

class IOManager:
    """
    A class to manage input and output operations for shapes.
    """

    @staticmethod
    def save_shapes(shapes, filename):
        """
        Save a list of shapes to a file in JSON format.

        Parameters:
        shapes (list): The list of shapes to be saved.
        filename (str): The name of the file to save the shapes to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([IOManager.shape_to_dict(shape) for shape in shapes], file)
        except Exception as e:
            print(f"Error saving shapes: {e}")

    @staticmethod
    def load_shapes(filename):
        """
        Load shapes from a file in JSON format.

        Parameters:
        filename (str): The name of the file to load the shapes from.

        Returns:
        list: A list of shapes loaded from the file.
        """
        try:
            with open(filename, 'r') as file:
                shape_dicts = json.load(file)
                shapes = [IOManager.dict_to_shape(shape_dict) for shape_dict in shape_dicts]
                return shapes
        except Exception as e:
            print(f"Error loading shapes: {e}")
            return []

    @staticmethod
    def shape_to_dict(shape):
        """
        Convert a shape object to a dictionary.

        Parameters:
        shape (Shape): The shape object to be converted.

        Returns:
        dict: A dictionary representation of the shape.
        """
        if isinstance(shape, Circle):
            return {
                "type": ShapeType.CIRCLE.value,
                "x": shape.x,
                "y": shape.y,
                "radius": shape.radius
            }
        elif isinstance(shape, Rectangle):
            return {
                "type": ShapeType.RECTANGLE.value,
                "x1": shape.x1,
                "y1": shape.y1,
                "x2": shape.x2,
                "y2": shape.y2
            }
        elif isinstance(shape, Line):
            return {
                "type": ShapeType.LINE.value,
                "x1": shape.x1,
                "y1": shape.y1,
                "x2": shape.x2,
                "y2": shape.y2
            }

    @staticmethod
    def dict_to_shape(shape_dict):
        """
        Convert a dictionary to a shape object.

        Parameters:
        shape_dict (dict): The dictionary representation of a shape.

        Returns:
        Shape: The shape object created from the dictionary.
        """
        shape_type = ShapeType(shape_dict["type"])
        if shape_type == ShapeType.CIRCLE:
            return Circle(shape_dict["x"], shape_dict["y"], shape_dict["radius"])
        elif shape_type == ShapeType.RECTANGLE:
            return Rectangle(shape_dict["x1"], shape_dict["y1"], shape_dict["x2"], shape_dict["y2"])
        elif shape_type == ShapeType.LINE:
            return Line(shape_dict["x1"], shape_dict["y1"], shape_dict["x2"], shape_dict["y2"])