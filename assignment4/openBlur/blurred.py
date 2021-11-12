import numpy as np
import cv2
from numba import jit


class Blurring:

    """
    Blurring class

    Implementation of the assignment in a class structure
    for more functionality and ease of use

    Has methods: pythonBlur, numpyBlur, numbaBlur, blur_faces
    """

    def __init__(self, filename=None, pictureName=None, array=None):
        """
        Initionalizing Blurring class

        1st argument: Which file to use

        2nd argument: What to call new picture

        3rd argument: A array of values

        The 3rd argument is used if no filename exist
        and for creating an image. Does not
        need filename of pictureName for just
        creating a object with the array values

        The array values created by openCV is stored in
        self.imageArray

        2nd argument defaults to 'None'
        if no 2nd argument is given, methods will only return arrays
        with the blurred values and not create a new picture

        3rd argument defaults to 'None'
        if no filename and no array is given, will raise error
        """
        if filename is None and array is None:
            print("Needs a array of values. See doctring for information")
            raise ValueError
        if array is not None and filename is None:
            self.imageArray = array
            self.pictureName = pictureName
        else:
            self.filename = filename
            self.pictureName = pictureName
            self.imageArray = cv2.imread(self.filename)

    def create_image(self):
        cv2.imwrite(self.pictureName, self.imageArray)
        return self.imageArray

    def __call__(self):
        return self.imageArray


    def pythonBlur(self):
        """
        Blurs a picture using python implementation
        Stores values in numpy arrays, but does all computations
        in python using for-loops
        Returns array values
        """
        image = self.imageArray
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

        self.imageArray = PicA2
        self.imageArray = self.imageArray.astype('uint8')
        if self.pictureName is not None:
            cv2.imwrite(self.pictureName, self.imageArray)
        return self.imageArray

    def numpyBlur(self):
        """
        Blurs a picture using numpy implementation
        Blurs the picture using numpy vectorization
        returns array values
        """
        image = self.imageArray
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
        self.imageArray = PicA2
        self.imageArray = self.imageArray.astype('uint8')
        if self.pictureName is not None:
            cv2.imwrite(self.pictureName, self.imageArray)
        
        return self.imageArray

    @jit
    def numbaBlur(self):
        """
        Blurs a picture using numba implementation
        Uses same implementiation as the python method
        but compiles using jit from Numba
        returns array values
        """
        image = self.imageArray
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
        self.imageArray = PicA2
        self.imageArray = self.imageArray.astype('uint8')
        if self.pictureName is not None:
            cv2.imwrite(self.pictureName, self.imageArray)
        return self.imageArray

    def blur_faces(self, xml):
        """
        Extra assignment:
        Blurs faces. Uses an XML file to find faces in a picture
        prints a green rectangle around faces and blurs inside rectangle
        returns array values
        """
        array = self.imageArray
        faceCascade = cv2.CascadeClassifier(xml)
        faces = faceCascade.detectMultiScale(array, scaleFactor=1.025, minNeighbors=5, minSize=(30 , 30))
        print(faces)
        print(" Found {} faces !".format(len(faces)))
        for (x, y, w, h) in faces:
            cv2.rectangle(array, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        for i in range(len(faces)):
            h, w, c = array.shape
            x, y, w, h = faces[i]
            hy = h + y
            wx = w + x

            for H in range(h, hy):
                for W in range(w, wx):
                    for C in range(c):
                        array[H,W,C] = (array[H, W, C]/9
                                    + array[H-1, W, C]/9
                                    + array[H+1, W, C]/9
                                    + array[H, W-1, C]/9
                                    + array[H, W+1, C]/9
                                    + array[H-1, W-1, C]/9
                                    + array[H-1, W+1, C]/9
                                    + array[H+1, W-1, C]/9
                                    + array[H+1, W+1, C]/9)

        
        if self.pictureName is not None:
            cv2.imwrite(self.pictureName, array)

        return array




def main():
    firstTry = Blurring('beatles.jpg', 'test_beatles.jpg')

    for i in range(100):
        firstTry.numbaBlur()

    new_obj = Blurring('beatles.jpg', 'test_beatles2.jpg')
    new_obj.blur_faces('haarcascade_frontalface_default.xml')


    return 0

if __name__ == "__main__":
    
    main()
    