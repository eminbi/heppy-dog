from scripts.video_processor import VideoProcessor
from scripts.object_detection import ObjectDetection
from scripts.behavior_analyzer import BehaviorAnalyzer
from scripts.data_saver import DataSaver

def main():
    video_path = "H:/my_videos/input_video.mp4"
    
    # 비디오 처리
    vp = VideoProcessor(video_path)
    vp.open_video()
    
    # 객체 탐지
    od = ObjectDetection("yolov3.weights", "yolov3.cfg", "coco.names")
    
    # 행동 분석
    analyzer = BehaviorAnalyzer()

    # 프레임 처리 및 분석
    while True:
        ret, frame = vp.cap.read()
        if not ret:
            break

        objects = od.detect_objects(frame)
        analyzer.analyze_behavior(objects)

    # 분석 결과 저장
    analyzer.save_analysis("results/behavior_analysis.csv")

if __name__ == "__main__":
    main()
