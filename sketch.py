import cv2
img_location = 'Enter the location of your image file '
filename = 'name of your image'
img = cv2.imread(img_location+filename)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)
inverted_blurred_img = 255 - blurred_img
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 200.0)
cv2.imshow('behfv4hv',pencil_sketch_IMG)
cv2.waitKey(0)
print("hi")
