import cv2
import os
import numpy as np

# 비디오 파일 경로 설정
video_path = "h:/my_videos/input_video.mp4"

# 비디오 파일이 존재하는지 확인
if not os.path.exists(video_path):
    print(f"Error: {video_path} 파일이 존재하지 않습니다.")
else:
    # 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)

    # 비디오 파일이 제대로 열렸는지 확인
    if not cap.isOpened():
        print(f"Error: {video_path} 파일을 열 수 없습니다.")
    else:
        print(f"{video_path} 파일을 성공적으로 열었습니다.")

        # 프레임별로 처리하여 특징 추출
        while True:
            ret, frame = cap.read()
            if not ret:
                print("비디오 재생이 완료되었습니다.")
                break

            # 이미지 전처리 (예: 그레이스케일 변환)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 특징 추출 (예: 가장자리 검출)
            edges = cv2.Canny(gray_frame, 50, 150)

            # 추출된 특징을 보여줌
            cv2.imshow('Edges', edges)

            # 'q' 키를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 비디오 파일 해제 및 창 닫기
        cap.release()
        cv2.destroyAllWindows()
