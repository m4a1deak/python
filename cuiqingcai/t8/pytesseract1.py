import pytesseract
from PIL import Image

image = Image.open('code2.jpg')
image = image.convert('L')
threshold = 130
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
image.show()
# re = pytesseract.image_to_string(image)
# print(re)
