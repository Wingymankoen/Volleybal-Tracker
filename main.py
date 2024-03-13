import os

from data import extract_images, import_images
from findball import get_ball

def main():
    wd = os.getcwd()
    pathin = wd + '\\Data\\' + 'Vball_vid.mp4'
    pathout = wd + '\\Data\\jpeg'
    if not (os.listdir(pathout)):
        extract_images(pathin, pathout)
    init_images = import_images(pathout)
    get_ball(init_images)


if __name__ == "__main__":
    main()
