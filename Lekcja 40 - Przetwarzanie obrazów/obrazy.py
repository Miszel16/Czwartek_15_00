import cv2
from PIL import Image
import numpy as np

# crtl+shift+p
# Python:Select Interpreter
# nasze .venv

# 1) Wyświetlanie obrazu (opencv)
# a)
def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# b) opencv
def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    show_image(img)
    return img


# c) pillow
def read_image_PIL(path):
    img = Image.open(path)
    try:
        print(img)
    except:
        print(type(img))
    img.show()
    return img

print("OpenCV:\n")
image = read_image_cv("image.jpg")
# obiekt ndarray - tablica


# print("Pillow:\n")
# read_image_PIL("image.jpg")

# 2. Flip obrazka
def reverse_image(img):
    img_reverse = img[::-1]
    return img_reverse

# show_image(reverse_image(image))
# show_image(cv2.flip(image,0))

# 3. Skala szarości
def gray_scale(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            gray = int(sum(img[row][column])/3)
            img[row][column][0] = gray # R
            img[row][column][1] = gray # G
            img[row][column][2] = gray # B
    return np.array(img)

# show_image(gray_scale(image))# wbudowana funkcja
# show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

