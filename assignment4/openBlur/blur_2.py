import numpy as np
import cv2
from openBlur.blur_1 import pythonBlur


def numpyBlur(filename, pictureName):
    """
        Blurs a picture using numpy implementation
        Blurs the picture using numpy vectorization
        returns array values
    """
    image = cv2.imread(filename)
    image = image.astype('float')
    PicA2 = np.zeros(np.shape(image))
    h_len, w_len, c_len = image.shape
    PicA2 = (image[1:h_len-1,1:w_len-1,:]
            + image[0:h_len-2,1:w_len-1,:]
            + image[2:h_len,1:w_len-1,:]
            + image[1:h_len-1,0:w_len-2,:]
            + image[1:h_len-1,2:w_len,:]
            + image[0:h_len-2,0:w_len-2,:]
            + image[0:h_len-2,2:w_len,:]
            + image[2:h_len,0:w_len-2,:]
            + image[2:h_len,2:w_len,:]) / 9

    PicA2 = PicA2.astype('uint8')
    cv2.imwrite(pictureName, PicA2)
    
    return PicA2