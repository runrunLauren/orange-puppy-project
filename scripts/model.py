from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import pickle

DENSE_LAYER = 2
LAYER_SIZE = 128
CONV_LAYER = 1


def load_data():
    x = [];
    y = []
    pickle_in = open("x.pickle", "rb")
    x = pickle.load(pickle_in)

    pickle_in = open("y.pickle", "rb")
    y = pickle.load(pickle_in)
    return x, y


def get_name():
    global name
    while True:
        name = str(input("Input model name:\n")).replace(" ", "")
        if len(name) > 1:
            break
    return name


x, y = load_data()
x = x / 255.0

model = Sequential()

model.add(Conv2D(LAYER_SIZE, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

for l in range(CONV_LAYER - 1):
    model.add(Conv2D(LAYER_SIZE, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # convert 3D feature maps to 1S feature vectors

for _ in range(DENSE_LAYER):
    model.add(Dense(LAYER_SIZE))
    model.add(Activation('relu'))

model.add(Dense(64))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x, y, batch_size=32, epochs=10, validation_split=0.3)

name = get_name()
model.save(name)
