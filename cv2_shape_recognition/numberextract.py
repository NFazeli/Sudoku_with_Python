import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# img = cv2.imread('first.jpg')
img = cv2.imread('1.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))

# hImg, wImg, _ = img.shape
# conf = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, )
# for b in boxes.splitlines():
#    print(b)
#    b = b.split(' ')
#    print(b)
#    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
#    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
