import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
import pytesseract
import random



def edgeDetect(image):
    images = []
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    for col in range(9):
        for row in range(14):
            x = row*40
            y = col*40
            images.append(gray[x:x+40, y:y+40])
    print("Divided image into " + str(len(images)) + " squares.")
    return images

def record():
    last_time = time.time()
    printscreen = np.array(ImageGrab.grab(bbox=(0,32,360,595)))
    printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    print("Grabbed screenshot.")
    return printscreen

def findNumbers(images):
    scanarray = []
    for image in images:
        image = Image.fromarray(image)
        string = pytesseract.image_to_string(image)
        print(string)

if __name__ == "__main__":
    findNumbers(edgeDetect(record()))