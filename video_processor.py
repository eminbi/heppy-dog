import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_folder, f'frame_{frame_count}.jpg')
        cv2.imwrite(frame_path, frame)  # 프레임을 이미지 파일로 저장
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

# 비디오 파일에서 프레임 추출 실행
extract_frames('your_video.mp4', 'output_frames')
