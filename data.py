import cv2
import glob
import os


def extract_images(input_path, output_path):
    vidcap = cv2.VideoCapture(input_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        cv2.imwrite(output_path + "\\frame%d.jpg" % count, image)  # save frame as JPEG file
        count += 1


def import_images(image_directory):
    jpeg_files = glob.glob(os.path.join(image_directory, '*.jpg')) + glob.glob(os.path.join(image_directory, '*.jpeg'))
    # Read all images in a single call
    images = [cv2.imread(image_path) for image_path in jpeg_files]
    return images