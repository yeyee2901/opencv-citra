import cv2
import os
import numpy as np


def main():
    """
    Percobaan pertama

    - mencoba menampilkan gambar pemandangan menggunakan opencv
    """
    img_path = "./pemandangan.png"

    # load image (return value adalah array numpy)
    img: np.ndarray = cv2.imread(img_path)

    # show image di window
    window_title = "Program Pertama"
    cv2.imshow(window_title, img)

    # tekan keyboard apa saja untuk close
    cv2.waitKey()

    # agar clean exit, hapus window nya untuk free resource komputer
    cv2.destroyWindow(window_title)
