from logging import getLogger

logger = getLogger(__name__)

def train_model():
    logger.info("모델 학습 시작")
    try:
        # 모델 학습 코드
        logger.debug("모델 학습 성공")
    except Exception as e:
        logger.error(f"모델 학습 중 오류 발생: {e}")
