from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model("images/img1.jpg")

# Draw results on image manually
for r in results:
    img = r.plot()  # draws boxes, labels on the image

cv2.imshow("Result", img)
cv2.waitKey(0)  # waits until you press any key
cv2.destroyAllWindows()