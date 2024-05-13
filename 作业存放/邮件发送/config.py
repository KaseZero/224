import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.txt',
                    filemode='a')


if __name__ == '__main__':
    logging.info("接口测试")
