import cv2  # Importar OpenCV

# Abrir la cámara (índice 0 para la webcam predeterminada)
camara = cv2.VideoCapture(0)

while True:
    success, img = camara.read()  # Leer un fotograma
    if not success:
        break  # Si falla la lectura, salir del bucle

    cv2.imshow("Video de camara", img)  # Mostrar el fotograma

    # Esperar 1 ms y salir si se presiona ESC (código ASCII 27)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cerrar todas las ventanas y liberar la cámara
cv2.destroyAllWindows()
camara.release()
