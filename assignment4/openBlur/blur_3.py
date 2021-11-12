import numpy as np
from numba import jit
import cv2
from openBlur.blur_2 import numpyBlur

@jit
def numbaBlur(filename, pictureName):
    """
        Blurs a picture using numba implementation
        Uses same implementiation as the python method
        but compiles using jit from Numba
        returns array values
    """
    image = cv2.imread(filename)
    image = image.astype('float')
    PicA2 = np.zeros(np.shape(image))
    H_len, W_len, C_len = image.shape
    for h in range(H_len-1):
        for w in range(W_len-1):
            for c in range(C_len):
                PicA2[h][w][c] = (image[h][w][c]
                                + image[h-1][w][c]
                                + image[h+1][w][c]
                                + image[h][w-1][c]
                                + image[h][w+1][c]
                                + image[h-1][w-1][c]
                                + image[h-1][w+1][c]
                                + image[h+1][w-1][c]
                                + image[h+1][w+1][c]) / 9
    PicA2 = PicA2.astype('uint8')
    cv2.imwrite(pictureName, PicA2)
    return PicA2
