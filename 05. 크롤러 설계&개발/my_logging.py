"""로그 전용 모듈"""
import logging.config
import settings

def get_my_logger(name):
    logging.config.dictConfig(settings.LOGGING_CONF)
    return logging.getLogger(name)

logger = get_my_logger(__name__)

if __name__ == "__main__":
    """my_logging 을 사용해봅니다."""
    logger.debug("DEBUG 레벨입니다.")
    logging.info("INFO 레벨입니다.")
    logger.warning("WARNING 레벨입니다.")
    logger.error("ERROR 레벨입니다.")
    logger.critical("CRITICAL 레벨입니다.")