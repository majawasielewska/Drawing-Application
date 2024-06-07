import tkinter as tk
from gui import DrawingApp

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    
    # Set the application icon
    # This will set the icon of the application window to the specified icon file.
    root.iconbitmap("logo.ico")

    # Initialize the DrawingApp with the main window as the root
    app = DrawingApp(root)
    
    # Start the Tkinter event loop
    # This will keep the application running and responsive to user interactions.
    root.mainloop()