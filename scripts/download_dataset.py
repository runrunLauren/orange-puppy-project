# Facilitates the downloading of the dataset from the LILA SNAPSHOT project.
# Can be found at http://lila.science/datasets
# All images with Jackals will be downloaded, from the following datasets, all within the SNAPSHOT project:
#   Karoo
#   Kgalagadi
#   Enonkishu
#   Camdeboo
#   Mountain Zebra
#   Kruger

# If needed, the Serengeti SNAPSHOT dataset could be added, which would bring in an additional 2000+ images of
# jackals. I frankly just didn't feel like the extra wait, but that may change.

# Also, for every image with a jackal in it, we will also be downloading an 'empty' image
# from the same park.

import os
import json
import random

JSONDIR = r'utils/JSON_files'
PARKS = ['KAR', 'KGA', 'ENO', 'CDB', 'MTZ', 'KRU']
# SAS URLS obtained from http://lila.science/?attachment_id=792
SAS_URLS = [url.strip() for url in open("utils/urls.txt", 'r')]
CATEGORIES = ['jackalblackbacked', 'empty']

for index in range(len(PARKS)):
    image_count = 0
    park = PARKS[index]
    
    # constants for retrieval of images from SAS blob
    sas_url = SAS_URLS[index]
    base_url = sas_url.split('?')[0]
    sas_token = sas_url.split('?')[1]

    # open json metadata file
    json_file = os.path.join(JSONDIR, "{}.json".format(park))
    with open(json_file, 'r') as f:
        data = json.load(f)

    # extract information from json file
    categories = data['categories'] # list of dictionaries containing 'id' and 'name' each
    annotations = data['annotations']
    images = data['images']

    for species in CATEGORIES:
        # create folder for downloaded images
        output_dir = "Dataset/{}".format(species)
        os.makedirs(output_dir, exist_ok=True)

        # Retrieve the ID of the category
        category_id = list(filter(lambda x: x['name'] == species, categories))[0]['id']

        # Retrieve all the images that match that category
        image_ids = [ann['image_id'] for ann in annotations if ann['category_id'] == category_id]
        # a little magic to ensure we download the same amount of empty images as jackals
        if image_count == 0:
            image_count = len(image_ids)
        else:
            random.shuffle(image_ids)
            image_ids = image_ids[:image_count]
        print('Selected {} of {} images'.format(image_count, len(images)))

        # Retrieve image file names
        filenames = [im['file_name'] for im in images if im['id'] in image_ids]

        # Downloading with azcopy
        print('Downloading images for {0} with azcopy'.format(species))
        
        # Write out a list of files, and use the azcopy "list-of-files" option to download those files
        # this azcopy feature is unofficially documented at
        # https://github.com/Azure/azure-storage-azcopy/wiki/Listing-specific-files-to-transfer
        az_filename = os.path.join(output_dir, 'filenames.txt')
        with open(az_filename, 'w') as f:
            for fn in filenames:
                f.write(fn.replace('\\','/') + '\n')
        cmd = './azcopy copy "{0}" "{1}" --list-of-files "{2}"'.format(
                sas_url, output_dir, az_filename)            
        os.system(cmd)
