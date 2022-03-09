import cv2
import numpy as np
import scipy.ndimage


def main():
    """
    Percobaan kedua

    - mean filter
    """
    img_path = "/home/yeyee/Pictures/2592b4393564b7f08636f98bbe52fb9d.png"

    # load image (return value adalah array numpy)
    img_bgr: np.ndarray = cv2.imread(img_path)

    img_gray: np.ndarray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # buat filter dengan size 5x5
    # lalu dibagi 25 untuk normalisasi
    filter = np.ones((5, 5))
    filter_normalized = filter / 25

    # proses filtering dengan konvolusi
    img_filtered = scipy.ndimage.filters.convolve(img_gray, filter_normalized)

    # proses stacking
    img_stacked = np.concatenate((img_gray, img_filtered), axis=1)

    # show image di window
    window_title = "Program Pertama"

    cv2.imshow(window_title, img_stacked)

    # on close
    cv2.waitKey()
    cv2.destroyAllWindows()
