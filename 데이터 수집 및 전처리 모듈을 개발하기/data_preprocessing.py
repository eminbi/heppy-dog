import cv2
import mediapipe as mp

def preprocess_video(video_path):
    cap = cv2.VideoCapture(video_path)
    mp_holistic = mp.solutions.holistic
    with mp_holistic.Holistic() as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # 처리 과정 추가
            results = holistic.process(frame)
            # 필요 시 프레임 저장 또는 특징 추출
    cap.release()

if __name__ == "__main__":
    preprocess_video("sample_video.mp4")
