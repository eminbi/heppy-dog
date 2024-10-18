import cv2
import os
import numpy as np

def preprocess_video(video_path, output_dir, resize_dim=(640, 480), normalize=True, gray_scale=False, frame_rate=30):
    """
    비디오 파일을 전처리하는 함수.
    
    Args:
        video_path (str): 입력 비디오 파일 경로.
        output_dir (str): 처리된 프레임이 저장될 디렉토리.
        resize_dim (tuple): 프레임의 크기를 조정할 크기 (가로, 세로).
        normalize (bool): True일 경우, 프레임 픽셀값을 0~1로 정규화.
        gray_scale (bool): True일 경우, 프레임을 흑백으로 변환.
        frame_rate (int): 초당 프레임 수 (FPS).
    
    Returns:
        None: 처리된 프레임을 output_dir에 저장.
    """
    
    # 비디오 파일 확인
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"비디오 파일을 찾을 수 없습니다: {video_path}")
    
    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise Exception(f"비디오 파일을 열 수 없습니다: {video_path}")

    frame_idx = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 설정된 프레임 비율에 따라 몇 프레임마다 처리할지 결정
    frame_interval = int(fps // frame_rate)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break  # 더 이상 읽을 프레임이 없을 경우 중지
        
        # 프레임을 설정된 간격으로 처리
        if frame_idx % frame_interval == 0:
            # 이미지 크기 조정
            frame = cv2.resize(frame, resize_dim)
            
            # 흑백 변환 옵션
            if gray_scale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 정규화 옵션
            if normalize:
                frame = frame.astype(np.float32) / 255.0

            # 처리된 프레임 저장
            output_filename = os.path.join(output_dir, f"frame_{frame_idx}.jpg")
            cv2.imwrite(output_filename, frame)
        
        frame_idx += 1

    # 자원 해제
    cap.release()
    print(f"프레임이 {output_dir}에 저장되었습니다.")


if __name__ == "__main__":
    video_path = "input_videos/sample_video.mp4"  # 예시 경로
    output_dir = "output_frames"  # 처리된 프레임이 저장될 디렉토리
    preprocess_video(video_path, output_dir)
