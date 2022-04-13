import numpy as np
import cv2

def rgb2gray(img: np.ndarray):
    """
    Fungsi untuk konversi RGB ke grayscale (secara definisi)
    """
    # langkah pertama: slicing array untuk mendapatkan nilai R, G, dan B
    r, g, b = img[:,:,0] , img[:,:,1] , img[:,:,2]

    # sesuaikan dengan persamaan yang diberikan.
    # menggunakan pembagian // agar dilakukan pembulatan secara otomatis
    grayscale = (r + g + b) // 3

    return grayscale

def main():
    """
    Main program
    """
    img: np.ndarray = cv2.imread("../pemandangan.png")

    gray = rgb2gray(img)
    print(gray)

    cv2.imshow("Main window", gray)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    cv2.imwrite("rgb2gray.png", gray)

main()
