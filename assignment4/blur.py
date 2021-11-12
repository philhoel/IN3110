import argparse
import cv2
from openBlur.blur_1 import pythonBlur
from openBlur.blur_2 import numpyBlur
from openBlur.blur_3 import numbaBlur
import time

parser = argparse.ArgumentParser(
        description="Blurring script"
    )

parser.add_argument('Function', help='Which function to use', type=int)
parser.add_argument('Filename', help='Which picture to use')
parser.add_argument('Picturename', help='What to call new picture')
parser.add_argument('--n', help='How many iterations. For more than one, output name = input name', type=int)
parser.add_argument('--time', help='Prints out runtime.')

args = parser.parse_args()
if args.n != None:
    n = args.n
else:
    n = 1

if args.time != None:
    Time = True
else:
    Time = False

if args.Function == 1:
    t = time.time()
    for i in range(n):
        pythonBlur(args.Filename, args.Picturename)
    t2 = time.time()
    if Time == True:
        print(f"Runtime: {t2-t}")
elif args.Function == 2:
    t = time.time()
    for i in range(n):
        numpyBlur(args.Filename, args.Picturename)
    t2 = time.time()
    if Time == True:
        print(f"Runtime: {t2-t}")
elif args.Function == 3:
    t = time.time()
    for i in range(n):
        numbaBlur(args.Filename, args.Picturename)
    t2 = time.time()
    if Time == True:
        print(f"Runtime: {t2-t}")
else:
    print("Function has to be called with 1, 2 or 3. See help for more information")