import logging
import os
from datetime import datetime

# 로그 파일 경로 설정
log_directory = "logs/"
log_file_name = f"project_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(log_directory, log_file_name)

# 로그 디렉토리 생성
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,  # 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),  # 로그 파일로 출력
        logging.StreamHandler()  # 콘솔로 출력
    ]
)

# 로깅 예시
def log_example():
    logging.debug("이것은 디버그 메시지입니다.")
    logging.info("이것은 정보 메시지입니다.")
    logging.warning("이것은 경고 메시지입니다.")
    logging.error("이것은 오류 메시지입니다.")
    logging.critical("이것은 치명적인 오류 메시지입니다.")

if __name__ == "__main__":
    log_example()
