from os import getcwd, listdir
from os.path import join, basename

import cv2


# Load paths
bag_folder_path = join(getcwd(), 'autoferry_bags')
# bag_names = listdir(bag_folder_path)
# bag_paths = [join(bag_folder_path, bag_name) for bag_name in bag_names if bag_name.endswith('.bag')]

# Load test bag
bag_names = '2020-09-15-14-29-27.bag'
bag_paths = [join(bag_folder_path, bag_name) for bag_name in bag_names]

# Define topics
front_image_topic = '/EO/F/image_raw'
front_left_image_topic = 'EO/FL/image_raw'
front_right_image_topic = 'EO/FR/image_raw'
image_topics = [front_image_topic, front_left_image_topic, front_right_image_topic]

# Define video output directory
video_output_dir = join(getcwd(), 'videos')

# Define videowriter settings
fps = 22
resolution = (2448, 2048)
# h x w = 2048 x 2448 for all cameras -> Previously inputted is apparently w x h, seems to check out

# Define videowriter and bridge
fourcc = cv2.VideoWriter_fourcc(*'H264')
bridge = CvBridge()


for bag_path in bag_paths:
    # Define output paths
    bag_name = basename(bag_path)
    video_output_path = join(video_output_dir, bag_name)
    bag = Bag(bag_path)
    for topic in image_topics:
        # E.g 'EO_F.avi'
        video_name = join(video_output_path, 'EO_' + topic.split('/')[1] + '.avi')
        out = cv2.VideoWriter(video_name, fourcc, fps, resolution)

        for _topic, msg, t in bag.read_messages(topics=[topic]):



