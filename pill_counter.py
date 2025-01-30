
#Image Reading
import cv2
img0 = cv2.imread(r'D:\SHU\ML_lab\Image_Processing\pill_images\000.png') #Blue, Green, Red
print(img0)
imgamber = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\amber.png")
print(imgamber)
imgblue= cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\blue.png")
print(imgblue)
imgwhite = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\white.png")
print(imgwhite)

#convert image BGR to RGB

import matplotlib.pyplot as plt
img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
plt.imshow(img0)
plt.title('Pill 0')
plt.show()

imgamber = cv2.cvtColor(imgamber, cv2.COLOR_BGR2RGB)
plt.imshow(imgamber)
plt.title('Pill amber')
plt.show()

imgblue = cv2.cvtColor(imgblue, cv2.COLOR_BGR2RGB)
plt.imshow(imgblue)
plt.title('Pill Blue')
plt.show()

imgwhite = cv2.cvtColor(imgwhite, cv2.COLOR_BGR2RGB)
plt.imshow(imgwhite)
plt.title('Pill White')
plt.show()

