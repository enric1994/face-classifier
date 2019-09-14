import os
import sys
import logging

import cv2
from keras.models import load_model
import numpy as np

from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.inference import load_image
from utils.preprocessor import preprocess_input

from keras import backend as K

detection_model_path = './trained_models/detection_models/haarcascade_frontalface_default.xml'
emotion_model_path = './trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
gender_model_path = './trained_models/gender_models/simple_CNN.81-0.96.hdf5'

face_detection = load_detection_model(detection_model_path)

# parameters for loading data and images
emotion_labels = get_labels('fer2013')
gender_labels = get_labels('imdb')
font = cv2.FONT_HERSHEY_SIMPLEX


def process_image(image):

    try:


        # hyper-parameters for bounding boxes shape
        gender_offsets = (30, 60)
        gender_offsets = (10, 10)
        emotion_offsets = (20, 40)
        emotion_offsets = (0, 0)

        emotion_classifier = load_model(emotion_model_path, compile=False)
        gender_classifier = load_model(gender_model_path, compile=False)

        # getting input model shapes for inference
        emotion_target_size = emotion_classifier.input_shape[1:3]
        gender_target_size = gender_classifier.input_shape[1:3]

        # loading images
        image_array = np.fromstring(image, np.uint8)
        unchanged_image = cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)

        rgb_image = cv2.cvtColor(unchanged_image, cv2.COLOR_BGR2RGB)
        gray_image = cv2.cvtColor(unchanged_image, cv2.COLOR_BGR2GRAY)

        faces = detect_faces(face_detection, gray_image)

        features = []

        for face_coordinates in faces:
            x1, x2, y1, y2 = apply_offsets(face_coordinates, gender_offsets)
            rgb_face = rgb_image[y1:y2, x1:x2]

            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]

            try:
                rgb_face = cv2.resize(rgb_face, (gender_target_size))
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue

            rgb_face = preprocess_input(rgb_face, False)
            rgb_face = np.expand_dims(rgb_face, 0)
            gender_prediction = gender_classifier.predict(rgb_face)

            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)

            features.append({'gender_prediction_female':str(gender_prediction[0][0]),
            'gender_prediction_male':str(gender_prediction[0][1]),
             'emotion_prediction0':str(emotion_prediction[0][0]),
             'emotion_prediction1':str(emotion_prediction[0][1]),
             'emotion_prediction2':str(emotion_prediction[0][2]),
             'emotion_prediction3':str(emotion_prediction[0][3]),
             'emotion_prediction4':str(emotion_prediction[0][4]),
             'emotion_prediction5':str(emotion_prediction[0][5]),
             'emotion_prediction6':str(emotion_prediction[0][6]),
             'x1':str(x1),
             'x2':str(x2),
             'y1':str(y1),
             'y2':str(y2) 
             })
    except Exception as err:
        logging.error('Error in emotion gender processor: "{0}"'.format(err))


    K.clear_session()
    return features
