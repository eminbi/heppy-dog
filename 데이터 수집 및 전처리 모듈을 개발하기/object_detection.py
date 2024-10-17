# 비디오 파일이 열렸는지 확인
if not cap.isOpened():
    print(f"Error: {video_path} 파일을 열 수 없습니다.")
else:
    print(f"{video_path} 파일을 성공적으로 열었습니다.")
