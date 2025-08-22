import numpy as np
import cv2
from ultralytics import YOLO
import pywhatkit
import datetime
import threading

cap= cv2.VideoCapture(0)
model= YOLO('yolo11n-seg.pt')

target_object = "person"
phone_number = "+8801703124713"  # include country code
message_text = "halay abar mobile haate nise"
message_sent = False
j=0

def send_whatsapp_message():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1   # pywhatkit requires at least +1 minute
    pywhatkit.sendwhatmsg(phone_number, message_text, hour, minute, wait_time=10)
    print("Message scheduled successfully!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(frame)
    r = result[0]
    class_ids = r.boxes.cls.cpu().numpy()
    names = [model.names[int(cls_id)] for cls_id in class_ids]

    if 'cell phone' in names and not message_sent:
        i = names.index('cell phone')
        bbox = r.boxes.xywh.cpu().numpy()
        x, y, w, h = bbox[i]
        x1 = int(x - w / 2)
        y1 = int(y - h / 2)
        x2 = int(x + w / 2)
        y2 = int(y + h / 2)
        final_img = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
        j+=1
        print(j)
        if j==1000:
            threading.Thread(target=send_whatsapp_message, daemon=True).start()
            j=0

            #message_sent = True  # prevent multiple sends
    else:
        final_img = frame

    cv2.imshow('frame', final_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()