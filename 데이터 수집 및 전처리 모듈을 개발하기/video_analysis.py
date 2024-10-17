import cv2
import os

# 비디오 파일 경로 설정
video_path = "H:/my_videos/video.mp4"  # 비디오 파일 경로를 정확하게 입력

# 경로가 정확한지 확인
if not os.path.exists(video_path):
    print(f"파일 경로가 존재하지 않습니다: {video_path}")
    exit()

# 비디오 파일 불러오기
cap = cv2.VideoCapture(video_path)

# 비디오 파일이 성공적으로 열렸는지 확인
if not cap.isOpened():
    print(f"비디오 파일을 열 수 없습니다: {video_path}")
    exit()

# 비디오 파일 정보 출력
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 총 프레임 수
fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임 수 (FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 프레임 너비
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 프레임 높이

print(f"총 프레임 수: {frame_count}, FPS: {fps}")
print(f"프레임 크기: {int(width)}x{int(height)}")

# 프레임을 순차적으로 읽어서 화면에 표시
while cap.isOpened():
    ret, frame = cap.read()  # 비디오의 한 프레임 읽기
    if not ret:  # 더 이상 읽을 프레임이 없으면 중지
        print("더 이상 읽을 프레임이 없습니다.")
        break

    # 프레임을 화면에 표시
    cv2.imshow('Video Frame', frame)

    # 'q' 키를 누르면 중지
    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("비디오 재생을 종료합니다.")
        break

# 자원 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
