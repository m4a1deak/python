import tesserocr
from PIL import Image

image = Image.open('doimg.jpg')

print(tesserocr.image_to_string(image))
