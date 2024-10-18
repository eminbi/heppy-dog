import logging
from logging import getLogger

# 로그 모듈 사용
logger = getLogger(__name__)

def some_function():
    try:
        # 일반적인 작업 수행
        logger.info("some_function() 실행 중")
    except Exception as e:
        # 오류 발생 시 로그 기록
        logger.error(f"오류 발생: {e}")
