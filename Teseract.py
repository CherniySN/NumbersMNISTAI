import cv2
import imutils as imutils
import numpy as np
from PIL import Image
import pytesseract
#import matplotlib.pyplot as plt


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def teseracted(fname):
    img = cv2.imread(fname)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.bilateralFilter(grayimg, 25, 15, 5)
    ing_filter = cv2.blur(grayimg, (1, 5))
    edges = cv2.Canny(ing_filter, 20, 200)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(img, config=config,  lang='rus')
    print(data)

    for i, vale in enumerate(data.splitlines()):
            if i == 0:
                continue
            vale = vale.split()
            x, y, w, h = int(vale[6]), int(vale[7]), int(vale[8]), int(vale[9])
            #cv2.rectangle(img, (x, y), (w+x, h+y), (0,214,120), 1)
            try:
                cv2.putText(img, vale[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)
            except:
                print('---')
    cv2.imwrite('result.jpg', img)

#i = 0
#for cont in contours:
        #сглаживание и определение количества углов
        #sm = cv2.arcLength(cont, True)
        #apd = cv2.approxPolyDP(cont, 0.02*sm, True)
        #выделение контуров
        #if len(apd) == 4:
            #cv2.drawContours(img, [apd], -1, (0,255,0), 4)
            #cv2.imwrite('result_{}.jpg'.format(i), img)
            #i+=1

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()


#cv2.imwrite('img_{}.png'.format(2), edges)
#cv2.imshow('Result', bitwise_img)
#cv2.waitKey(0)


'''
image - cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(image, config=config, lang='rus')
print(data)


def rec (data):
    for i, vale in enumerate(data.splitlines()):
        if i == 0:
            continue
        vale = vale.split()


        x, y, w, h = int(vale[6]), int(vale[7]), int(vale[8]), int(vale[9])
        cv2.rectangle(image, (x, y), (w+x, h+y), (0,214,120), 1)
        #cv2.putText(image, vale[11], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0,214,120), 1)
    #except:
        #print('Что-то пошло не так')

rec(data)

cv2.imshow('Result', image)
cv2.waitKey(0)

#print(pytesseract.image_to_string(Image.open('images/ndfl.jpg')))
'''