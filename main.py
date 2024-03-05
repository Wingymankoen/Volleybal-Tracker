import os

from data import extract_images, import_images


def main():
    pathin = os.getcwd() + '\\Data\\' + 'Vball_vid.mp4'
    pathout = os.getcwd() + '\\Data\\jpeg'
    if not (os.listdir(pathout)):
        extract_images(pathin, pathout)
    init_images = import_images(pathout)


if __name__ == "__main__":
    main()
