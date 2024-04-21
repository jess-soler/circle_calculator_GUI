"""
    Jessica Soler
    circle_class.py
    4/20/2024
    calculate the area and circumference of a circle
    with a theme
    GUI
"""
# import the tkinter module with tk standard widgets
from tkinter import *
# override tk widgets with themed ttk widgets if available
from tkinter.ttk import *
# import Vapor theme
import sv_ttk
# import math module for pi (math.pi)
import math
import tkinter


#-------------------------------CIRCLE CALC CLASS------------------------------#
class CircleGUI:
    def __init__(self):     
        
        # create the main window   
        self.root = Tk()
        
        # create the title
        self.root.title("Circle Calculator")
        
        # create the GUI widgets in a separate method
        self.create_widgets()
        
        # set the theme
        sv_ttk.set_theme("light")
        
        # call the mainloop method to start the program
        mainloop()



        
        
#-------------------------------CREATE WIDGETS-------------------------------#
    def create_widgets(self):
        """ create and grid widgets for the GUI """
        
        # create main label frame to hold widgets
        self.main_frame = LabelFrame(
            self.root,                                  # assign to parent window
            text="Enter the radius of the circle: ",    # text for the frame
            relief=GROOVE,                              # decorative border
        )
        
         # create entry widget in the frame to get input from user
        self.entry = Entry(
            self.main_frame,        # assign to parent frame
            width=10,               # width of the entry widget
        )
        
        # create button widget to call the calculate method
        self.btn_calculate = Button(
            self.main_frame,                     # assign to parent frame
            text="Calculate",                    # text on the button
            command=self.calculate               # connect calculate method to button click
        )
        
        # create label in the frame to display the circle calculations
        self.lbl_diameter = Label(
            self.main_frame,             # assign to parent frame
            width=50,                    # width of the label widget in characters
            relief=GROOVE,               # decorative border
            anchor=W,                    # align text to the left (or west)
            font=("Arial", 12, "bold")   # set font style
        )
        
        self.lbl_area = Label(
            self.main_frame,             # assign to parent frame
            width=50,                    # width of the label widget in characters
            relief=GROOVE,               # decorative border
            anchor=W,                    # align text to the left (or west)
            font=("Arial", 12, "bold")   # set font style
        )
        
        self.lbl_circumference = Label(
            self.main_frame,             # assign to parent frame
            width=50,                    # width of the label widget in characters
            relief=GROOVE,               # decorative border
            anchor=W,                    # align text to the left (or west)
            font=("Arial", 12, "bold")   # set font style
        )
        
        # use grid layout manager to place widgets in the frame
        self.entry.grid(row=0, column=0)
        self.btn_calculate.grid(row=0, column=1)
        
        # sticky uses cardinal directions to stick labels
        # to sides of the column
        # sticky=EW expands the label to fit the column width
        # based on the largest widget in the column
        self.lbl_diameter.grid(
            row=1,
            column=0,
            sticky=EW
        )
        self.lbl_area.grid(
            row=2,
            column=0,
            sticky=EW
        )
        self.lbl_circumference.grid(
            row=3,
            column=0,
            sticky=EW
        )
        
        # set padding between frame and window border
        self.main_frame.grid_configure(padx=20, pady=20)
        
        # set padding for all widgets inside the frame
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
            
        # start the program with focus on the entry widget
        self.entry.focus_set()
        
        # grid the main frame in the window
        self.main_frame.grid()
        
        # set padding between frame and window border
        self.main_frame.grid_configure(padx=10, pady=20)
        
        
#-------------------------------CALCULATE/DISPLAY-------------------------------#
    def calculate(self):
        """ 
            method called by the botton click event 
            to calculate diameter, area, and circumference
            of a circle from the given radius
        """
        # get the radius
        self.radius = float(self.entry.get())
        
        # calculate the diameter
        self.diameter = self.radius * 2
        # calculate the area
        self.area = math.pi * self.radius ** 2
        # calculate the circumference
        self.circumference = 2 * math.pi * self.radius
        
        # display the results
        self.lbl_diameter.configure(text=f"Diameter: {self.diameter:,.2f}")
        self.lbl_area.config(text=f"Area: {self.area:,.2f}")
        self.lbl_circumference.config(text=f"Circumference: {self.circumference:,.2f}")
        
        # 0 starts the selection at the beginning of the entry widget text
        # END finishes the selection at the end of the entery widget text
        self.entry.selection_range(0, END)
#-------------------------------RUN PROGRAM-------------------------------#
# create object from the class to run the program
circle_1 = CircleGUI()