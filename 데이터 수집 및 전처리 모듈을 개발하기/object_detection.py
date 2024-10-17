import cv2

# 비디오 파일 경로 설정
video_path = "H:/my_videos/영상/input_video.mp4"

# 비디오 파일 열기
cap = cv2.VideoCapture(video_path)

# 비디오 파일이 열렸는지 확인
if not cap.isOpened():
    print(f"Error: {video_path} 파일을 열 수 없습니다.")
else:
    print(f"{video_path} 파일을 성공적으로 열었습니다.")

# 프레임 처리
while True:
    ret, frame = cap.read()
    if not ret:
        print("비디오 재생이 완료되었습니다.")
        break

    # 비디오 출력
    cv2.imshow('Frame', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
