import numpy as np

# 예측 결과 저장
def save_predictions_to_csv(frames, predictions, output_csv):
    predicted_actions = np.argmax(predictions, axis=1)
    results = {'frame': frames, 'predicted_action': predicted_actions}
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"예측 결과가 {output_csv}에 저장되었습니다.")

# 예측 결과 저장 예시
save_predictions_to_csv(frames, predictions, 'predicted_results.csv')

# 성능 평가 (정확도 예시)
def evaluate_model(model, X_test, y_test):
    _, accuracy = model.evaluate(X_test, y_test)
    print(f"모델 정확도: {accuracy:.2f}")

# 테스트 데이터로 성능 평가
X_test = X_train  # 테스트 데이터를 학습 데이터로 가정한 예시
y_test = y_train
evaluate_model(model, X_test, y_test)
