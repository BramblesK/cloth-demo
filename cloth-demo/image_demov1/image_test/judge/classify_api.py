from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras

import numpy as np


def classify(pic):
    new_model = keras.models.load_model('./judge/my_picmodel.h5')
    probability_model = tf.keras.Sequential([
        new_model,
        tf.keras.layers.Softmax()
    ])
    image = tf.image.decode_jpeg(pic, channels=1)
    image = tf.image.resize(image, [28, 28])
    im = np.array(image, dtype=int)
    im = im.reshape(28, 28)
    im = np.array([im])
    predictions1 = probability_model.predict(im)
    return (np.argmax(predictions1[0]))

