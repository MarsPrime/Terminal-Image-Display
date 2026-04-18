# Treminal Image Display
This program shows image in terminal by converting pixels into symbols.

## Dependences:
- python >= 3.13
- hexstyle >= 1.1.1
- pillow >= 12.1.0
  
## Usage
``` python
python3 main.py <path_to_image>
python3 main.py <path_to_image> <crop_paramter>
```
## Parameters
- -help or --h - show help message
- <image_path> - path of image that will be displayed 
- <crop_parameter> - number that shows how lines need to delete from result text (it let image fit into terminal)

## Examples
![Example1](./example_images/image_1.png "example")  
![Example2](./example_images/image_2.png "example")
![Example3](./example_images/image_3.png "example")
![Example4](./example_images/image_4.png "example")

## Use case 
I use it to display music album covers in my terminal when I take notes about them.

## Future functions:
- [ ] Show images with various aspect raito (not only 4x4)
