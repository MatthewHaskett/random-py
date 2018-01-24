# Created by Matthew Haskett 20 / 10 / 17
# A program to calculate a triangle's hypotenuse from the two sides
# usage of pythagoras' theorem.

# Imports
import math

from tkinter import *


# Calculate the answer
def calculate():
    # Open try block for checking a number was entered
    try:

        # Get from the entry fields
        side_one = int(sideOneEntryBox.get())
        side_two = int(sideTwoEntryBox.get())

        # Square them both
        side_one = side_one * side_one
        side_two = side_two * side_two

        # Add them and square root
        final_side = side_one + side_two
        final_side = math.sqrt(final_side)
        final_side = round(final_side, 2)

        # Set output text
        outputLabel.config(text="Output: %s" % final_side)

    # Catch ValueError, the exception thrown when entering something not a number.
    except ValueError:

        # Set the output to an error
        outputLabel.config(text="Error, must be numbers")


# Tkinter setup
master = Tk()

# Set the title of the UI
master.title("Pythagoras Solver")

# Add an explanation label
Label(master, text="Enter the two sides of a right angled triangle and hit 'Calculate' to find the hypotenuse").grid(
    row=0)

# Adding labels to the boxes
Label(master, text="Side 1").grid(row=1)
Label(master, text="Side 2").grid(row=2)

# Create entry boxes
sideOneEntryBox = Entry(master)
sideTwoEntryBox = Entry(master)

# Grid the boxes
sideOneEntryBox.grid(row=1, column=1)
sideTwoEntryBox.grid(row=2, column=1)

# Button to calculate
Button(master, text="Calculate", command=calculate).grid(row=3)

# Spacer
Label(master, text=" ").grid(row=4)

# Output text
outputLabel = Label(master, text="Nothing yet, do a calculation")
outputLabel.grid(row=5)

# Start
mainloop()
