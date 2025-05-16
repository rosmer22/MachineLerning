import cv2

cap = cv2.VideoCapture('http://10.104.114.196:8080//video')
while True:
    success, img = cap.read()
    if not success:
        break
    imagen_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", imagen_grises)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()