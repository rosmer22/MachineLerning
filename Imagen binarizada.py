import cv2

imagen = cv2.imread('Imagenes/cat_gray.png', cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(imagen, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Gato en escala Grises', imagen)
cv2.imshow('Gato en binario', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
