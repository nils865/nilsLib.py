def clampTo(comma, number):
    return int(number * (10 ** comma)) / (10 ** comma)

def setColor(r,g,b):
    return(f"\x1b[38;2;{r};{g};{b}m")

def setBackgroundColor(r,g,b):
    return(f"\x1b[48;2;{r};{g};{b}m")