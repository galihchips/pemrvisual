# import numpy as np
# import matplotlib.pyplot as plt
#
#
# x = np.linspace(-8,8,1000)
# plt.figure(figsize=(4,15))
#
# plt.plot(x, (0.05-x*2)*0.5, '-k')
# plt.plot(x, -((0.05-x*2)*0.05), '-k')
#
# y1 = x -x -0
# y2 = 0.5*x
# y3 = x
# y4 = 2*x
# y5 = -0.5*x
# y6 = -x
# y7 = -2*x
#
# plt.plot(x, y1, '-k', la  bel='y1')
# plt.plot(x, y2, '-r', label='y2')
# plt.plot(x, y3, '-g', label='y3')
# plt.plot(x, y4, '-b', label='y4')
# plt.plot(x, y5, '-y', label='y5')
# plt.plot(x, y6, '-m', label='y6')
# plt.plot(x, y7, '-c', label='y7')
#
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# x1 = 100
# y1 = 200
# x2 = 800
# y2 = 600
#
# lw = int(20)
#
# hd = int(lw/2)
#
# row = int(5/7*1080)
# col = int(5/7*1920)
# print('col, row = ', col, ',', row)
#
#
# Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
# Gambar[:, :, :] = 0
#
# for i in range (x1-hd, x1 + hd) :
#     for j in range(y1-hd, y1 + hd):
#         if((i-x1) ** 2 + (j-y1) **2 ) < hd ** 2:
#             Gambar[j, i, :] = 0
#             Gambar[j, i, 2] = 255
#
# for i in range (x2-hd, x2 + hd) :
#     for j in range(y2-hd, y2 + hd):
#         if((i-x2) ** 2 + (j-y2) **2 ) < hd ** 2:
#             Gambar[j, i, :] = 0
#             Gambar[j, i, 2] = 255
#
# plt.figure()
# plt.imshow(Gambar)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

#################################### USER ENTRY #####################################
x1 = 100
y1 = 200
x2 = 1000
y2 = 800

pd = int(30)
lw = int(10)

hd = int(pd/2)
hw = int(lw/2)

row = int(1080)
col = int(1920)

print('col, row = ', col, ',', row)
############################# FUNCTION (FUNGSI) ############################

############################# PERSIAPAN (PREPARATION) ############################
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
Gambar[:, :, :] = 0

############################# MAIN PROGRAM ############################

for i in range (x1-hd, x1 + hd) :
    for j in range(y1-hd, y1 + hd):
        if((i-x1) ** 2 + (j-y1) **2 ) < hd ** 2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 2] = 255

for i in range (x2-hd, x2 + hd) :
    for j in range(y2-hd, y2 + hd):
        if((i-x2) ** 2 + (j-y2) **2 ) < hd ** 2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 2] = 255
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

# call function from another file
# from simple import luas_lingkaran
# import numpy as np
#
# # create input from user
# print('Masukkan radius : ')
# # declarate value from input to var
# x = input()
# # declarate pi
# pi = 3.14
# # call function
# luas_lingkaran(int(x), pi)
import numpy as np
from matplotlib import pyplot as plt, transforms
# import matplotlib.pyplot as plt
#
# #mengatur nilai titik
# x = np.linspace(-3, 3, 20)
# plt.figure(figsize=(3, 30))
# base = plt.gca().transData
# rot = transforms.Affine2D().rotate_deg(90)
#
#
# plt.plot(x, (0.01 - x ** 2) ** 0.5, '-k')
# plt.plot(x, -((0.01 - x ** 2)) ** 0.5, '-k')
#
# y = x - x - 0
# y1 = -x**3 + 2*x**2 + 2*x - 2
#
# plt.plot(x, y, '-k')
#
# plt.plot(x, y1, '-k', label='y1')
#
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

# plt.figure(figsize=(4, 4), dpi=200)
# X = 100
# Y = 100
#
# gambar = np.zeros(shape=(X, Y, 3), dtype=np.uint8)
# m = 7
# n = 6
#
#
# start_x = 2
# start_y = 2
# T0 = 255 * np.array([
#     [0, 0, 1, 1, 0, 0],
#     [1, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1]]
# )
# T1 = 255 * np.array([
#     [0, 0, 1, 1, 0, 0],
#     [1, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1]]
# )
# gambar[start_y:2+m, start_x:2+n, 2] = T0
# # gambar[8:2+m, 8:2+n, 2] = T1
# # gambar[8:2+m, 2:2+n, 2] = T1
#
# plt.imshow(gambar)
# plt.show()














