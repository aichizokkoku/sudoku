import pytesseract
from PIL import Image

url_img = '/home/ec2-user/environment/sudoku/sudoku.png'
img = Image.open(url_img)
number = pytesseract.image_to_string(img)
print (number)