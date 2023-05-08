import pytesseract
import argparse
import cv2
import os
from PIL import Image
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of image file")
ap.add_argument("-p", "--preprocess",type=str,default="thresh",help="Preprocessing")
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# gray = cv2.bilateralFilter(gray,9,75,75)
gray = cv2.medianBlur(gray,3)
# gray = cv2.medianBlur(gray,1)
gray = cv2.GaussianBlur(gray,(1,1),0)
gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# kernel = np.ones((3,3),np.uint8)
# gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

export_fol = './output'
if not os.path.exists(export_fol):
    os.makedirs(export_fol)
# filename = os.path.join(export_fol,"{}.jpg".format(os.getpid()))
# cv2.imwrite(filename,gray)

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
instance = Image.fromarray(cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB))
text = pytesseract.image_to_string(instance,lang='vie')

# os.remove(filename)

print(text)

cv2.imshow("image",gray)
cv2.waitKey(0)