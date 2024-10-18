import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2

def preprocess_input_frame(frame, target_size=(64, 64)):
    """
    입력 프레임을 모델에 맞게 전처리하는 함수

    Args:
    - frame: 비디오 프레임
    - target_size: 모델 입력 크기

    Returns:
    - 전처리된 프레임
    """
    # 크기 조정
    frame_resized = cv2.resize(frame, target_size)
    
    # 정규화 (0-255 범위를 0-1로)
    frame_normalized = frame_resized / 255.0
    
    # 배치 차원을 추가하여 (64, 64, 3) -> (1, 64, 64, 3)
    return np.expand_dims(frame_normalized, axis=0)

def predict_behavior(model, frame):
    """
    학습된 모델을 사용하여 프레임에 대한 행동 예측

    Args:
    - model: 학습된 모델
    - frame: 비디오 프레임

    Returns:
    - 예측된 행동 클래스
    """
    preprocessed_frame = preprocess_input_frame(frame)
    predictions = model.predict(preprocessed_frame)
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class[0]

def run_prediction_on_video(model_path, video_path):
    """
    비디오 파일에 대한 행동 예측을 수행하는 함수

    Args:
    - model_path: 학습된 모델 파일 경로
    - video_path: 예측할 비디오 파일 경로
    """
    # 모델 로드
    model = load_model(model_path)
    if model is None:
        print("모델을 로드할 수 없습니다.")
        return

    # 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"비디오 파일을 열 수 없습니다: {video_path}")
        return

    # 비디오의 각 프레임에 대한 예측
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("더 이상 읽을 프레임이 없습니다.")
            break

        # 프레임에 대한 행동 예측
        predicted_behavior = predict_behavior(model, frame)
        print(f"예측된 행동 클래스: {predicted_behavior}")

        # 'q' 키를 누르면 중지
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("비디오 재생을 종료합니다.")
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 예시 사용법
    model_path = "models/pet_behavior_cnn.h5"
    video_path = "input_videos/test_video.mp4"
    
    run_prediction_on_video(model_path, video_path)
