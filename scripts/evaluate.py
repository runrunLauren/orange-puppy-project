import cv2
import keras
import os

DATADIR = r"testing_set"
CATEGORIES = ["puppies", "empty"]
IMG_SIZE = 100 

model = keras.models.load_model('opp.h5')
puppy_images = []

for category in CATEGORIES: 
    path = os.path.join(DATADIR, category)  # either orange puppy photo or empty
    class_num = CATEGORIES.index(category)  
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        prediction = model.predict(new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1))
        if CATEGORIES[int(prediction[0][0])] == 'puppies':
            puppy_images.append(img)

print("The following images are believed to have puppies")
for img in puppy_images:
    print(img)

