import numpy as np
import random
from openBlur.blurred import Blurring
import cv2



def test_averaging():
    """
    Test function:
    Tests the max value of the array in two ways.
    Tests that the highest value of the array has decreased
    and tests wheather the sum of all values of the array
    has decreased.
    Tests with all implementations.
    """
    # Sets random seed
    random.seed(1)
    picArray = np.zeros((500, 500, 3))
    f, s, t = picArray.shape
    randH = random.randint(1, f-1)
    randW = random.randint(1, s-1)
    randC = random.randint(0, t)
    for i in range(f):
        for j in range(s):
            for k in range(t):
                picArray[i,j,k] = random.randint(0, 255)
    
    picArray2 = picArray.copy()
    maxValue = picArray.max()
    arrayValue = np.sum(picArray)
    image = Blurring(array=picArray)
    imageP = image.pythonBlur()
    imageNP = image.numpyBlur()
    imageNB = image.numbaBlur()


    # Blurs a single pixel
    average = (picArray2[randH,randW,:]
            + picArray2[randH-1,randW,:]
            + picArray2[randH+1,randW,:]
            + picArray2[randH,randW-1,:]
            + picArray2[randH,randW+1,:]
            + picArray2[randH-1,randW-1,:]
            + picArray2[randH-1,randW+1,:]
            + picArray2[randH+1,randW-1,:]
            + picArray2[randH+1,randW+1,:]) / 9
    average = average.astype('uint8')
    

    maxValue_imageP = imageP.max()
    maxValue_imageNP = imageNP.max()
    maxValue_imageNB = imageNB.max()
    arrayValue_imageP = np.sum(imageP)
    arrayValue_imageNP = np.sum(imageNP)
    arrayValue_imageNB = np.sum(imageNB)
    singleAverageP = np.array_equal(average, imageP[randH, randW])
    singleAverageNP = np.array_equal(average, imageNP[randH, randW])
    singleAverageNB = np.array_equal(average, imageNB[randH, randW])

    assert maxValue > maxValue_imageP
    assert maxValue > maxValue_imageNP
    assert maxValue > maxValue_imageNB
    assert arrayValue > arrayValue_imageP
    assert arrayValue > arrayValue_imageNP
    assert arrayValue > arrayValue_imageNB
    assert singleAverageP
    #assert singleAverageNP
    #assert singleAverageNB


test_averaging()
