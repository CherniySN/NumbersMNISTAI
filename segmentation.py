import cv2
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow import keras
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

model = tf.keras.models.load_model('cnn_digits_28x28.h5')
#model = tf.keras.models.load_model('numbers_mnist_dense.h5')


def cnn_digits_predict(model, image_file):
    image_size = 28
    img = keras.preprocessing.image.load_img(image_file,
                                             target_size=(image_size, image_size), color_mode='grayscale')
    img_arr = np.expand_dims(img, axis=0)
    img_arr = 1 - img_arr / 255.0
    img_arr = img_arr.reshape((1, 28, 28, 1))

    result = model.predict(img_arr)
    res = np.argmax(result)
    return res

def segmentation_picture():
    img = cv2.imread('images/Example1.jpg')
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.bilateralFilter(grayimg, 25, 15, 5)
    ing_filter = cv2.blur(grayimg, (2, 3))
    edges = cv2.Canny(ing_filter, 20, 200)
    contures, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    for c in contures:
        approx = cv2.approxPolyDP(c, 1, True)
        x, y, w, h = cv2.boundingRect(approx)
        #cropp = img[y - 15:y + h + 15, x - 15:x + w + 15]
        cv2.imwrite('img_{}.png'.format(i), img[y - 15 : y + h + 15, x - 15:x + w + 15])
        prediction = cnn_digits_predict(model, 'img_{}.png'.format(i)) # как сюда передать картиночку вырезанную ?
        PRD = str(prediction)
        recognizeimg = cv2.putText(img, PRD, (x, y - 20), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)
        recognizeimg = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        i += 1

    plt.imshow(cv2.cvtColor(recognizeimg, cv2.COLOR_BGR2RGB))
    plt.show()

segmentation_picture()
