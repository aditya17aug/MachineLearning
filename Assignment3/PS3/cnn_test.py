# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:34:38 2018

@author: Pooja Jaiswal
"""
import numpy as np
import sys
import cv2
import glob
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.models import Sequential
from keras.datasets import mnist
from keras.preprocessing import image
from keras import backend as K

def precision(y_true, y_pred):
    # Calculates the precision
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def recall(y_true, y_pred):
    # Calculates the recall
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

# dimensions of images
img_width, img_height = 28, 28

# loading 
print("Model is loading...!!")
model = load_model('cnn_model.h5',custom_objects={'recall': recall, 'precision':precision})
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy',recall,precision])
while(1):
    imageFileName= None
    if len(sys.argv) == 2:
        imageFileName = sys.argv[1]
        print("Enter image filepath: ",imageFileName) 
    else:
        print("!!Opps... Please provide an image filepath.")   
        break
    test_image = cv2.imread(imageFileName)
    test_image_resize = cv2.resize(test_image,  (img_width, img_height)) # resizing image into model size
    test_image_gray = cv2.cvtColor(test_image_resize, cv2.COLOR_BGR2GRAY) # converting image into grayscale
    test_image_blur = cv2.blur(test_image_gray,(5,5))
    test_image_thr = cv2.adaptiveThreshold(test_image_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2) #appling Gussian threshhold
    test_image_flt = test_image_thr.astype('float32')
    batch = np.reshape(test_image_flt,[img_width,img_height,1])
    batch /= 255
    batch_expand = np.expand_dims(batch,axis=0)
    y_pred= model.predict(x=batch_expand) # classifying binary image
    cls_pred = np.argmax(y_pred, axis=1)
    # to check even/odd
    if cls_pred is None:
        print("Selected image is not a valid image")
    else:
        if(cls_pred == 0):
            print("Selected image is an even number")
        else:
            print("Selected image is an odd number")
    cv2.imshow('Original Image',test_image) #load original image
    cv2.imshow('Binary Image',batch) # load binary image
    k = cv2.waitKey(0)
    if k == ord('q')or ord('Q'): # Esc
        cv2.destroyAllWindows()
        break