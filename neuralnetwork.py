import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, \
    AveragePooling2D
from tensorflow.keras.optimizers import SGD, RMSprop, Adam

import tensorflow as tf

import numpy as np


def mnist_cnn_model():
    image_size = 28
    num_channels = 1
    num_classes = 10
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu',
                     padding='same',
                     input_shape=(image_size, image_size, num_channels)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu',
                     padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu',
                     padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())

    model.add(Dense(128, activation='relu'))

    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer=Adam(), loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def mnist_cnn_train(model):
    (train_digits, train_labels), (test_digits, test_labels) = tf.keras.datasets.mnist.load_data()

    image_size = 28
    num_channels = 1

    train_data = np.reshape(train_digits, (train_digits.shape[0], image_size, image_size, num_channels))
    train_data = train_data.astype('float32') / 255.0

    num_classes = 10
    train_labels_cat = tf.keras.utils.to_categorical(train_labels, num_classes)

    val_data = np.reshape(test_digits, (test_digits.shape[0], image_size, image_size, num_channels))
    val_data = val_data.astype('float32') / 255.0
    val_labels_cat = tf.keras.utils.to_categorical(test_labels, num_classes)

    print("Training the network...")

    model.fit(train_data, train_labels_cat, epochs=4, batch_size=64,
              validation_data=(val_data, val_labels_cat))

    return model


model = mnist_cnn_model()
mnist_cnn_train(model)
model.save('cnn_digits_28x28.h5')


def cnn_digits_predict(model, image_file):
    image_size = 28
    img = tf.keras.preprocessing.image.load_img(image_file,
                                                target_size=(image_size, image_size), color_mode='grayscale')
    img_arr = np.expand_dims(img, axis=0)
    img_arr = 1 - img_arr / 255.0
    img_arr = img_arr.reshape((1, 28, 28, 1))

    result = model.predict_classes([img_arr])
    return result[0]
