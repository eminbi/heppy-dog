import cv2
import numpy as np

# YOLO 모델 및 가중치 파일 경로
model_path = "yolov3.weights"
config_path = "yolov3.cfg"
class_names_path = "coco.names"

# 클래스 이름 불러오기
with open(class_names_path, 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# YOLO 네트워크 로드
net = cv2.dnn.readNet(model_path, config_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# 비디오 파일 경로 설정
video_path = "H:/my_videos/영상/input_video.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지 전처리 (YOLO에서 사용하는 입력 크기로 맞추기)
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    
    # 객체 탐지
    detections = net.forward(output_layers)
    
    class_ids = []
    confidences = []
    boxes = []
    
    # 탐지 결과 분석
    for out in detections:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:  # 신뢰도 임계치
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # 박스 좌표 계산
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Non-maximal suppression 적용 (중복 박스 제거)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(class_names[class_ids[i]])
            confidence = confidences[i]
            
            # 탐지된 객체에 대한 박스 그리기
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # 탐지된 결과 화면에 출력
    cv2.imshow("Object Detection", frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
