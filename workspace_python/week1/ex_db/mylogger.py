import logging


# 로그 파일 생성 함수
def make_logger(fileNm, name="custom_logger"):
    logger = logging.getLogger(name)

    # 중복 핸들러 추가 방지
    if not logger.hasHandlers():
        # 로그 레벨 설정
        logger.setLevel(logging.DEBUG)

        # 로그 포맷 수정
        log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # 콘솔 핸들러 추가
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(log_format)

        # 파일 핸들러 추가
        file_handler = logging.FileHandler(filename=fileNm, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_format)

        # 핸들러 추가
        logger.addHandler(console)
        logger.addHandler(file_handler)

        # 중복 로깅 방지
        logger.propagate = False

    return logger


# 테스트 코드
if __name__ == '__main__':
    logger = make_logger("app.log", "test")
    logger.debug("디버그 메시지입니다")
    logger.info("정보 메시지입니다")
    logger.warning("경고 메시지")
    logger.error("심각한 오류")
