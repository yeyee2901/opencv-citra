import cv2
import os
import numpy as np
from skimage.filters.thresholding import threshold_otsu


def main():
    """
    Percobaan keempat

    segmentasi gambar dengan teknik Otsu thresholding
    """
    # load the image.
    img_path = "Botol.jpg"
    img1 = cv2.imread(img_path)

    # transformasi ke grayscale 8 bit
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./percobaan-keempat/botol-grayscale.png", img1_gray)

    # kalkulasi nilai threshold menggunakan fungsi threshold_otsu()
    # dari library scikit-image
    threshold_value = threshold_otsu(img1_gray)
    print(f"Nilai threshold gambar: {threshold_value}")

    # aplikasikan threshold ke gambar, dan maksimalkan nilainya
    # sehingga gambar akhir adalah putih sempurna (255) ATAU hitam sempurna (0)
    img2 = 255 * (img1_gray > threshold_value)

    # force konversi ke array 8-bit agar tidak error
    img2 = np.array(img2, dtype=np.uint8)

    # tampilkan gambar
    winname = "Otsu"
    cv2.imshow(winname, img2)
    cv2.waitKey()

    # cleanup
    cv2.destroyAllWindows()

    # simpan hasil
    cv2.imwrite("./percobaan-keempat/botol-otsu.png", img2)
