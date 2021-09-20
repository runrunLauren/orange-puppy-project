# Orange Puppy Project
Image classifier: Identifies black-backed jackals in trail camera footage.

### Acknowledgements

Knowing very little about Machine Learning, this was truly just a fun little thing to do that I cannot claim any superior knowledge over. Saying that, this would not be possible without the various tutorials I followed, and most importantly, the availability of good data. To that I owe the [LILA datasets](https://lila.science/datasets/) all  my gratitude.

Now if only I could get a farmer to actually use this...

### Requirements

This project was built on a specific version of Python and Keras. If you wish to run this without any edits, you will have to match the specific Python version.

#### Python 3.6.*
 - install pyenv and download python version 3.6.\<any>
 - set your python version in the project directory `pyenv local 3.6.*`

#### azcopy
 - download azcopy from [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)
 - extract 'azcopy' to the project root

#### Python packages
 - numpy `pip install numpy`
 - cv2  `pip install opencv-python`
 - tqdm `pip install tqdm`
 - keras `pip install keras==2.3.0`
 - specific version required `pip install 'h5py==2.10.0' --force-reinstall`

#### Images
 - run `python scripts/download_dataset.py`
 - if completed correctly, continue with the next step. Otherwise repeat.
 - run `python scripts/move.py`

### Modelling & Classification

#### Parse into correct format
 - run `python scripts/process.py`

#### Create the machine learning model
- run 'python scripts/model.py'. Make sure to input a name for the model when prompted.

### Evaluating pictures
 - By default, images in 'test_set' will be evaluated.
 - Add any images to this directory.
 - run `python script/evaluate.py`
