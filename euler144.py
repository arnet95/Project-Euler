from math import sqrt, acos

startx, starty = 0.0, 10.1
stopx, stopy = 1.4, -9.6

while (not (-0.01 <= stopx <= 0.01)) or stopy < 0:
    scalarprod = stopx - startx + (((starty - stopy) * stopy)/(4*stopx))
    absx = sqrt(1+(stopy/(4*stopx))**2)
    absy = sqrt((stopx-startx)**2 + (stopy-starty)**2)
    theta = acos(scalarprod/(absx*absy))
