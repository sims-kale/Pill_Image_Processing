
# #Image Reading and Displaying
import cv2
img0 = cv2.imread(r'D:\SHU\ML_lab\Image_Processing\pill_images\000.png') #Blue, Green, Red
# print(img0)
imgamber = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\amber.png")
# print(imgamber)
imgblue= cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\blue.png")
# print(imgblue)
imgwhite = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\white.png")
# print(imgwhite)

# #convert image BGR to RGB

import matplotlib.pyplot as plt
img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
# plt.imshow(img0)
# plt.title('Pill 0')
# plt.show()

imgamber = cv2.cvtColor(imgamber, cv2.COLOR_BGR2RGB)
# plt.imshow(imgamber)
# plt.title('Pill amber')
# plt.show()

imgblue = cv2.cvtColor(imgblue, cv2.COLOR_BGR2RGB)
plt.imshow(imgblue)
plt.title('Pill Blue')
# plt.show()

imgwhite = cv2.cvtColor(imgwhite, cv2.COLOR_BGR2RGB)
plt.imshow(imgwhite)
plt.title('Pill White')
plt.show()

#Image Histogram

channels = ['b','g','r']
for idx,channel in enumerate(channels):
  plt.hist(imgblue[:,:,idx].flatten(),256,[0,255],color=channel, alpha=0.5)
  plt.yscale("log")


#Image thresholding

cv2.imshow('Original Image', img0)
cv2.imshow('Temp Blue', imgblue)

img_blur = cv2.GaussianBlur(img0, (5,5), 0)
img_ms = cv2.pyrMeanShiftFiltering(img_blur, 20, 60)
#edge = auto_canny(img_ms)
cv2.imshow('Mean Shift Filtered Image', img_ms)



thre_blue_low = (190, 150, 150)
thre_blue_high = (255, 210, 200)
bw_blue = cv2.inRange(img_ms,thre_blue_low, thre_blue_high)
cv2.imshow('Binary Blue Image', bw_blue)

#Counting the number of blue pills
# cnts,_ = cv2.findContours(bw_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(f"Number of contours found: {len(cnts)}")
# c_num=0
# display = img0.copy()
# for i,c in enumerate(cnts):
#     # draw a circle enclosing the object
#     ((x, y), r) = cv2.minEnclosingCircle(c)
#     print(f"Contour {i}: center=({x}, {y}), radius={r}")
#     if r>5:
#         c_num+=1
#         cv2.circle(display, (int(x), int(y)), int(r), (0, 255, 0), 2)
#         cv2.putText(display, "Blue #{}".format(c_num), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
#     else:
#         continue
# print(f"Number of Blue Pills: {c_num}")
# cv2.imshow('Detected Blue Pills', display)
cv2.waitKey(0) # wait for a key event to close the window
