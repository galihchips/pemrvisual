import numpy as np
from matplotlib import pyplot as plt

#FUNCTION TO ADD TEXT TO AN IMAGE
def add_text_to_image(image, pos_y, pos_x, ch, R, G, B, ukuran_teks):
    char_d = np.array([[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 1, 1 ,1, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])

    char_e = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]])
    char_f = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


    if ch == "d": char = char_d
    if ch == "e": char = char_e
    if ch == "f": char = char_f

    print(char)
    m, n = char.shape  #Ukuran char by default adalah 14 x 12 (kurang lebih setara text size 12).

    print(m, n)
    zoom_factor = round(ukuran_teks/12)
    m_ = round(m/zoom_factor); n_ = round(n/zoom_factor)
    print(m_, n_)

    #if ukuran_teks < 12
        #Lakukan operasi downsize char dari 14x12 ke 7x6

    #if ukuran_teks == 24:
        #Lakukan operasi upsize char dari 14x12 ke 28x24

    #Teks bersifat transparan.
    #Piksel pada posisi selain "1" warnanya tetap mengikuti latar.
    for i in range(0, m):
        for j in range(0, n):
            if char[i, j] == 1:
                image[pos_y+i, pos_x+j, 0] = R
                image[pos_y+i, pos_x+j, 1] = G
                image[pos_y+i, pos_x+j, 2] = B

    return image

#====================================================================================
#USER ENTRIES
#====================================================================================
Y = 300; X = 300                                    #Resolution of the whole image.

#====================================================================================
#MAIN PROGRAM
#====================================================================================
#PREPARING IMAGE TO BE ADDED BY TEXTS
latar_hitam = np.zeros(shape=(Y, X, 3), dtype=np.uint8)
latar_putih = np.zeros(shape=(Y, X, 3), dtype=np.uint8)
latar_putih[:, :, :] = 255

#POSITION, COLOR AND SIZE OF THE TEXT
start_y = int(round(0.1*Y)); start_x = int(round(0.1*X))
pos_y = start_y; pos_x = start_x
R = int(0); G = int(0); B = int(0)
ukuran = 12

#CALL THE FUNCTION FOR ADDING THE TEXT
gambar_dan_teks = add_text_to_image(latar_putih, pos_y, pos_x, "d", R, G, B, ukuran)
pos_x = pos_x + 12
gambar_dan_teks = add_text_to_image(latar_putih, pos_y, pos_x, "e", R, G, B, ukuran)
pos_x = pos_x + 12
gambar_dan_teks = add_text_to_image(latar_putih, pos_y, pos_x, "f", R, G, B, ukuran)
# pos_x = pos_x + 12
# gambar_dan_teks = add_text_to_image(latar_putih, pos_y, pos_x, "1", R, G, B, ukuran)
# pos_x = pos_x + 7
# gambar_dan_teks = add_text_to_image(latar_putih, pos_y, pos_x, "2", R, G, B, ukuran)

#SHOW THE RESULT
plt.imsave("gambar_dan_teks.jpg", gambar_dan_teks)

plt.figure(figsize=(7, 5), dpi=200)   #Width and height of the image window in inches.
plt.imshow(gambar_dan_teks)
plt.show()