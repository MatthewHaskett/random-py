# Created by Matthew Haskett 31 / 10 / 17
# A program to log someone into something.
# Usage of Tkinter and JSON.

# Imports
import json

from tkinter import *

# Debugging framework.
DEBUG = True


def debug(msg):
    if DEBUG:
        print("-> [DEBUG]: " + msg)


# Dictionary to store login data.
data = {}

try:
    with open("login.json", "r") as infile:
        data = json.loads(infile.read())

except FileNotFoundError:
    debug("The file was not found.")


# Login
def login():

    # Get from the entry fields
    username = usernameEntryBox.get()
    password = passwordEntryBox.get()

    if username in data:
        if password == data[username]:
            outputLabel.config(text="Logged in")
        else:
            outputLabel.config(text="Incorrect Password!")

    else:
        outputLabel.config(text="Not registered!")


def register():
    # Get from the entry fields
    username = usernameEntryBox.get()
    password = passwordEntryBox.get()

    # Check the user hasn't registered.
    if username in data:
        outputLabel.config(text="Already registered.")

    # Register them
    else:
        data[username] = password

        # Tell them they logged in
        outputLabel.config(text="Registered")


def save():
    with open("login.json", "w") as outfile:
        json.dump(data, outfile)


# Tkinter setup
master = Tk()

# Adding labels to the boxes
Label(master, text="Username").grid(row=1)
Label(master, text="Password").grid(row=2)

# Create entry boxes
usernameEntryBox = Entry(master)
passwordEntryBox = Entry(master, show='•')

# Grid the boxes
usernameEntryBox.grid(row=1, column=1)
passwordEntryBox.grid(row=2, column=1)

# Spacer
Label(master, text=" ").grid(row=3)

# Buttons to login or register
Button(master, text="Login", command=login).grid(row=4, column=1)
Button(master, text="Register", command=register).grid(row=4)
Button(master, text="Save", command=save).grid(row=4, column=2)

# Output label
outputLabel = Label(master, text="")
outputLabel.grid(row=5)

# Start
mainloop()
