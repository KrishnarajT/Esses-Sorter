import cv2
import pytesseract
import os

img = os.path.join('C:/Users/littl/Desktop/New folder/',  '6.jpg' )
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

def makebetter(pic):
    """"Returns the pic made better for reading with OCR"""
    gray = get_grayscale( pic )
    cann = canny( gray )
    return cann