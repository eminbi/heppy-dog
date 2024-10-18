import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# 모델 하이퍼파라미터 설정
input_shape = (64, 64, 3)  # 이미지 크기 (64x64) 및 RGB 채널
num_classes = 10  # 예측할 행동의 클래스 수 (예시: 10개의 행동)

# 하이퍼파라미터 설정
batch_size = 32
epochs = 20
learning_rate = 0.001

# 데이터 경로 설정
train_data_dir = "data/train"
validation_data_dir = "data/validation"

# 이미지 전처리를 위한 데이터 증강 생성기
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # 픽셀 값을 0-255에서 0-1로 정규화
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

# 데이터 생성기 설정
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(64, 64),
    batch_size=batch_size,
    class_mode="categorical"
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(64, 64),
    batch_size=batch_size,
    class_mode="categorical"
)

# CNN 모델 구성
model = Sequential()

# 입력 레이어
model.add(Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 두 번째 레이어
model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 세 번째 레이어
model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 완전 연결 레이어
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation="softmax"))

# 모델 컴파일
optimizer = Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

# 모델 훈련
model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# 학습된 모델 저장
model_save_path = "models/pet_behavior_cnn.h5"
if not os.path.exists("models"):
    os.makedirs("models")
model.save(model_save_path)
print(f"모델이 저장되었습니다: {model_save_path}")
