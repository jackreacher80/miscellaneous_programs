"""
File: image_processing.py
----------------

"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'


def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    # TODO: your code here
    for pixel in image:
        average_pixel_rgb_value = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red >= average_pixel_rgb_value:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = average_pixel_rgb_value
            pixel.green = average_pixel_rgb_value
            pixel.blue = average_pixel_rgb_value

    return image


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
