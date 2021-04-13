# Test file to summarize all messages in a topic in a respective csv file

# Imports
from os import listdir, getcwd
from os.path import join, splitext

import bagpy
from tqdm import tqdm
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np


bag_folder_path = join(getcwd(), 'autoferry_bags')
bag_names = listdir(bag_folder_path)
bag_paths = [join(bag_folder_path, bag_name) for bag_name in bag_names if bag_name.endswith('.bag')]


test_bag_name = '2020-09-15-14-29-27.bag'
test_bag_path = join(bag_folder_path, test_bag_name)

test_bag = bagreader(test_bag_path)
csv_dir = join(bag_folder_path, splitext(test_bag_name)[0])

# h x w = 2048 x 2448 for all cameras
front_image_topic = '/EO/F/image_raw'
front_left_image_topic = 'EO/FL/image_raw'
front_right_image_topic = 'EO/FR/image_raw'
image_topics = [front_image_topic, front_left_image_topic, front_right_image_topic]

# If already written csv files, do not do again..
assert len(listdir(csv_dir)) == 0, 'The csv directory is not empty and will be overwritten - sure you want this '
for t in tqdm(image_topics):
    if t in test_bag.topics:
        data = test_bag.message_by_topic(t)
    else:
        print('Skipped topic of name {} not found in test_bag'.format(t))

front_image_topic_csv = 'EO-F-image_raw.csv'
front_left_camera_topic_csv = 'EO-FL-image_raw.csv'
front_right_camera_topic_csv = 'EO-FR-image_raw.csv'

front_camera_df = pd.read_csv(join(csv_dir, front_image_topic_csv))

print('Finished writing csv files')


