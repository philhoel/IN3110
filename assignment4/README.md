# Assignment 4  


## Package

### Requirements

#### Needs:
Python 3.6 or later  
Numpy  
openCV  
Numba  

### Install

The package is called 'openBlur'.  
Can be installed with:  
'python3 setup.py build_ext --inplace'  
'pip install .'  


### How to run  

import: 'import openBlur.blur_1'  
Called with: 'openBlur.blur_1.pythonBlur'  

blur_1: contains pythonBlur  
blur_2: contains numpyBlur  
blur_3: contains numbaBlur  

blur_1, blur_2, blur_3 needs a filename and a new name as the name for new picture  
If blurring multiple times is necessary, give inputname and outputname
same name (needs to be a string).

#### Blurred

import: 'import openBlur.blurred'  
Called with: openBlur.blurred.Blurring  

Contains:  
Blurring (class)  
pythonBlur (method)  
numpyBlur (method)  
numbaBlur (method)  
blur_faces (method)  
create_image (method)  
call (method)  

Initilizing the object takes three keyword arguements: filename, pictureName and array  
If no filename is spesified, use 'array="array-to-give"'.  
Can be used for just maniplulating array, without having a file.  
For more info, see code or print docstrings.  


## Answering assignment  

For assignment 4.1, 4.2 and 4.3, blur_1, blur_2 and blur_3 is created  
with report2.txt and report3.txt  
For assignment 4.5, blur.py is created. Can be runned with  
3 arguments and 2 optional arguments.  
Choosing of function is first, choose between 1, 2 and 3 (Takes in integer value).  
Choosing input filename is second, (Takes string).  
Choosing outputfile name is third.  
Optionals is number of times to loop and if wanting runtime printed out.  
Use --help for more info
For assignment 4.6 and 4.7, see blurred.  
Here is have chosen to redo the whole assigment and make it into  
a class structure for more functionality and overview.  
The class file is added in the package and is recommended for using the program.  
Has the extra assignment 4.7 implemented as a method


## Extra notes

The test_blur.py should work with pytest.  
Tried to use all implementations to test, but they gave minor differences, which was enough to raise AssertionError.  
These faults are commented out since it works perfectly for python implementation.  

Could not get .DS_Store out of github, even after adding it to .gitignore file.
