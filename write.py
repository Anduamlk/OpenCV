import  cv2
img = cv2.imread('andu.jpg',1)
print(img)
cv2.imshow('andu',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('andu_copy.jpg',1)
cv2.destroyAllWindows()
