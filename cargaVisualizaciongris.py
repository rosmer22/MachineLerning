# Importación de librerías necesarias
import cv2

# ------------------------------------------
# 1. Carga y visualización de imagen en color y escala de grises
# ------------------------------------------
imagen = cv2.imread('Imagenes/lenna.png')
imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('Lenna Original', imagen)
cv2.imshow('Lenna Escala grises', imagen_grises)
cv2.imwrite('Imagenes/lenna_gray_2024.png', imagen_grises)
cv2.waitKey(0)
cv2.destroyAllWindows()