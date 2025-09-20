from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np
import os
import random
import string

x_train = []
y_train = []
x_valid = []
y_valid = []


image = ImageCaptcha(width=80, height=30, font_sizes=(21, 25, 28))

image.write('1A0a', 'out.png')

for i in range(60000):
    if i % 100 == 0:
        print(i)
    text = ""
    char_index = []
    # Generate for characters
    for j in range(4):
        # All uppercase letters + lowercase letters + digits
        chars = string.ascii_letters + string.digits  
        rand_char = random.choice(chars)
        text += rand_char
        if '0' <= rand_char <= '9':
            char_index.append(ord(rand_char) - ord('0'))
        elif 'a' <= rand_char <= 'z':
            char_index.append(ord(rand_char) - ord('a') + 10)
        else:
            char_index.append(ord(rand_char) - ord('A') + 36)
    
    y_train.append(char_index)
    
    data = image.generate(text)   # BytesIO

    # Open with PIL
    pil_img = Image.open(data)
    
    # Convert to NumPy array
    np_img = np.array(pil_img)
    x_train.append(np_img)

for i in range(600):
    text = ""
    char_index = []
    # Generate for characters
    for j in range(4):
        # All uppercase letters + lowercase letters + digits
        chars = string.ascii_letters + string.digits  
        rand_char = random.choice(chars)
        text += rand_char
        if '0' <= rand_char <= '9':
            char_index.append(ord(rand_char) - ord('0'))
        elif 'a' <= rand_char <= 'z':
            char_index.append(ord(rand_char) - ord('a') + 10)
        else:
            char_index.append(ord(rand_char) - ord('A') + 36)
    
    y_valid.append(char_index)
    
    data = image.generate(text)   # BytesIO

    # Open with PIL
    pil_img = Image.open(data)
    
    # Convert to NumPy array
    np_img = np.array(pil_img)
    x_valid.append(np_img)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_valid = np.array(x_valid)
y_valid = np.array(y_valid)

os.makedirs("../data", exist_ok=True)
np.savez("../data/dataset.npz", x_train=x_train, y_train=y_train, x_valid=x_valid, y_valid=y_valid)
