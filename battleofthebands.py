import json

# Debugging framework
DEBUG = True


def debug(msg):
    if DEBUG:
        print("-> [DEBUG]: " + msg)


# A dictionary of the bands.
bands = {}

# Whether bands are being inputted, for loop control.
inputtingBands = True

# Whether the data has not been loaded, to check whether to ask for it.
notLoadedData = True

try:

    # Try to open the file, and load data if it can.
    with open("bands.json", "r") as infile:
        bands = json.loads(infile.read())
        inputtingBands = False
        notLoadedData = False

except FileNotFoundError:

    # Debug that the file wasn't found, also in except
    # clause to hide stacktrace.
    debug("The file was not found, asking for info.")


# Function to add band to dictionary.
def input_band(band):
    if inputtingBands:
        bands[band] = 0


# Load data if required.
if notLoadedData:

    # Loop until received 'end'.
    while inputtingBands:

        # Prompt the user to input the band.
        inp = input("Please enter the name of the band to add, or 'end' if there are no more: ")

        # Check if the user wants to stop inputting
        # bands, in that case to as we are told.
        if inp.lower() == "end":
            inputtingBands = False

        # Request input.
        input_band(inp)

    # Request data for amount of votes.
    for key in bands:

        # Prompt the user to input votes.
        inp = int(input("Please enter the amount of votes for '" + key + "': "))

        # Set the votes in the dictionary.
        bands[key] = inp

    # Open the file (python creates it if it doesn't exist).
    with open("bands.json", "w") as outfile:

        # Serialize the dictionary in the form
        # of a JSON string.
        json.dump(bands, outfile)


else:

    # Notify the user that the data was loaded
    # from a previous session.
    print("Loaded data from file. Please delete bands.json and restart the program if you don't want this to happen.")

# Add a fancy results header.
print("")
print("---------------------------------------")
print("+\t\tResults\t\t      +")
print("---------------------------------------")
print("")

# Counter variable.
i = len(bands) + 1

# Iterate through the bands, ordered.
for key, value in sorted(bands.items(), key=lambda x: x[1]):

    # negate from counter.
    i -= 1

    # Print result.
    print(str(i) + ": " + key + " - ", value)
