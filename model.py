from keras.datasets import mnist
from keras.layers import Dense, Flatten, Dropout
from keras.models import Sequential


# example of creating model
# load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

# create model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax'),
])

# compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# test model
test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test data accuracy:', test_acc)

# save model
model.save("saves/test")