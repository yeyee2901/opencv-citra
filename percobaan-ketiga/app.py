import cv2
import os
import numpy as np


def main():
    """
    Percobaan ketiga

    - Histogram equalization
    """
    # Opening the image.
    img_path = "/home/yeyee/Pictures/2592b4393564b7f08636f98bbe52fb9d.png"

    img1 = cv2.imread(img_path)
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # 2D array is converted to a 1D array.
    fl = img1.flatten()

    # Histogram and the bins of the image are computed.
    hist, bins = np.histogram(img1, 256, [0, 255])

    # cumulative distribution function is computed
    cdf = hist.cumsum()

    # Places where (cdf = 0) is masked or ignored and
    # rest is stored in cdf_m.
    cdf_m = np.ma.masked_equal(cdf, 0)

    # Histogram equalization is performed.
    num_cdf_m = (cdf_m - cdf_m.min()) * 255
    den_cdf_m = (cdf_m.max() - cdf_m.min())
    cdf_m = num_cdf_m / den_cdf_m

    # The masked places in cdf_m are now 0.
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    # cdf values are assigned in the flattened array.
    im2 = cdf[fl]

    # im2 is 1D so we use reshape command to.
    # make it into 2D.
    im3 = np.reshape(im2, img1.shape)

    img3_gray = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)

    # set image bersebelahan
    img_stacked = np.concatenate((img1, im3), axis=1)
    img_stacked_gray = np.concatenate((img1_gray, img3_gray), axis=1)

    # show image
    cv2.imshow("Percobaan Ketiga", img_stacked_gray)

    # on close
    cv2.waitKey()
    cv2.destroyAllWindows()
