import os
from tensorflow.keras.models import load_model

def save_trained_model(model, model_save_path):
    """
    학습된 모델을 저장하는 함수

    Args:
    - model: 학습된 Keras 모델 객체
    - model_save_path: 모델을 저장할 파일 경로
    """
    # 모델 디렉터리가 존재하지 않으면 생성
    model_dir = os.path.dirname(model_save_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # 모델 저장
    model.save(model_save_path)
    print(f"모델이 저장되었습니다: {model_save_path}")

def load_trained_model(model_save_path):
    """
    저장된 모델을 로드하는 함수

    Args:
    - model_save_path: 모델이 저장된 파일 경로

    Returns:
    - 로드된 모델 객체
    """
    if not os.path.exists(model_save_path):
        print(f"모델 파일을 찾을 수 없습니다: {model_save_path}")
        return None

    model = load_model(model_save_path)
    print(f"모델이 로드되었습니다: {model_save_path}")
    return model
