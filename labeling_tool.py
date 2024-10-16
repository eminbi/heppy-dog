import pandas as pd

def save_labels_to_csv(frame_files, labels, output_csv):
    label_data = {'frame': frame_files, 'action': labels}
    df = pd.DataFrame(label_data)
    df.to_csv(output_csv, index=False)
    print(f"라벨링 데이터가 {output_csv}에 저장되었습니다.")

# 예시 수동 라벨링 데이터
frame_files = ['frame_0.jpg', 'frame_1.jpg', 'frame_2.jpg']
labels = ['꼬리 흔들기', '짖기', '귀를 내림']

# CSV 파일로 라벨링 데이터 저장
save_labels_to_csv(frame_files, labels, 'labeled_data.csv')
