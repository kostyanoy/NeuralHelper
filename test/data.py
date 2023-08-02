import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical

# example of data loader file
def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    print(np.array(x_train).shape)

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    return x_train, y_train, x_test, y_test, None, None
