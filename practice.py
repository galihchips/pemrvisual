import numpy as np
import matplotlib.pyplot as plt

#################################### USER ENTRY #####################################
x1 = 100
y1 = 200
x2 = 100
y2 = 800

pd = int(30)
lw = int(10)

radius = int(pd/2)
hw = int(lw/2)

row = int(1080)
col = int(1920)

print('col, row = ', col, ',', row)


############################# FUNCTION (FUNGSI) ############################
def create_point (radius, y, x, r, g, b):
    for i in range (y-radius, y + radius) :
        for j in range(x-radius, x + radius):
            if((i-y) ** 2 + (j-x) **2 ) < radius ** 2:
                Gambar[j, i, 0] = int(r)
                Gambar[j, i, 1] = int(g)
                Gambar[j, i, 2] = int(b)

    for i in range (x2-radius, x2 + radius) :
        for j in range(y2-radius, y2 + radius):
            if((i-x2) ** 2 + (j-y2) **2 ) < radius ** 2:
                Gambar[j, i, :] = 0
                Gambar[j, i, 2] = 255


############################# PERSIAPAN (PREPARATION) ############################
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
Gambar[:, :, :] = 0


############################# MAIN PROGRAM ############################

dy = y2-y1
dx = x2-x1
# ini untuk garis horizontal
if dy <= dx :
    my = dy/dx
    print('x1, x2 = ', x1, x2)
    for i in range(x1, x2) :
        j = int(my * (i-x1) + y1)
        x = i
        y = j
        for i in range(x-hw, x+hw) :
            for j in range(y-hw, y+hw) :
                if((i-x) **2 + (j-y) **2) < hw ** 2:
                    Gambar[j,i,0] = 255
# ini untuk vertical
if dy > dx :
    mx = dx/dy
    print('dy, dx = ', dy, dx)
    for j in range(y1, y2) :
        i = int(mx * (j-y1) + x1)
        x = i
        y = j
        for i in range(x-hw, x+hw) :
            for j in range(y-hw, y+hw) :
                if((i-x) **2 + (j-y) **2) < hw ** 2:
                    Gambar[j,i,0] = 255
plt.figure()
plt.imshow(Gambar)
plt.show()