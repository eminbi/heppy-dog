import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def detect_scene_changes(video_path, threshold=30):
    """
    장면 전환을 감지하여 구간을 나누는 함수
    :param video_path: MP4 파일 경로
    :param threshold: 장면 전환 감지 민감도(값이 낮을수록 작은 변화도 감지)
    :return: 장면 전환 시간이 저장된 리스트
    """
    cap = cv2.VideoCapture(video_path)
    scene_changes = []
    prev_frame = None
    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is not None:
            frame_diff = cv2.absdiff(prev_frame, gray_frame)
            diff_score = frame_diff.sum() / 255

            if diff_score > threshold:
                scene_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # 초 단위 시간
                scene_changes.append(scene_time)

        prev_frame = gray_frame

    cap.release()
    return scene_changes

def split_video_by_scene(input_file, scene_changes):
    """
    장면 전환을 기준으로 MP4 파일을 구간별로 나누는 함수
    :param input_file: MP4 파일 경로
    :param scene_changes: 장면 전환 시간 리스트
    """
    video = VideoFileClip(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # 출력 폴더 생성
    output_folder = "output_scene_segments"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_time = 0
    for i, end_time in enumerate(scene_changes + [video.duration]):
        segment = video.subclip(start_time, end_time)
        output_filename = os.path.join(output_folder, f"{base_name}_scene_{i+1}.mp4")
        segment.write_videofile(output_filename, codec="libx264")
        start_time = end_time

    video.close()
    print(f"장면 전환에 따른 구간 나누기가 완료되었습니다. {output_folder} 폴더에서 확인하세요.")

# MP4 파일 경로와 장면 전환 감지 민감도 설정
input_file = "C:\\Users\\eminb\\Desktop\\example_video.mp4"
scene_changes = detect_scene_changes(input_file, threshold=30)

# 장면 전환에 따라 구간 나누기
split_video_by_scene(input_file, scene_changes)
