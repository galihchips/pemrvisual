import numpy as np
import matplotlib.pyplot as plt

# def luas_lingkaran(r, pi):
#   # declaration val as a main program
#   val = pi*r**2
#
#   # print value
#   print("luas lingkaran adalah", val)
#   # return val
#PROGRAM UNTUK TITIK DAN GARIS
print("\033c")       #To close all
import numpy as np
import matplotlib.pyplot as plt

#The user informs the coordinates of the two points for the line.
y1 = 200
x1 = 100
y2 = 200
x2 = 800

#The user decides the point (vertex) diameter
pd = int(30)
# The user decide the line width
lw = int(10)

#Setting the size of the canvas
col = int(1920)
row = int(1080)
print('col, row =', col, ',', row)

## FUNCTION UNTUK MEMBUAT GARIS
## Once x and y known, create a circle and color it red.
def buat_garis(y1, x1, y2, x2, pd, lw):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16) #Preparing the black canvas
    hd = int(pd/2)                               #Calculate the half point diameter.
    hw = int(lw/2)                              #Calculate the half half line width.
    dy = y2-y1
    dx = x2-x1
    #Untuk garis yang cenderung horisontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j,i,0] = 255
    #Untuk garis yang cenderung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)           #Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ',', y)
            for i in range(x-hw, x+hw):        #Creating a circle surrounding (x,y) and coloring it red
                for j in range(y-hw, y+hw):
                    if ( (i-x)*2 + (j-y)*2 ) < hw **2:
                        Gambar[j,i,0] = 255
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                Gambar[j, i, 0] = 255

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                Gambar[j, i, 0] = 255
    return Gambar

#Coloring the two points red (loop, condition, comparation)


## MAIN PROGRAM
hasil = buat_garis(y1, x1, y2, x2, pd, lw)

plt.figure()
plt.imshow(hasil)
plt.show()