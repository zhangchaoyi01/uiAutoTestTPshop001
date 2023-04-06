import logging.handlers
import os
from config import BASE_PATH


class GetLogging:
    logger = None

    @classmethod
    def get_logger(cls):
        # 确保调用多次时，使用的是同一个日志器
        if cls.logger is None:
            # 1.获取日志器
            cls.logger = logging.getLogger()
            # 2.设置日志级别
            cls.logger.setLevel(logging.INFO)
            # 3.获取控制台处理器
            sh = logging.StreamHandler()
            # 获取本地项目路径
            file_path = BASE_PATH + os.sep + "log" + os.sep + "page_all.log"
            # 4.获取文件处理器，文件以时间分割
            th = logging.handlers.TimedRotatingFileHandler(file_path, when='midnight', interval=1, backupCount=30,
                                                           encoding="utf-8")
            # 5.设置格式
            format = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s | %(funcName)s:%(lineno)d] - %(message)s'
            # 6.把格式添加到格式器
            fm = logging.Formatter(format)
            # 7.将格式器添加到处理器 -->控制台
            sh.setFormatter(fm)
            # 8.将格式器添加到处理器 -->文件
            th.setFormatter(fm)
            # 9.获取处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        # return 返回日志器
        return cls.logger
