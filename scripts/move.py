import os
import random
import re

TRAIN_DIR = r'training_set'
TEST_DIR = r'testing_set'
CHANCE = list(range(10))

# create folders
os.makedirs("{}/empty".format(TRAIN_DIR),exist_ok=True)
os.makedirs("{}/empty".format(TEST_DIR),exist_ok=True)
os.makedirs("{}/puppies".format(TRAIN_DIR),exist_ok=True)
os.makedirs("{}/puppies".format(TEST_DIR),exist_ok=True)

for root, dirs, files in os.walk("Dataset", topdown=False):
    for file in files:
        origin = "{}/{}".format(root, file)
        # 0.1 chance to be in test set, otherwise it will be used for training
        if random.choice(CHANCE) == 1:
            destination = TEST_DIR
        else:
            destination = TRAIN_DIR

        # depending on the root, it will either be placed in 'empty' or 'puppies'
        if re.search('empty', root) is not None:
            destination += "/empty/{}".format(file)
        else:
            destination += "/puppies/{}".format(file)          

        # move file to new combined folder
        os.rename(origin, destination)

    # delete old folder
    os.rmdir(root)


