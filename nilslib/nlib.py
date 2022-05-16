import os, sys
    
def clampDecimalPlace(comma, number): # Clamps the number to a specified number of decimal Places (e.g 0.123 >0.1)
    return int(number * (10 ** comma)) / (10 ** comma)

def setTTYFgCol(r,g,b): # Sets the color of the text foreground (if supported by the terminal)
    return(f"\x1b[38;2;{r};{g};{b}m")

def setTTYBgCol(r,g,b): # Sets the color of the text background (if supported by the terminal)
    return(f"\x1b[48;2;{r};{g};{b}m")

def clear(): # Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

def moveCursor(lines): # Moves the cursor up by given lines
   sys.stdout.write("\x1b[1A" * int(lines))

def resetColor(): # Resets the color to default
    sys.stdout.write("\x1b[0m")
