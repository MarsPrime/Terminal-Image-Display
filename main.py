from PIL import Image   # pillow let read pixels from image
import shutil   # helps to get terminal size
import hexstyle # color symbols in terminal
import sys  # work with arguments from terminal
import os   


def main(argv):

    validate_parameters(argv)


def display_image(image_path : str, crop : int = 1):

    image  = Image.open(image_path)

    image = image.convert("RGBA")

    image_gray = image.convert("L")

    step_x : int = image.height // shutil.get_terminal_size().lines + crop
    step_y : int = image.width // shutil.get_terminal_size().lines + crop

    for y in range(0, image.width, step_y):
        for x in range(0, image.height, step_x):

            try:
                current_pixel_color = rgb_to_hex(image.getpixel((x,y)))
                current_pixel_brightness =image_gray.getpixel((x,y))
            except IndexError as err:
                pass

            print(hexstyle.set(current_pixel_color) + 
                  get_symbol(current_pixel_brightness) + 
                  hexstyle.reset(), end=" ")
            

        print()

def rgb_to_hex(colors : list = [0, 0, 0]) -> str:
    return "#{:02x}{:02x}{:02x}".format(colors[0], colors[1], colors[2])


def get_symbol(brightness : int):
     if brightness == 0:
         return "."

     elif brightness < 50:
         return ":"

     elif brightness < 100:
         return "0"

     elif brightness < 150:
         return "g"

     elif brightness < 200:
         return "&"

     elif brightness <= 255:
         return "@"


def validate_parameters(argv : list):
    match len(argv):

        case 1:
            show_help_message()

        case 2:
            if (check_image_file(argv[-1])):
                display_image(argv[-1])
            
            elif (argv[-1] == "--h" or argv[-1] == "-help"):
                show_help_message()

            else:
                print(f"file {argv[-1]} is not an image or file does not exist")

        case 3:
            
            if not (check_image_file(argv[-2])):
                print(f"file {argv[-2]} is not an image or file does not exist")

            elif not (check_crop_parameter(argv[-1])):
                print(f"crop parameter must be > 0, enetred numeber is {argv[-1]}")

            else:
                display_image(argv[-2], int(argv[-1]))
        
        
def check_image_file(file_path : str):
    file_abs_path : str = (os.path.abspath(file_path))

    if (os.path.isfile(file_abs_path)):
        return True

    else:
        return False


def check_crop_parameter(paramter : str):
    return int(paramter) >= 0


def show_help_message():
    print(f"This program displays image in terminal")
    print(f"Usage: main.py  -help | --h to show help message")
    print()
    print(f"Usage: main.py  path_to_image")
    print(f"Example: main.py ./image.png")
    print()
    print(f"Usage: main.py  path_to_image crop_number")
    print(f"Example: main.py ./image.png 10")
    print()


if __name__ == "__main__":
    main(sys.argv)
