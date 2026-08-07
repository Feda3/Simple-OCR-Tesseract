import cv2
import pytesseract

# specify the path for tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# load the image
image = cv2.imread('stop_sign.jpg')

# Apply filters as follows:
# 1. grayscale to remove colors
# 2. slight blur to remove noise
# 3. force a black/white aspect
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, black_and_white_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

# use pytesseract to read the text and print the result
recognized_text = pytesseract.image_to_string(black_and_white_image, config='--psm 6')
print("--------\nHere is what Tesseract saw:", recognized_text.strip(), "\n--------")

# show the final processed immage
cv2.imshow("What Tesseract Sees", black_and_white_image)
cv2.waitKey(0)
