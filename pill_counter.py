import cv2
import matplotlib.pyplot as plt

# Image Reading
og_img0 = cv2.imread(
    r"D:\SHU\ML_lab\Image_Processing\pill_images\000.png"
)  # Blue, Green, Red
og_imgamber = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\amber.png")
og_imgblue = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\blue.png")
og_imgwhite = cv2.imread(r"D:\SHU\ML_lab\Image_Processing\pill_images\white.png")

# Check if the images were loaded successfully
if og_img0 is None or og_imgamber is None or og_imgblue is None or og_imgwhite is None:
    print("Error: Could not load one or more images.")
    exit()

# Convert image BGR to RGB
img0 = cv2.cvtColor(og_img0, cv2.COLOR_BGR2RGB)
imgamber = cv2.cvtColor(og_imgamber, cv2.COLOR_BGR2RGB)
imgblue = cv2.cvtColor(og_imgblue, cv2.COLOR_BGR2RGB)
imgwhite = cv2.cvtColor(og_imgwhite, cv2.COLOR_BGR2RGB)

# Display images
# plt.imshow(img0)
# plt.title('Pill 0')
# plt.show()

# plt.imshow(imgamber)
# plt.title('Pill amber')
# plt.show()

# plt.imshow(imgblue)
# plt.title('Pill Blue')
# plt.show()

# plt.imshow(imgwhite)
# plt.title('Pill White')
# plt.show()

# Image thresholding
img_blur = cv2.GaussianBlur(og_img0, (5, 5), 0)
img_ms = cv2.pyrMeanShiftFiltering(img_blur, 20, 60)
cv2.imshow("Mean Shift Filtered Image", img_ms)

# Blue Image Histogram
channels = ["b", "g", "r"]
for idx, channel in enumerate(channels):
    plt.hist(og_imgblue[:, :, idx].flatten(), 256, [0, 255], color=channel, alpha=0.5)
    plt.yscale("log")
plt.show()

# Threshold values for blue color
thre_blue_low = (190, 150, 150)
thre_blue_high = (255, 210, 200)
bw_blue = cv2.inRange(img_ms, thre_blue_low, thre_blue_high)
cv2.imshow("Binary Blue Images", bw_blue)

# Counting the number of blue pills
cnts, _ = cv2.findContours(bw_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c_num = 0
display = og_img0.copy()
for i, c in enumerate(cnts):
    # draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if r > 5:
        c_num += 1
        cv2.circle(display, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.putText(
            display,
            "Blue #{}".format(c_num),
            (int(x), int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2,
        )
    else:
        continue
cv2.imshow("Detected Blue Pills ", display)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# White Image Histogram
for idx, channel in enumerate(channels):
    plt.hist(og_imgwhite[:, :, idx].flatten(), 256, [0, 255], color=channel, alpha=0.5)
    plt.yscale("log")
plt.show()

# Threshold values for white color
thre_white_low = (200, 200, 200)
thre_white_high = (255, 255, 255)
bw_white = cv2.inRange(img_ms, thre_white_low, thre_white_high)
cv2.imshow("Binary White Image", bw_white)

# Counting the number of white pills
cnts, _ = cv2.findContours(bw_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Number of white contours found: {len(cnts)}")
c_num = 0

for i, c in enumerate(cnts):
    # Draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    print(f"White Contour {i}: center=({x}, {y}), radius={r}")
    if r > 5:
        c_num += 1
        cv2.circle(display, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.putText(
            display,
            "White #{}".format(c_num),
            (int(x), int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )

print(f"Number of white pills detected: {c_num}")
cv2.imshow("Detected White pills", display)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# Amber Image Histogram
# cv2.imshow(og_imgamber)

channels = ["b", "g", "r"]

for idx, channel in enumerate(channels):
    plt.hist(og_imgamber[:, :, idx].flatten(), 256, [0, 255], color=channel, alpha=0.5)
    plt.yscale("log")

# Threshold values for amber color
thre_amber_low = (0, 0, 200)
thre_amber_high = (60, 120, 255)
bw_amber = cv2.inRange(img_ms, thre_amber_low, thre_amber_high)
cv2.imshow("Binary Amber Image", bw_amber)

# Counting the number of amber pills
cnts, _ = cv2.findContours(bw_amber, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c_num = 0
# display = img.copy()
for i, c in enumerate(cnts):
    # draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if r > 5:
        c_num += 1
        cv2.circle(display, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.putText(
            display,
            "Amber #{}".format(c_num),
            (int(x), int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (10, 10, 255),
            2,
        )
    else:
        continue
cv2.imshow("Detected Amber pills", display)
cv2.waitKey(0)
# cv2.destroyAllWindows()
