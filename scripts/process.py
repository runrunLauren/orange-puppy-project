import numpy as np
import os
import cv2
from tqdm import tqdm
import random
import pickle

DATADIR = r"training_set"
CATEGORIES = ["puppies", "empty"]
IMG_SIZE = 100

training_data = []
for category in CATEGORIES: 
    path = os.path.join(DATADIR,category)  # either orange puppy photo or empty
    classification = CATEGORIES.index(category)  # get the classification  (0 for puppies, 1 for empty)

    for img in tqdm(os.listdir(path)):  # iterate over each image per puppies and empty
        try:
            img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
            training_data.append([new_array, classification])  # add this to our training_data
        except Exception as e:
            print("Exception arose: ", e, os.path.join(path,img))
random.shuffle(training_data) # we shuffle so that the puppies and empties are mixed

x = []; y = []
for array, classification in training_data:
    x.append(array)
    y.append(classification)

x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()







