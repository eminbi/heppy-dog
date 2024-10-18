import cv2
import os

def process_video(video_path, output_dir):
    # 비디오 파일이 존재하는지 확인
    if not os.path.exists(video_path):
        print(f"파일 경로가 존재하지 않습니다: {video_path}")
        return

    # 출력 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)

    # 비디오 파일이 성공적으로 열렸는지 확인
    if not cap.isOpened():
        print(f"비디오 파일을 열 수 없습니다: {video_path}")
        return

    # 비디오 정보 출력
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"총 프레임 수: {frame_count}, FPS: {fps}")
    print(f"프레임 크기: {width}x{height}")

    frame_idx = 0

    # 비디오 프레임을 하나씩 읽어 처리
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("더 이상 읽을 프레임이 없습니다.")
            break

        # 현재 프레임 저장 (이미지 파일로 저장)
        frame_filename = os.path.join(output_dir, f"frame_{frame_idx:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"{frame_filename} 저장됨")

        # 'q'를 누르면 중지
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_idx += 1

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "input_videos/video.mp4"  # 분석할 MP4 파일 경로
    output_dir = "output_frames"  # 출력 프레임을 저장할 디렉토리

    process_video(video_path, output_dir)
