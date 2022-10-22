import numpy as np
import matplotlib.pyplot as plt

row = int(800)
col = int(800)
print('row,col =', row, ',', col)


def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lb, lg):
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    if x1 <= x2: a, b = x1, x2
    if x2 < x1: a, b = x2, x1
    if y1 <= y2: c, d = y1, y2
    if y2 < y1: c, d = y2, y1
    dy = y2 - y1
    dx = x2 - x1

    if(abs(dy) <= abs(dx)):
        my = dy / dx
        for i in range(a, b):
            j = int(my * (i - x1) + y1)
            x = i
            y = j
            print('x, y =',x,y)
            for i in range(x - hw, x + hw):
                for j in range(y-hw, y +hw):
                    if((i -x) ** 2 + (j-y) ** 2) < hw ** 2 :
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    if(abs(dy) > abs(dx)):
        mx = dx / dy
        for j in range(c, d):
            i = int(mx * (j - y1) + x1)
            y = j
            x = i

            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

y0, x0 = 400, 400
y1, x1 = 200, 285; y2, x2 = 200, 515; y3,x3 = 400, 631
y4, x4 = 600, 515; y5, x5 = 600, 285; y6, x6 = 400, 169

pd = int(6); pr = 255; pg = 0; pb = 0

lw = int(6); lr = 255; lg = 0; lb = 0
hd = int(pd/2)
hw = int(lw/2)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
Gambar[:, :, :] = 255

hasil = buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil

hasil = buat_garis(Gambar, y2, x2, y3, x3, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil

hasil = buat_garis(Gambar, y3, x3, y4, x4, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil

hasil = buat_garis(Gambar, y4, x4, y5, x5, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil

hasil = buat_garis(Gambar, y5, x5, y6, x6, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil

hasil = buat_garis(Gambar, y6, x6, y1, x1, hd, hw, pr, pb, pg, lr, lb, lg)
Gambar = hasil


plt.figure()
plt.imshow(Gambar)
plt.show()