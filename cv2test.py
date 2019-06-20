import cv2

c1 = cv2.VideoCapture(0)

while True:
	r1, v1 = c1.read()
	cv2.imshow('Cam1', v1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

c1.release()
cv2.destroyAllWindows()
