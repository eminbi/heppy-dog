import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import pandas as pd

# 라벨링된 데이터 불러오기
def load_labeled_data(csv_file):
    data = pd.read_csv(csv_file)
    frames = data['frame'].values  # 프레임 이름
    actions = data['action'].values  # 행동 라벨
    return frames, actions

# 간단한 LSTM 모델 정의
def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(64, input_shape=input_shape, return_sequences=True),
        LSTM(64),
        Dense(32, activation='relu'),
        Dense(5, activation='softmax')  # 예시: 5개의 성격/감정 상태 분류
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# 학습 데이터 로드 (임의 데이터 예시)
frames, actions = load_labeled_data('labeled_data.csv')

# 프레임을 기반으로 한 학습 데이터 준비 (여기서는 임의 값 사용)
X_train = [[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]]  # 예시 데이터
y_train = [[1, 0, 0, 0, 0]]  # 첫 번째 성격/감정 분류

# LSTM 모델 학습
model = create_lstm_model(input_shape=(3, 3))
model.fit(X_train, y_train, epochs=10)

# 새로운 데이터에 대한 예측
X_new = [[[0.2, 0.3, 0.4], [0.5, 0.6, 0.7], [0.8, 0.9, 1.0]]]  # 새로운 데이터
predictions = model.predict(X_new)
print("예측 결과:", predictions)
