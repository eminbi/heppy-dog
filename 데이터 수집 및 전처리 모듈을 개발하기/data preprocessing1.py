from logging import getLogger

logger = getLogger(__name__)

def preprocess_data():
    logger.info("데이터 전처리 시작")
    # 전처리 작업 수행
    try:
        # 데이터 처리 코드
        logger.debug("프레임 분할 성공")
    except Exception as e:
        logger.error(f"데이터 전처리 중 오류 발생: {e}")
